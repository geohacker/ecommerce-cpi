# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
#from scrapy.http import Request
from flipkart_trends.spiders.books import FlipkartBooksSpider
from flipkart_trends.spiders.infibeam import InfibeamSpider
from scrapy.exceptions import DropItem
import csv, items
from scrapy import log
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flipkart_trends.models import Base, Books
from datetime import datetime

class FlipkartTrendsPipeline(object):

  def __init__(self):
    self.newcsv=csv.writer(open("books.csv","w"))
    self.engine = create_engine('mysql://root:thecryptex@localhost/ecommerce')
    self.Session = sessionmaker(bind=self.engine)
    self.dt = datetime
    Base.metadata.create_all(self.engine)
    self.session = self.Session()

  def process_item(self, item, spider):
    log.msg(item['title'], level=log.DEBUG)
    self.newcsv.writerow([item['author'][0],item['title'][0],item['price'][0]])
    book = Books(2,item['title'][0],item['author'][0],flipkart=item['price'][0].split(' ')[2])
    self.session.add(book)
    self.session.commit()
    
    return item


    #if item["author"]== unicode("Anupam Kher"):
     # print item
    #else:
     # raise DropItem("invalid author")
      
