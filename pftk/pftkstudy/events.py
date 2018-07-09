# (c) 2018, charlesg@unixrealm.com - Fork from QSTK
# (c) 2011, 2012 Georgia Tech Research Corporation
# This source code is released under the New BSD license.

#
#@author: Vishal Shekhar
#@contact: mailvishalshekhar@gmail.com
#@summary: Example Event Datamatrix acceptable to EventProfiler App
#

import pandas 
from pftk.pftkutil import data_access as da
import numpy as np
import math
import pftk.pftkutil.qsdateutil as du
import datetime as dt
import pftk.pftkutil.data_access as da

"""
Accepts a list of symbols along with start and end date
Returns the Event Matrix which is a pandas Datamatrix
Event matrix has the following structure :
    |IBM |GOOG|XOM |MSFT| GS | JP |
(d1)|nan |nan | 1  |nan |nan | 1  |
(d2)|nan | 1  |nan |nan |nan |nan |
(d3)| 1  |nan | 1  |nan | 1  |nan |
(d4)|nan |  1 |nan | 1  |nan |nan |
...................................
...................................
Also, d1 = start date
nan = no information about any event.
1 = status bit(positively confirms the event occurence)
"""

def find_events(symbols, d_data, verbose=False):
	# Get the data from the data store
	storename = "Yahoo" # get data from our daily prices source
	# Available field names: open, close, high, low, close, actual_close, volume
	closefield = "close"
	volumefield = "volume"
	window = 10

	if verbose:
            print(__name__, " reading data")
	close = d_data[closefield]
	if verbose:
            print(__name__, " finding events")
	for symbol in symbols:
	    close[symbol][close[symbol]>= 1.0] = np.NAN
	    for i in range(1,len(close[symbol])):
	        if np.isnan(close[symbol][i-1]) and close[symbol][i] < 1.0 :#(i-1)th was > $1, and (i)th is <$1
             		close[symbol][i] = 1.0 #overwriting the price by the bit
	    close[symbol][close[symbol]< 1.0] = np.NAN
	return close
