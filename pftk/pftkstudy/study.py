#
# Example use of the event profiler
#
import datetime as dt
import numpy as np

# PFTK imports
import pftk.pftkstudy.events as ev
import pftk.pftkstudy.event_profiler as ep
import pftk.pftkutil.qsdateutil as du
import pftk.pftkutil.data_access as da

if __name__ == '__main__':

    ls_symbols = np.loadtxt('symbol-set1.txt',dtype='S10',comments='#')
    dt_start = dt.datetime(2008,1,1)
    dt_end = dt.datetime(2009,12,31)
    ldt_timestamps = du.getNYSEdays( dt_start, dt_end, dt.timedelta(hours=16) )

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    eventMatrix = ev.find_events(ls_symbols,d_data,verbose=True)
    ep.eventprofiler(eventMatrix, d_data,
            i_lookback=20,i_lookforward=20,
            s_filename="MyEventStudy")
