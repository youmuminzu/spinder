import scrapy
class DFileSpider(scrapy.Spider):
    name = "dfilespider"
    allowed_domains =["qq.com"]
    start_urls = ['https://new.qq.com/ch/photo/']
    def parse(self, response, **kwargs):
      li_list = response.xpath('//div[@id="List"]/ul/li')
      for li in li_list:
          pic_hrefs = li.xpath('//a[@class="cf pics"]/img@src').extract()
          pic_urls = list(map(lambda url: response.urljoin(url),pic_hrefs))