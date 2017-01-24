from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.loader.processor import TakeFirst
from scrapy.contrib.loader import XPathItemLoader
from scrapy.selector import HtmlXPathSelector
from find_torrent.scraper.items import tor_item
from find_torrent.scraper.parsers import extratorrent_to_torrent

class Fast_Torrent_Loader(XPathItemLoader):
    default_output_processor = TakeFirst()


class Fast_Torrent(CrawlSpider):
    name = "extratorrent_old"
    allowed_domains = ["extratorrent.cc"]
    start_urls = ["http://extratorrent.cc"]

    #http://extratorrent.cc/torrent/5279775/War.Dogs.2016.720p.BRRip.x264.AAC-ETRG.html
    rules = (
        Rule(LinkExtractor(allow=(r'/torrent/.*.html',)), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=(r'/category/.*/*',)), follow=True),
    )

    def parse_item(self, response):
        print('YO', response.url)
        hxs = HtmlXPathSelector(response)
        l = Fast_Torrent_Loader(tor_item(), hxs)

        self.logger.info('Hi, this is an item page! %s', response.url)

        """
        l.add_xpath('title', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table[2]/tbody/tr/td[2]/h1')
        l.add_xpath('description', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/div[4]')
        l.add_xpath('magnet', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/a[2]')
        l.add_xpath('torrent', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/a[1]')
        l.add_xpath('type_category', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[3]/td[2]')
        l.add_xpath('size', '/html/body/table/tbody/tr[3]/td/table/tbody/tr/td[2]/table[3]/tbody/tr/td[1]/table/tbody/tr[7]/td[2]')
        """
        print('============================================================================')
        extratorrent_to_torrent(response.body)

        # return l.load_item()