from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy import log
from scrapy.http import Request

class InfibeamSpider(BaseSpider):
  name = "InfibeamSpider"
  allowed_domains = ["http://infibeam.com","www.infibeam.com"]
  
  def start_requests(self):
    lookup = Request("http://infibeam.com/search?q=Anupam Kher,The Best Thing About You Is You!",
        callback=self.parse_lookup)
    return [lookup]

  def parse_lookup(self,response):
    hxs =  HtmlXPathSelector(response)
    log.msg("here",level=log.DEBUG)
    sites = hxs.select('//body')
    return sites


