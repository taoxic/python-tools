import scrapy

from crawlerConfluence.items import CrawlerconfluenceItem

class EasemobSpider(scrapy.Spider):
    #the name of the spider
    name = "easemob"
    # 搜索的域名范围
    allowed_domains = ["c1.com"]
    #the url of the first page that we will start scraping
    start_urls = ["https://c1.com/plugins/pagetree/naturalchildren.action?decorator=none&excerpt=false&sort=position&reverse=false"]

    # def start_requests(self):
    #     cookie = ''
    #     cookies = {i.split('=')[0]:i.split('=')[1] for i in cookie.split('; ')}
    #     headers = {'Accept':'text/plain, */*; q=0.01','Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7','Cache-Control':'no-cache','Host':'c1.com'}
    #     yield scrapy.Request(
    #         url = self.start_urls[0],
    #         cookies = cookies,
    #         headers = headers
    #     )

    # 解析的方法，每个初始URL完成下载后将被调用，Response 作为参数传入
    # 1.负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
    # 2.生成需要下一页的URL请求。
    def parse(self, response):
        spans = response.xpath('//span[@class="plugin_pagetree_children_span"]')
        title = spans.extract_first()  

        base_url = "https://c1.com"
        for span in spans: 
            # id = span.xpath('./@id')
            title = span.xpath('./a/text()').get()
            path = span.xpath('./a/@href').get()
            print(base_url + path)
            item = CrawlerconfluenceItem()
            item['title'] = title
            item['url'] = base_url + path
            yield item
            # yield scrapy.Request(base_url + path, callback=self.get_content)
    
    # def get_content(self, response):
    #     print('################ 获取HTML ################')
    #     title = response.xpath('/html/head/title/text()').get()
    #     print(title)
    #     content = response.xpath('//div[@id="main-content"]/*')
    #     print(content.getall())
    #     item = CrawlerconfluenceItem()
    #     item['title'] = title
    #     item['content'] = content.get()
    #     yield item
