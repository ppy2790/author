#coding=utf-8
import requests
from lxml import etree

### 这个代码是单独的,可以直接运行

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}


def get_info(url,page):

    uid   = url.split('/')
    uid   = uid[4]

    if url.find('page='):
        page = page+1

    html = requests.get(url,headers=headers).content

    selector = etree.HTML(html)

    infos2 = selector.xpath('//ul[@class="note-list"]/li/@id')


    infos = selector.xpath('//ul[@class="note-list"]/li')


    for info in infos:

        name = info.xpath('div/div/div/a/text()')[0]
        dd = info.xpath('div/div/div/span/@data-datetime')[0]
        type = info.xpath('div/div/div/span/@data-type')[0]
        print type
        print dd


    if len(infos) > 1:
        tid = infos2[len(infos2) - 1]
        tid = int(filter(str.isdigit, tid)) - 1
        print tid

        next_url = 'http://www.jianshu.com/users/%s/timeline?max_id=%s&page=%s' % (uid, tid, page)

        print next_url
        get_info(next_url,page)



get_info('http://www.jianshu.com/users/54b5900965ea/timeline',1)

