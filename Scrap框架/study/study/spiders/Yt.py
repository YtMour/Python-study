import scrapy
import scrapy.core.scheduler

#Twisted作为核心引  asyncio  IO等待时间  单线程的进阶版本
"""
爬虫中间件放在爬虫进入和出去的时候
一开始爬虫运行的时候，我们就可以对爬虫进行操作
process_start_requests对start_urls

processing spider input是在下载中间件返回，还没有给爬虫的时候
process_spider_output在爬虫pase调用结束之后使用

1.爬虫里边拿到start_urls，封装成Request请求对象（没有真的去请求）
2.调度器队列 先进先出 排队
3.挨个处理请求 交给下载中间件  
4.下载中间件去请求Internet  首先process_request 服务器  process_response
5.响应交给爬虫parse css 正则 items对象结合parse存储数据
6.item存储的数据交给管道 存储
"""

class XjbtestSpider(scrapy.Spider):
    name = "xjbtest"
    allowed_domains = ["baidu.com"]
    start_urls = ["https://docs.scrapy.org/en/latest/intro/install.html",
                  'https://docs.scrapy.org/en/latest/']

    def parse(self, response):
        #self.log(response.body)
        pass
