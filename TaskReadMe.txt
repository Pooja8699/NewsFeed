Tool Used -- Pychram IDE
Framework -- Scrapy (Version- 1.8.0)
HTTP API Server - scrapyrt
DataBase -- MongoDB

1. What is Scrapy?

Scrapy is a free and open-source web-crawling framework written in Python.
Scrapy Project architecture is built around "spiders" which are self-contained crawlers that are given a set of instructions.


Command to create a scrapy project: 

scrapy startproject NewsFeed 

2. Directory Structure -- 

NewsFeed/
    scrapy.cfg            # deploy configuration file

    NewsFeed/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py
			
			news_scrapper.py   # Contains code for crawling web pages.
			
	urls.text              # Contains URLs to scrape


3. Fuctionality of Items.py -->

The main goal in scraping is to extract structured data from unstructured sources, typically, web pages. Scrapy spiders can return the extracted data as Python dicts. 
While convenient and familiar, Python dicts lack structure: it is easy to make a typo in a field name or return inconsistent data, especially in a larger project with many spiders.
To define common output data format Scrapy provides the Item class. Item objects are simple containers used to collect the scraped data. 
They provide a dictionary-like API with a convenient syntax for declaring their available fields.

	
4. Functionality of Pipeline.py

After an item has been scraped by a spider, it is sent to the Item Pipeline which processes it through several components that are executed sequentially.
Each item pipeline component (sometimes referred as just “Item Pipeline”) is a Python class that implements a simple method. 
They receive an item and perform an action over it.

Typical uses of item pipelines are:

cleansing HTML data
validating scraped data (checking that the items contain certain fields)
checking for duplicates (and dropping them)
storing the scraped item in a database


5. Functionality of settings.py -->

The project settings module is the standard configuration file for your Scrapy project, it’s where most of your custom settings will be populated. 
For a standard Scrapy project, this means you’ll be adding or changing the settings in the settings.py file created for your project.


6. To Run a spider --> cd NewsFeed

scrapy crawl spiderName --> e.g - scrapy crawl newsScrape

7. To store output in JSON File. 

scrapy crawl newsScrape -o items.json 

8. DataBase Used - MongoDB

Written items to MongoDB using pymongo. MongoDB address and database name are specified in Scrapy pipelines.py; MongoDB collection is named after item class.

9. Scrapyrt HTTP API

Scrapyrt supports endpoint /crawl.json that can be requested with two methods.
Default Port - 9080

To run newsScrape spider -->
curl "http://localhost:9080/crawl.json?spider_name=newsScrape&start_requests=True"

It creates a log file with current Date. 

10. MongoDB -   Settings in pipelines.py
    port 27017 
	DataBase Name - MyNewsFeed
	Collection Name - News_tb
    


References  --  

https://github.com/scrapinghub/scrapyrt/blob/master/docs/source/api.rst
https://www.youtube.com/watch?v=ve_0h4Y8nuI&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t











