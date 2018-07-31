import scrapy
import time
from youracclaim.items import YouracclaimItem
from scrapy.selector import Selector
from urllib import request
from bs4 import BeautifulSoup

class IBMBadges_spider(scrapy.Spider):  
    name = "IBMBadges_spider"  
    allowed_domains = ["www.youracclaim.com"]  
    start_urls = [  
        "https://www.youracclaim.com/organizations/ibm/badges/"  
    ]

    positionUrls = ["https://www.youracclaim.com/organizations/ibm/badges"]

    curPage = 1
    curPositionUrlIndex = 0

    #
    headers = {
        'x-devtools-emulate-network-conditions-client-id': "233bee36-f680-45ae-8b7f-d7d736c0d47b",
        'upgrade-insecure-requests': "1",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'dnt': "1",
        'accept-encoding': "gzip, deflate",
        'accept-language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        'cookie': "_ga=GA1.2.1828852866.1527757300; _gid=GA1.2.880362684.1531987545; secured_previously_signed_in_user=NFpEbndjQmFkaXNtMjJycXZieVp6TWNzY0hZTzhDZCtsdkVxclJTZGN1L21zSkdubDNqblgzd1I1MkgwOVNlMy0tNmd5UEVCencvOWM4cGlCazJEemF4UT09--6cde149e16ad5a3d458cc1ef2b5dab800ebcdd5a; time_zone_name=Beijing; _jefferson_session=ekZpSWE2MXl3bS9Wa3hPZjZvR2ZqNklFYWJXNW5DVUVwVG03WlBzT0JOQVAvQVhpZThHL2xCRjV0b3JyR2FUeFNpTjl3ZTAxaks2dy93Vjg5K0xhQUFvT0VHZmU0djRSWUphOW1mSWpnaER2T0lRQTcwNnJzRDdNNVVvcXpJcm1NemRCa1pGa3dJMXpGcE1IVnVrcmF3PT0tLTF3OHVnZUlVbTg0RmhOZnVtay8xakE9PQ%3D%3D--27d991b29a555a94a27dfa80b4cb527001d30046",
        'cache-control': "no-cache"
    }

    def start_requests(self):
        return [self.next_request()]

    def parse(self, response):
    	print("request -> " + response.url)

    	sel = Selector(response)
    	badge_list = sel.xpath('//a[@class="badge-card do-not-underline"]')
        
    	for badge_info in badge_list:
    		item = YouracclaimItem()
    		item["title"] = badge_info.xpath('span/em/text()').extract()[0]
    		item["link"] = "https://www.youracclaim.com" + badge_info.xpath('@href').extract()[0]
    		item["image"] = badge_info.xpath('div/img/@src').extract()[0]
    		#print("title -> " + item["title"])
    		yield item

    	if self.curPage < 2:
    		self.curPage += 1
    		time.sleep(30)
    	yield self.next_request()


    def next_request(self):
        return scrapy.http.FormRequest(
            self.positionUrls[self.curPositionUrlIndex] + ("?page=%d" % (self.curPage)),
            headers=self.headers,
            callback=self.parse
        )
