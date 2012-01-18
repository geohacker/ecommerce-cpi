from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from scrapy.http import Request
from ecommerce import Session
from ecommerce.models import Base, Books, Meta
from sqlalchemy.sql.expression import desc
import urllib
from ecommerce.items import Book

class InfibeamSpider(BaseSpider):
  name = "InfibeamSpider"
  allowed_domains = ["http://infibeam.com","www.infibeam.com"]

  def __init__(self):
    self.session = Session()
  
  def start_requests(self):
    round_info = self.session.query(Meta).order_by(desc(Meta.round)).first()
    for row in self.session.query(Books).filter(Books.round==round_info.round):
      # log.msg("Looking for "+row.title,level=log.DEBUG)
      ebayurl="http://www.ebay.in/sch/i.html?_from=R40&_npmv=3&_trksid=m570&_nkw=Anupam Kher&_sacat=267"
      url = "http://www.infibeam.com/search?q="+row.title+" ,"+row.author
      yield Request(url,callback=self.parse_lookup, encoding='utf-8')
  
  def parse_lookup(self,response):
    hxs =  HtmlXPathSelector(response)
#    log.msg("here",level=log.DEBUG)
    result_title = hxs.select('//div[@id="bd"]/div[@id="yui-main"]/div[@class="yui-b"]/div[@class="yui-g"]/div[@id="search_result"]/ul[@class="search_result"]/li/span[@class="title"]/h2[@class="simple"]/a/text()').extract()[0]
    result_price = hxs.select('//div[@id="bd"]/div[@id="yui-main"]/div[@class="yui-b"]/div[@class="yui-g"]/div[@id="search_result"]/ul[@class="search_result"]/li/div[@class="price"]/b/text()').extract()[0]
    item = Book()
    item['title']=result_title
    item['author']="None"
    item['price']= result_price
    return item


