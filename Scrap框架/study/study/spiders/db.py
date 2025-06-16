import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import StudyItem


class DbSpider(scrapy.Spider):
    name = "db"
    allowed_domains = ["book.douban.com"]
    start_urls = ["https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start=20&type=T"]

    def __init__(self):
        super().__init__()
        self.page = 20

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        titles = soup.select(".subject-item .info h2 a")
        contents = soup.select(".subject-item .info p")

        for title, content in zip(titles, contents):
            studyItem = StudyItem()
            mtile = title.text.replace('\n', '').replace(' ', '')
            mcontent = content.text.replace('\n', '').replace(' ', '')
            studyItem['title'] = mtile
            studyItem['content'] = mcontent
            yield studyItem

        if self.page < 100:
            self.page += 20
            next_url = f'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4?start={self.page}&type=T'
            yield response.follow(next_url, callback=self.parse)
