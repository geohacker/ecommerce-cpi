# Scrapy settings for flipkart_trends project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'flipkart_trends'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['flipkart_trends.spiders']
NEWSPIDER_MODULE = 'flipkart_trends.spiders'
DEFAULT_ITEM_CLASS = 'flipkart_trends.items.FlipkartTrendsItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['flipkart_trends.pipelines.FlipkartTrendsPipeline']
