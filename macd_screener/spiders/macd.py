import scrapy


class MacdSpider(scrapy.Spider):
    name = 'macd_screener'
    allowed_domain = ['https://stock-screener.org/']
    start_urls = ['https://stock-screener.org/macd-crossover.aspx']

    def parse(self, response):
        stocks = response.xpath("//table[@class='styled']/tbody/tr")
        for stock in stocks:
            symbol = stock.xpath(".//td[1]/text()").get()
            opens = stock.xpath(".//td[3]/text()").get()
            high = stock.xpath(".//td[4]/text()").get()
            low = stock.xpath(".//td[5]/text()").get()
            close = stock.xpath(".//td[6]/text()").get()
            volume = stock.xpath(".//td[7]/text()").get()
            percent = stock.xpath(".//td[8]/font/text()").get()

            yield {
                'Symbol': symbol,
                'Open': opens,
                'High': high,
                'Low': low,
                'Close': close,
                'Volume': volume,
                '%Change': percent
            }
