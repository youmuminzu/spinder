import scrapy
from items import StockstarItem,StockstarItemLoader\

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']
    start_urls = ['http://quote.stockstar.com/stock/ranklist_a_3_1_1.html']

    def parse(self, response):
        page = int (response.url.split("_")[-1].split(".")[0])
        item_nodes = response.css('#datalist tr')
        if page > 10:
            return
        for node in item_nodes:
            item_loader = StockstarItemLoader(item=StockstarItem(),selector=node)
            item_loader.add_css("code", "td:nth-child(1) a::text")
            item_loader.add_css("abbr", "td:nth-child(2) a::text")
            item_loader.add_css("last_trade", "td:nth-child(3)::text")
            item_loader.add_css("chg_ratio", "td:nth-child(4)::text")
            item_loader.add_css("chg_amt", "td:nth-child(5)::text")
            item_loader.add_css("volumn", "td:nth-child(6)::text")
            stock_item = item_loader.load_item()
            yield stock_item
        if item_nodes:
            next_page = page + 1
            next_url = response.url.replace ("{0}.html".format (page) , "{0}.html".format(next_page))
            yield scrapy.Request(url=next_url, callback=self.parse)
        pass
