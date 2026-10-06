## pftk Tutorial 4

## The Allocation DataFrame

An allocation DataFrame is created using the pandas data structure DataFrame. This structure consists of a series of
python datetime objects as indexes, and stock symbols for column headings. The last column in the DataFrame is the
symbol \_CASH, which represents what percentage of a portfolio is held in cash. Each row has the distribution of the
portfolio recorded via values in each column that represent how much of the portfolio is in that stock at that date and
time. Normally these values are normalized so that they add to one.

## Creating an Allocation

In order to setup an allocation table, we must first create the DataFrame. A pandas DataFrame object consists of
indices, column headings, and data. Datetime objects are used for the indices. We can create a list of timestamps over
the time period we are interested in looking in a similar fashion to how we produce timestamps for the DataAccess
utility. We create a list of timestamps like so:

```
dt_start = dt.datetime(2004, 1, 1)
dt_end = dt.datetime(2009, 12, 31)

# We need closing prices so the timestamp should be hours=16.
dt_timeofday = dt.timedelta(hours=16)

# Get a list of trading days between the start and the end.
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

# Creating an object of the dataaccess class with Yahoo as the source.
c_dataobj = da.DataAccess('Yahoo')
```

These timestamps will help us look at the dates between 2004 through the end of 2009.

## Symbols

The allocation DataFrame describes the distribution of a portfolio across several stocks. It also details how much of
the portfolio should be in cash at a point in time. In this particular example, we wish to look at the first 20 stocks
of the S&P500. The way we set up column headers to reflect this stock symbol information is like so:

```
ls_symbols = c_dataobj.get_symbols_from_list('sp5002012')
ls_symbols = ls_symbols[:20]
ls_symbols.append('_CASH')
```

## Allocations

Now that we have the symbols and time period for our allocation, we must determine how much of the portfolio will be in
each equity at each date. Normally this will be the most involved part in creating an allocation. In this particular
example we will be creating a new random distribution for our portfolio at the start of each month. We create random
values for the first row in our allocation table like so:

```
na_vals = np.random.randint(0, 1000, len(ls_symbols))
# Normalize the row - Typecasting as everything is int.
na_vals = na_vals / float(sum(na_vals))
# Reshape to a 2D matrix to append into dataframe.
na_vals = na_vals.reshape(1, -1)
```

We then make a one row DataFrame for the first date using the constructor like so:

```
df_alloc = pd.DataFrame(na_vals, index=[ldt_timestamps[0]], columns=ls_symbols)
```

Since we only desire to reallocate our portfolio once a month, we only add a new row to the DataFrame for each new
month. We must then repeat the process of creating and normalizing random values for the allocation. Then we create
another DataFrame row and append it to what we have already. Thus we build up an allocation table across all of the
months in our list of timestamps.

```
dt_last_date = ldt_timestamps[0]
# Looping through all dates and creating monthly allocations
for dt_date in ldt_timestamps[1:]:
    if dt_last_date.month != dt_date.month:
        # Create allocation
        na_vals = np.random.randint(0, 1000, len(ls_symbols))
        na_vals = na_vals / float(sum(na_vals))
        na_vals = na_vals.reshape(1, -1)
        # Append to the dataframe
        df_new_row = pd.DataFrame(na_vals, index=[dt_date], columns=ls_symbols)
        df_alloc = df_alloc.append(df_new_row)
    dt_last_date = dt_date
```

## Using an Allocation

pftk uses allocation tables for a variety of tasks, most notably in backtesting strategies. In order to use an
allocation table, you can either pass it to the function you wish to use it with, or store it in a pickle file for later
usage. To do the latter, you must import the cPickle package and dump the object like so:

```
output=open("allocations.pkl","wb")
cPickle.dump(alloc,output)
```

Then you may use the allocation at a later point in time.