#!/usr/bin/env python

# Pull Updated data from EODHistoricalData.

import urllib3
import requests
import datetime
import os
import getopt
import sys
import pandas as pd
import duckdb
from io import StringIO

__author__="charlesg"
__date__ ="$$"

from pftk.pftkutil.data_access import get_db_path, SCHEMA

urllib3.disable_warnings()

def usage():
	print(sys.argv[0] + " -h|--help -k|--key=KEY -s|--symbols=FILE [--source=NAME] [--db=PATH]")
	print("  -k|--key: EOD API key (or set EOD_API_KEY environment variable)")
	print("  -s|--symbols: File with one symbol per line (default: symbols.txt)")
	print("  --source: Data source name stored in the DB (default: EODHistoricalData)")
	print("  --db: DuckDB file (default: $PFTK_DB or ./market.duckdb)")

def fetch_eod(symbol, key):
    '''Fetch full daily history for one symbol from EODHistoricalData as a DataFrame.'''
    _now = datetime.datetime.now()
    url = "https://eodhistoricaldata.com/api/table.csv"
    fields = {'a':0, 'b':1, 'c':2000, 'd':_now.month-1, 'e':_now.day, 'f':_now.year, 's': symbol, 'api_token': key }
    r = requests.get(url, fields)
    r.raise_for_status()
    df = pd.read_csv(StringIO(r.content.decode('utf-8')), skipfooter=1, parse_dates=[0], index_col=0, engine='python')
    if df.shape[1] < 6:
        raise ValueError("unexpected response: {0!r}".format(r.text[:60]))
    return df

# Add a new data source by adding a fetch function returning a DataFrame indexed by date with columns
# open, high, low, close, adjusted close, volume (in that order).
SOURCES = {'EODHistoricalData': fetch_eod}

def get_data(db_path, source, ls_symbols, key):
    '''Pull symbols from a source and upsert them into the prices table.
    @db_path: DuckDB file
    @source: key of SOURCES, also stored in the prices.source column
    @ls_symbols: list of symbols to read
    @key: API key
    '''
    fetch = SOURCES[source]
    con = duckdb.connect(db_path)
    con.execute(SCHEMA)

    ls_missed_syms = []
    for symbol in ls_symbols:
        # A leading "$" means an index (e.g. $SPX), which EOD spells "^SPX".
        api_symbol = '^' + symbol[1:] if symbol[0] == '$' else symbol
        print("Getting {0}".format(api_symbol))
        try:
            df = fetch(api_symbol, key)
            df = df.iloc[:, :6]
            df.columns = ['open', 'high', 'low', 'close', 'adj_close', 'volume']
            df.index.name = 'date'
            df = df.reset_index()
            df.insert(0, 'symbol', symbol)
            df.insert(0, 'source', source)
            con.execute("INSERT OR REPLACE INTO prices SELECT * FROM df")
        except requests.HTTPError as err:
            # Never print err itself: its message contains the URL, including the API token.
            code = err.response.status_code
            if code == 401:
                print("API key rejected (401). Check EOD_API_KEY in finSandbox/.env")
                sys.exit(1)
            ls_missed_syms.append(symbol)
            print("Unable to fetch data for stock: {0}: HTTP {1}".format(symbol, code))
        except Exception as err:
            ls_missed_syms.append(symbol)
            print("Unable to fetch data for stock: {0}: {1}".format(symbol, err))

    con.close()
    print("All done. Got {0} stocks. Could not get {1}".format(len(ls_symbols) - len(ls_missed_syms), len(ls_missed_syms)))
    return ls_missed_syms

def read_symbols(s_symbols_file):
    '''Read a list of symbols'''
    ls_symbols=[]
    file = open(s_symbols_file, 'r')
    for line in file.readlines():
        str_line = str(line)
        if str_line.strip(): 
            ls_symbols.append(str_line.strip())
    file.close()
    return ls_symbols  

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hk:s:", ["help", "key=", "symbols=", "source=", "db="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)

    key = os.getenv('EOD_API_KEY')  # Try environment variable first
    symbols_file = 'symbols.txt'
    source = 'EODHistoricalData'
    db_path = get_db_path()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-k", "--key"):
            key = a  # Command line overrides environment variable
        elif o in ("-s", "--symbols"):
            symbols_file = a
        elif o == "--source":
            source = a
        elif o == "--db":
            db_path = a

    if not key:
        print("Error: API key required. Set EOD_API_KEY environment variable or use -k option.")
        usage()
        sys.exit(2)
    if source not in SOURCES:
        print("Error: unknown source {0}. Known: {1}".format(source, ", ".join(SOURCES)))
        sys.exit(2)

    get_data(db_path, source, read_symbols(symbols_file), key)

if __name__ == '__main__':
    main()
