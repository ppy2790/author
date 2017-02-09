#coding=utf-8

from scrapy.spiders import CrawlSpider
from scrapy.http import Request, FormRequest
from scrapy.selector import Selector


import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class AuthorSpider(CrawlSpider):

    name = 'jauthor'

    start_urls=[
        #'http://www.jianshu.com/users/54b5900965ea/timeline' #url要求是以timeline结尾的,而不是直接的作者主页url
        'http://www.jianshu.com/users/5f4159893525/timeline'
    ]




    def parse(self,response):

        selector = Selector(response)

        url = str(response.url)

        pg = 1

        if url.find('?max_id=') >0 :

            pg = int(response.meta['pg'])



        user = url.split('/')[4]


        ids = selector.xpath('//ul[@class="note-list"]/li/@id').extract()

        index = len(ids)

        id = filter(str.isdigit,str(ids[index-1]))


        infos = selector.xpath('//ul[@class="note-list"]/li')

        for info in infos:

            feedtype = info.xpath('div/div[1]/div/span/@data-type').extract()[0]

            ##行为类型 喜欢, 打赏 like_user, like_note 。。。
            ##最后一条 join_jianshu 注册时间
            print feedtype

            dt = info.xpath('div/div[1]/div/span/@data-datetime').extract()[0]
            ## 时间
            print dt


        url = 'http://www.jianshu.com/users/'+user+'/timeline'
        next = url +'?max_id='+str(id) +'&page='+ str(pg+1)

        if len(infos) > 1:

            yield Request(next,callback=self.parse,meta={'pg':str(pg+1)})













