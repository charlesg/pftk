# Quick start

If you are in a hurry, you can skip to the  [Installation Guide](installation_guide.md).

# About the Python Financial ToolKit

The python financial toolkit (pftk) is a fork from **pftk** which I learned to use taking a course on [Coursera](http://www.coursera.com). Over the years, I enjoyed using the package but it was no longer developped and needed updates. I forked it to implement a few immidiate needs:

* Refresh for compatibility with more Python versions.
* Implementation of new backends, starting with [EOD Historical Data](http://eodhistoricaldata.com). This was becoming important since Yahoo stopped allowing historical data downloads.

Pftk is a Python-based open source software framework designed to support portfolio construction and management.

Pftk was built primarily for finance students, computing students, and quantitative analysts with programming experience.  You should not expect to use it as a desktop app trading platform.  Instead, think of it as a software infrastructure to support a workflow of modeling, testing and trading.  

* Scroll through the [Gallery](gallery.md) to see the sorts of things you can do easily with **pftk**.  
* If you are in a hurry, you can skip to the [Installation Guide](installation_guide.md).

Key components of pftk are:

* **Data**: A data access package that enables fast reading of historical data (`pftkutil.data_access`).
* **Processing tools**: Uses [pandas](http://code.google.com/p/pandas/), a Python package designed for time series evaluation of equity data.
* **Portfolio optimization**: Using the CVXOPT library.
* **Event studies**: An efficient event analyzer, [Event Profiler](event_profiler.md).
* **Simulation**: A simple backtester, [[quicksim]], that includes transaction cost modeling.

## Gallery

Scroll through the [[Gallery]] to see the sorts of things you can do easily with **pftk**.  

## Download, Installation & Open Source License

* pftk is released under the New BSD License. Read the [[license]].
* QSTK was also released under the New BSD License.
* Download and installation instructions are here: [[Installation_Guide]].

## Assumptions & Supported Platforms

Testing was done on done on Mac OS X and Ubuntu Linux on Intel machines. We recommend a 2.0 GHz processor and 2GB of RAM as a minimum. Pftk does run on Windows machines, but we don't guarantee it, and we can't always help you if you run into problems.

We make some assumptions about the you should know about that may limit pftk's use, including:

* **Frequency**: Daily trading (versus intra-day high frequency trading);
* **Equities**: Publicly traded equities for which historical data are available;
* **Calendars**: US market calendars (e.g. NYSE open/close).

Having said that, the tool kit can easily be adapted for other trading regimes.  You might want to scan our to see some examples of what you can do with pftk.

## Documentation

This page is the root page for pftk documentation.  Here are links to information about important modules and APIs:

* Installation and overview information
  * [Installation Guide](installation_guide) for downloads and details on getting up and running.
  * [Connecting With Data Sources](connection_with_data_sources.md)
  * [Newscred Data](newscred_data.md)
  * [Getting Yahoo Data](getting_yahoo_data.md)
  * [Getting Compustat Data.](getting_compustat_data.md)
  * [Work Flow Guide](workflow_guide) that provides an overview of intended use of the software
* Pftk Tutorials
  * [Tutorial 1](tutorial_1.md) Reading data and basic time series operations and plotting
  * [Tutorial 2](tutorial_2.md) Reading CSV data (not **pftk** specific)
  * [Tutorial 3](tutorial_3.md) Tips for accessing historical data via DataAccess + a quick and dirty portfolio back test
  * [Tutorial 4](tutorial_4.md) Creating a an equity allocation DataFrame
  * [Tutorial 5](tutorial_5.md) Using pftksim to back test an allocation strategy (**in development**)
  * [Tutorial 8](tutorial_8.md) Using the CVXOPT library (**in development**)
  * [Tutorial 9](tutorial_9.md) Event Profiler (**in development**)
  * [Tutorial 10](tutorial_10.md) Visualizer (**in development**)
* Other Tutorials
  * [Numpy Tutorial 1]() Working with Numpy arrays (**in development**)
  * [Pandas Tutorial 1]() Working with DataFrames (**in development**)

## Contributing & Coding Conventions

Contact the author about contributions to the code.

Please follow coding conventions described here: [[Coding Standard]]

Use the text 2FIX as a comment indicating a potential bug.  As in:

``` Python
 # 2FIX we may inadvertently divide by zero below
 x = y / u
```

## Contributors

pftk is currently maintained and developped by:

* Charles Gagnon, the New York Genome Center

The original QSToolKit development began to support  CS 8803-FIN: Machine Learning for Trading, a course at Georgia Tech. 

* Prof Tucker Balch, Georgia Tech
* Sourabh Bajaj, Georgia Tech, now Google
* Drew Bratcher, Georgia Tech
* Weiyi Chen, Georgia Tech, now Millennium
* John Cornwell, Georgia Tech
* Prof Maria Hybinette, UGA
* Shreyas Joshi, Georgia Tech, now AQR
* Harikrishna Narayanan, Georgia Tech, now Yahoo! Finance

## Resources, Relevant News & Links

* [Resources](): Additional relevant resources.
* [Tucker Balch's blog](http://augmentedtrader.wordpress.com)
* [WSJ Article](http://online.wsj.com/article/SB10001424052748703834604575365310813948080.html) about AI for trading.

Older documents:
* [Workflow Guide](workflow_guide.md) :: provides a block diagram overview of **pftk** intended use.
