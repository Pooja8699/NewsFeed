# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo     # Importing pymongo library to store Result in MongoDB Database
class NewsfeedPipeline(object):

    def __init__(self):
        # This method establishes connection with MongoDB in the mentioned IP and Port
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )
        db= self.conn['MyNewsFeed']          # DataBase Name
        self.collection = db['News_tb']      # Collection Name

    def process_item(self, item, spider):
        self.collection.insert(dict(item))    # Insert as a dictionary in MongoDB
        return item
