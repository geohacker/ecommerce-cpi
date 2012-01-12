#Models for items to be scraped.

from scrapy.item import Item, Field

class FlipkartBook(Item):
    title = Field()
    author= Field()
    price = Field()
