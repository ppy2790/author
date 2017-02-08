#coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector

from jiannian.items import  ArticleItem
from jiannian.items import AuthorItem

import json




import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class AuthorSpider(CrawlSpider):

    name = 'author'

    start_urls=[
        'http://www.jianshu.com/users/54b5900965ea/timeline'
        #'http://www.jianshu.com/users/e21d00d18f05/timeline'
        #'http://www.jianshu.com/u/e21d00d18f05'
    ]

    pg = 1

    def parse(self,response):
        selector = Selector(response)

        ids = selector.xpath('//ul[@class="note-list"]/li/@id').extract()

        index = len(ids)

        id = filter(str.isdigit,str(ids[index-1]))


        infos = selector.xpath('//ul[@class="note-list"]/li')

        for info in infos:

            feedtype = info.xpath('div/div[1]/div/span/@data-type').extract()[0]

            print feedtype

            dt = info.xpath('div/div[1]/div/span/@data-datetime').extract()[0]
            print dt

        self.pg = self.pg+1

        url = 'http://www.jianshu.com/users/54b5900965ea/timeline'
        next = url +'?max_id='+str(id) +'&page='+ str(self.pg)

        if len(infos) > 1:

            yield Request(next,callback=self.parse)



    def parse_0(self,response):

        item = AuthorItem()

        selector = Selector(response)

        infos = selector.xpath("//div[@class='meta-block']/p/text()").extract()

        focus_num= int(str(infos[0]))
        fan_num= int(str(infos[1]))
        article_num = int(str(infos[2]))
        word_num = int(str(infos[3]))
        like_num = int(str(infos[4]))

        item['author_url']= response.url

        item['focus_num']= focus_num
        item['fan_num'] = fan_num
        item['article_num'] = article_num
        item['word_num'] = word_num
        item['like_num'] = like_num

        name = selector.xpath('//div[@class="title"]/a/text()').extract()[0]

        item['author_name']=name


        yield item














