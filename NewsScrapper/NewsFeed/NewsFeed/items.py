# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


# Extracted data --> Temporary containers (items) --> Storing in Database
import scrapy

class NewsfeedItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    story = scrapy.Field()
    category = scrapy.Field()
    story_time = scrapy.Field()
    story_date = scrapy.Field()
    author = scrapy.Field()
    pass
