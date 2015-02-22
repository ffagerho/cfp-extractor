import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

from cfp.items import CfpItem

class WikiCfpSpider(CrawlSpider):
    name = "wikicfp"
    allowed_domains = ["wikicfp.com"]
    start_urls = ["http://www.wikicfp.com/cfp/call?conference=software%20engineering"]
    rules = (
        Rule(LinkExtractor(allow=["/cfp/call\?conference=software%20engineering&page=\d+"])),
        Rule(LinkExtractor(allow=["/cfp/servlet/event.showcfp\?eventid=\d+&copyownerid=\d+"]), callback="parse_cfp"),
    )

    def parse_cfp(self, response):
        print "HERE:", response
        item = CfpItem()
        item["url"] = response.url
        item["name"] = response.xpath("(//span[@typeof='v:Event'])[1]/span[@property='v:summary']/@content").extract()
        item["long_name"] = response.xpath("(//span[@typeof='v:Event'])[1]/span[@property='v:description']/text()").extract()
        item["when"] = response.xpath("(//span[@typeof='v:Event'])[1]/span[@property='v:startDate']/@content").extract()
        item["where"] = response.xpath("(//span[@typeof='v:Event'])[1]/span[@rel='v:location']/span[@typeof='v:Address']/span[@property='v:locality']/@content").extract()
        item["submission_deadline"] = response.xpath("//span[span[@content='Submission Deadline']]/span[@property='v:startDate']/@content").extract()
        item["notification_due"] = response.xpath("//span[span[@content='Notification Due']]/span[@property='v:startDate']/@content").extract()
        item["final_version_due"] = response.xpath("//span[span[@content='Final Version Due']]/span[@property='v:startDate']/@content").extract()
        item["text"] = response.xpath("//td[@align='center']/div[@class='cfp']").extract()
        return item
