from scrapy.spider import BaseSpider
from ecommerce.items import Book
from scrapy.selector import HtmlXPathSelector

class FlipkartSpider(BaseSpider):
  name = "FlipkartSpider"
  allowed_domains = ["http://flipkart.com","www.flipkart.com"]
  start_urls = [
      'http://www.flipkart.com/view-books/0/new-releases'
      ]
  def parse(self, response):
    #filename = response.url.split("/")[-2]
    #open(filename, 'wb').write(response.body)
    hxs = HtmlXPathSelector(response)
    #hxs.select('//div[@class="line bmargin10"]/h2[@class="fk-srch-item-title fksd-bodytext"]/a/text()').extract()
    sites = hxs.select('//div[@class="fk-srch-item fk-inf-scroll-item"]')
    #sites = hxs.select('//div[@class="lastUnit"]/div[@id="search_results"]')
    items=[]
    print sites.__len__()
    for site in sites:
      #print site
      item = Book()
      item['title']= site.select('div[@class="line fksd-bodytext "]/div[@class="line bmargin10"]/h2[@class="fk-srch-item-title fksd-bodytext"]/a/text()').extract()
      item['author'] = site.select('div[@class="line fksd-bodytext "]/div[@class="line bmargin10"]/span[@class="fk-item-authorinfo-text fksd-smalltext"]/a/text()').extract()
      item['price'] = site.select('div[@class="line fksd-bodytext "]/div[@class="unit fk-sitem-info-section"]/div[@class="line fk-itemdetail-info fksd-bodytext"]/div[@class="line dlvry-det"]/div[@class="line fk-srch-pricing fksd-smalltext"]/b[@class="fksd-bodytext price final-price"]/text()').extract()
      items.append(item)
      #print item
    return items


