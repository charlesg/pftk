If you are in a hurry, you can skip to the  [[QSToolKit_Installation_Guide]].

[[File:Eventstudy1.png|300px|thumb|right|How stocks perform after a market event.]]

## Georgia Tech Course

[[http://wiki.quantsoftware.org/index.php?title=ML4Trading CS 7646]]

# About the Python Financial ToolKit

The python financial toolkit (pftk) is a fork from QSTK which I learned to use taking a course on [[Coursera][http://www.coursera.com]. Over the years, I enjoyed using the package but it was no longer developped and needed updates. I forked it to implement a few immidiate needs:
* Refresh for compatibility with more Python versions.
* Implementation of new backends, starting with [[EODHistoricalData][http://eodhistoricaldata.com]]. This was becoming important since YAhoo stopped allowing historical data downloads.

Pftk is a Python-based open source software framework designed to support portfolio construction and management.

QSTK was built primarily for finance students, computing students, and quantitative analysts with programming experience.  You should not expect to use it as a desktop app trading platform.  Instead, think of it as a software infrastructure to support a workflow of modeling, testing and trading.  

* Scroll through the [[Gallery]] to see the sorts of things you can do easily with QSTK.  
* If you are in a hurry, you can skip to the  [[QSToolKit_Installation_Guide]].

Key components of pftk are:

* '''Data:''' A data access package that enables fast reading of historical data ([[qstkutil.DataAccess]]).
* '''Processing tools:''' Uses [http://code.google.com/p/pandas/ pandas], a Python package designed for time series evaluation of equity data.
* '''Portfolio optimization:''' Using the CVXOPT library.
* '''Event studies:''' An efficient event analyzer, [[Event_Profiler]].
* '''Simulation:''' A simple backtester, [[quicksim]], that includes transaction cost modeling.
<BR clear=right>

## Gallery

Scroll through the [[Gallery]] to see the sorts of things you can do easily with QSTK.  

## Download, Installation & Open Source License==

* pftk is released under the New BSD License. Read the [[license]].
* QSTK is released under the New BSD License.
* Download and installation instructions are here: [[Installation_Guide]].

## Assumptions & Supported Platforms==

Testing was done on done on Mac OS X and Ubuntu Linux on Intel machines. We recommend a 2.0 GHz processor and 2GB of RAM as a minimum. Pftk does run on Windows machines, but we don't guarantee it, and we can't always help you if you run into problems.

We make some assumptions about the you should know about that may limit pftk's use, including:

* '''Frequency:''' Daily trading (versus intra-day high frequency trading);
* '''Equities:''' Publicly traded equities for which historical data are available;
* '''Calendars:''' US market calendars (e.g. NYSE open/close).

Having said that, the tool kit can easily be adapted for other trading regimes.  You might want to scan our to see some examples of what you can do with pftk.

## Documentation

This page is the root page for pftk documentation.  Here are links to information about important modules and APIs:

* Installation and overview information
** [[QSToolKit Installation Guide]] for downloads and details on getting up and running.
** [[Connecting With Data Sources]]
** [[Newscred Data]]
** [[Getting Yahoo Data]]
** [[Getting Compustat Data.]]
** [[Work Flow Guide]] that provides an overview of intended use of the software
* QSTK Tutorials
** [[QSTK Tutorial 1]] Reading data and basic time series operations and plotting
** [[QSTK Tutorial 2]] Reading CSV data (not QSTK specific)
** [[QSTK Tutorial 3]] Tips for accessing historical data via DataAccess + a quick and dirty portfolio back test
** [[QSTK Tutorial 4]] Creating a an equity allocation DataFrame
** [[QSTK Tutorial 5]] Using qstksim to back test an allocation strategy
** [[QSTK Tutorial 6]] Reading Compustat data  ('''Not in use anymore''')
** [[QSTK Tutorial 7]] Using the NAG library  ('''Not in use anymore''')
** [[QSTK Tutorial 8]] Using the CVXOPT library
** [[QSTK Tutorial 9]] Event Profiler
** [[QuantViz|QSTK Tutorial 10]] Visualizer
* Other Tutorials
** [[Numpy Tutorial 1]] Working with Numpy arrays
** [[Pandas Tutorial 1]] Working with DataFrames 
<!--
* QSTK major modules
** [http://www.quantsoftware.org/Docs/html/index.html APIs] for all modules
** [[qstklearn]]
** [[qstktest]]
** [[qstkutil]]
** [[Features]]
* QSTK applications
** [[csvconverter]]
** [[data_updater]]
** [[quicksim]]
** [[Event_Profiler]]
** [[QuantViz]]
** [[Report Generator]]
-->
'''Getting help:''' send email to tucker@cc.gatech.edu

## Contributing & Coding Conventions

Contact the author about contributions to the code.

Please follow coding conventions described here: [[Coding Standard]]

Use the text 2FIX as a comment indicating a potential bug.  As in:

 # 2FIX we may inadvertently divide by zero below
 x = y / u

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

* [[Resources]]: Additional relevant resources.
* Tucker Balch's blog [http://augmentedtrader.wordpress.com augmentedtrader.wordpress.com]
* WSJ [http://online.wsj.com/article/SB10001424052748703834604575365310813948080.html?mod=WSJ_hpp_LEFTTopStories article] about AI for trading.

Older documents 
* [Fund Tools]
* [[Work_Flow_Guide]] that provides a block diagram overview of QSTK intended use.
* [[Legacy_Main_Page]]
