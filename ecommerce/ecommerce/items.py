#Models for items to be scraped.

from scrapy.item import Item, Field

class Book(Item):
    title = Field()
    author= Field()
    price = Field()
