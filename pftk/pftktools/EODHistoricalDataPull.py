#!/usr/bin/env python

# Pull Updated data from EODHistoricalData.

import urllib3
import requests
import datetime
import os
import getopt
import sys
import pandas as pd
from io import StringIO

__author__="charlesg"
__date__ ="$$"

urllib3.disable_warnings()

def usage():
	print(sys.argv[0] + " -h|--help -k|--key=KEY -d|--dest=DESTINATION DIR")

def get_data(data_path, ls_symbols, key):
    '''Read data from EODHistoricalData
    @data_path : string for where to place the output files
    @ls_symbols: list of symbols to read
    '''

    # Create path if it doesn't exist
    if not (os.access(data_path, os.F_OK)):
        os.makedirs(data_path)

    ls_missed_syms = []
    
    _now =datetime.datetime.now();
    miss_ctr=0; #Counts how many symbols we could not get
    for symbol in ls_symbols:
        # Preserve original symbol since it might
        # get manipulated if it starts with a "$"
        symbol_name = symbol
        if symbol[0] == '$':
            symbol = '^' + symbol[1:]

        symbol_data=list()
        print("Getting {0}".format(symbol))
        
        try:
            # EOD Historical Data
            url = "https://eodhistoricaldata.com/api/table.csv"
            fields = {'a':0, 'b':1, 'c':2000, 'd':_now.month-1, 'e':_now.day, 'f':_now.year, 's': symbol, 'api_token': key }
            r = requests.get(url, fields)
            
            df = pd.read_csv(StringIO(r.content.decode('utf-8')), skipfooter=1, parse_dates=[0], index_col=0, engine='python')

            # Now writing data to file
            fn = data_path + "/" + symbol_name + ".csv"
            
            df.to_csv(fn, encoding='utf-8')    

        except urllib3.exceptions.HTTPError:
            miss_ctr += 1
            ls_missed_syms.append(symbol_name)
            print("Unable to fetch data for stock: {0} at {1}").format(symbol_name, url)
            
    print("All done. Got {0} stocks. Could not get {1}".format(len(ls_symbols) - miss_ctr, miss_ctr))
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
        opts, args = getopt.getopt(sys.argv[1:], "ht:k:d:", ["help", "key=", "dest="])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    
    path = ""
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-d", "--dest"):
            path = a
        elif o in ("-k", "--key"):
            key = a
        else:
            assert False, "unhandled option"
    
    if not os.path.isdir(path):
        try:
            raise Exception("Destination directory does not exist: ", path)
        except:
            raise
    else:
        ls_symbols = read_symbols('symbols.txt')
        get_data(path, ls_symbols, key)

if __name__ == '__main__':
    main()

