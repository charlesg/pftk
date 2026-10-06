## QSTK Tutorial 1

## Overview

In this tutorial we will take a look at using QSTK code for basic time series analysis of stock price data. Python works
well for this because you can do some very powerful analyses in a few lines of code. There are also convenient libraries
for displaying data easily. All of the code you see below is available in QSTK/Examples/Basic/tutorial1.py.

In this tutorial we focus on techniques for looking at equity price data, but you might also want to consult this more
general [Numpy Learn](https://numpy.org/learn/) about NumPy as well.

Acknowledgments: We heavily leverage pandas and NumPy.

## Prerequisites

Make sure you have installed QSTK correctly. For instructions, visit [QSToolKit\_Installation\_Guide](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=QSToolKit_Installation_Guide "QSToolKit Installation Guide").

## Reading Historical Data

In this first section of the code we import several useful libraries. numpy, pylab and matplotlib provide a number of functions to Python that give it MATLAB-like capabilities. datetime helps us manipulate dates. The qstkutil items are from the QuantSoftware ToolKit

```
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
```

We'll be using historical adjusted close data. QSTK has a DataAccess class designed to quickly read this data into pandas DataFrame object. We must first select which symbols we're interested in, and for which time periods.

```
ls_symbols = ["AAPL", "GLD", "GOOG", "$SPX", "XOM"]
dt_start = dt.datetime(2006, 1, 1)
dt_end = dt.datetime(2010, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)
```

In the first line above we create a list of 5 equities we're interested to look at. Next we specify a start date and and end date using Python's datetime feature. Finally, we get a list of timestamps that represent NYSE closing times between the start and end dates. The reason we need to specify 16:00 hours is because we want to read the data that was available to us at the close of the day.

Now we are ready to read the data in:

```
c_dataobj = da.DataAccess('Yahoo')
ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
d_data = dict(zip(ls_keys, ldf_data))
```

The first line creates an object that will be ready to read from our Yahoo data source. The second two lines provide the various data types you want to read. The third line creates a list of dataframe objects which have all the different types of data. The fourth line converts this list into a dictionary and then we can access anytype of data we want easily.

Take a look [here](https://web.archive.org/web/20150323190205/http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) for examples of what you can do with them. A DataFrame's rows correspond to points in time, and its columns usually represent specific stocks or equities. The data in each cell of a DataFrame represents the corresponding item (say closing price) for that stock at that time. You can access the indexes for the rows and the columns as close.index, or close.columns.

The "real" data within a DataFrame can be pulled out and manipulated as a NumPy ndarray. NumPy provides sophisticated indexing and slicing capabilities similar to those that MATLAB allows. For more details on this take a look at [a numpy tutorial](https://web.archive.org/web/20150323190205/http://www.scipy.org/Tentative_NumPy_Tutorial), (skip to the indexing and slicing section). We we leverage NumPy features in this tutorial.

## First Figure

[![](https://web.archive.org/web/20150323190205im_/http://wiki.quantsoftware.org/images/thumb/0/0c/Adjustedclose2.png/300px-Adjustedclose2.png)](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=File:Adjustedclose2.png)

The figure on the right shows the adjusted close data from the file. In this section we look at the code that generated it. First, we create date objects from the date data:

```
na_price = d_data['close'].values
plt.clf()
plt.plot(ldt_timestamps, na_price)
plt.legend(ls_symbols)
plt.ylabel('Adjusted Close')
plt.xlabel('Date')
plt.savefig('adjustedclose.pdf', format='pdf')
```

In the first line we pull out the close prices we cant to plot into a 2D numpy array from a dataframe. In the next line we erase any previous graph.

  
We can then plot the data using plt.plot. Note that the pyplot plot() command is smart enough to plot several lines at once if it is provided a 2D object. pyplot automatically assigns a color to each line, but you can, if you like, assign your own colors. We add a legend with the symbol names and also add labels for the axes. Finally, with plt.savefig the figure is written to a file.

## Normalized Data

[![](https://web.archive.org/web/20150323190205im_/http://wiki.quantsoftware.org/images/thumb/0/03/Normalized2.png/300px-Normalized2.png)](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=File:Normalized2.png)

A problem with the previous figure is that the high share price of GOOG dominates. It is difficult to see what's going on with the other equities. Also, as an investor, you really want to see relative, or normalized price moves. Here's how to normalize the data:

```
na_normalized_price = na_price / na_price[0, :]
```

The line of code above nicely illustrates how effective Python (with NumPy) can be. In that single line of code we executed 2000 divide operations. Each row in pricedat was divided by the first row of pricedat. Thus normalizing the data with respect to the first day's price. The resulting figure is to the right.

Up til now I've shown all of the code. From here forward, I'm only going to show what's important or relevant. So I'm not repeating the code for plotting. You can see it in the source code that referenced at the beginning of this tutorial.

## Daily Returns

[![](https://web.archive.org/web/20150323190205im_/http://wiki.quantsoftware.org/images/thumb/6/69/Rets.png/300px-Rets.png)](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=File:Rets.png)

It is very often useful to look at the returns by day for individual stocks. The general equation for daily return on day t is:

- ret(t) = (price(t)/price(t-1)) -1

We can compute this in Python all at once as using the builtin QSTK function returnize0:

```
na_rets = na_normalized_price.copy()
tsu.returnize0(na_rets)
```

In the figure at right we illustrate the daily returns for SPY and XOM. Observe that they tend to move together but that XOM's moves are more extreme.

  

## Scatter Plots

[![](https://web.archive.org/web/20150323190205im_/http://wiki.quantsoftware.org/images/thumb/a/a8/Scatter2.png/300px-Scatter2.png)](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=File:Scatter2.png)

Scatter plots are a convenient way to assess how similarly two equities move together. In a scatter plot of daily returns the X location of each point represents the return on one day for one stock, and the Y location is the return for another stock. If the cloud of points is arranged roughly in a line we can infer that the equities move together.

[![](https://web.archive.org/web/20150323190205im_/http://wiki.quantsoftware.org/images/thumb/1/14/ScatterSPXvGLD.png/300px-ScatterSPXvGLD.png)](https://web.archive.org/web/20150323190205/http://wiki.quantsoftware.org/index.php?title=File:ScatterSPXvGLD.png)

The figures to the right illustrate the visual difference between two equities that move together (top/blue) and two that are less correlated (bottom/red). What do the shapes of the point clouds tell you about these relationships?

The figure at the top was created with the following line of code:

```
plt.scatter(na_rets[:, 3], na_rets[:, 1], c='blue')
```

  

## Exercise: Cumulative Daily Returns

Using the daily returns we can reconstruct cumulative daily returns. Note that in general the cumulative daily return for day t is defined as follows (this is NOT Python code, it is an equation):

```
daily_cum_ret(t) = daily_cum_ret(t-1) * (1 + daily_ret(t))
```

I don't provide the code for this, as it is a programming assignment. If you plot the result, it should look exactly like the normalized returns plot above.

## Exercise: Line fit to Daily Returns

Finally, we revisit the scatterplots above that reveal visually how closely correlated (related) the daily movement of two stocks are. It's even better if can quantify this correlation by fitting a line to them using linear regression. Note the red line in the figure on the right; this was computed using one of NumPy's linear regression tools. The value of the slope of the line is reported as "corr" which is technically not correct.

Wikipedia has a nice discussion of correlation here: [wikipedia](https://web.archive.org/web/20150323190205/http://en.wikipedia.org/wiki/Correlation_and_dependence)

Again, I'm not going to show the code here, but I will tell you that the code is not very complex, and I used the following functions: polyfit(), polyval(), and sort().