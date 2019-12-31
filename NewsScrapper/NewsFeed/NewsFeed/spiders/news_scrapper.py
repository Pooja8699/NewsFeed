import scrapy
import json
from ..items import NewsfeedItem

class NewsSpider(scrapy.Spider):
    #items = NewsfeedItem()
    # Iterates through urls.txt and fetches each URL to scrape.
    name='newsScrape'   # Name of the Spider
    f= open("urls.txt")
    start_urls =[url.strip() for url in f.readlines()]
    f.close()

    def start_requests(self):
        urls = (
            (self.parse_1, self.start_urls[0]),   # 1st URL mentioned in txt file , calls parse_1 method
            (self.parse_2, self.start_urls[1]),   # 2nd URL mentioned in txt file, calls parse_2 method
            (self.parse_3, self.start_urls[2]),   # 3rd URL mentioned in text file, calls parse_3 method
        )

        for cb,url in urls:
            yield scrapy.Request(url, callback=cb)


    def parse_1(self,response):
        ## ReutersIndia News
        items = NewsfeedItem()
        ## Fetches each item using CSS selector, specific to the mentioned website
        all_PageHeadLines = response.css(".ImageStoryTemplate_image-story-container")

        for news in all_PageHeadLines:
            title = news.css(".FeedItemHeadline_full a::text").extract()
            story = news.css(".FeedItemLede_lede::text").extract()
            category = news.css(".FeedItemMeta_channel::text").extract()
            story_time = news.css(".FeedItemMeta_date-updated::text").extract()

            # Extracted data is stored in containers called as Items to maintain a proper structure of the data in the form of dictionary.
            items['title'] = title
            items['story'] = story
            items['category'] = category
            items['story_time'] = story_time

            yield items


    def parse_2(self,response):
        ##Timesofindia
        items = NewsfeedItem()

        ## Fetches each item using CSS selector
        all_titles =response.css("#c_0201")

        for news in all_titles:
            title = news.css("#c_wdt_list_1 .w_tle:nth-child(1) a::text").extract()
            story_time =news.css("span.strlastupd::text").extract()

            # Extracted data is stored in containers called as Items to maintain a proper structure of the data in the form of dictionary.
            items['title'] = title
            items['story_time'] = story_time
            yield items

    def parse_3(self,response):
        ## InShorts News
        items = NewsfeedItem()

        # Fetches each item using CSS Selectors

        all_newsList = response.xpath("//div[@class='news-card z-depth-1']")   ## xpath selectors select HTML tags specified in the expression.

        for news in all_newsList:
            title = news.css(".news-right-box .clickable span::text").extract()
            author = news.css(".author::text")[0].extract()
            story_date = news.css(".time+ span::text")[0].extract()
            story_time =news.css(".time::text")[0].extract()
            story = news.css(".news-card-content div::text").extract()

            # Extracted data is stored in containers called as Items to maintain a proper structure of the data in the form of dictionary.
            items['title'] = title
            items['author'] = author
            items['story_date'] =story_date
            items['story_time'] =story_time
            items['story'] =story

            yield items