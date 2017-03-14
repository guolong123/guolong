#coding=utf-8
import urllib2_test
import re
url = 'http://r.qidian.com/'
# //book.qidian.com/info/1002487970


def get_bangdan(url):
    '''
    此方法接收主分类下的url地址，如：http://r.qidian.com/
    返回爬取到的分类名称和地址
    '''
    urls = []
    titles = []
    all_data = urllib2_test.getHtml(url)
    # print all_data
    print '###################################################\
    #########################################################\n\n\n\n\n'
    classes_cont = '<li class=""><a href="//(.*?)?style=1" data-eid="(.*?)">(.*?)</a><cite></cite></li>'
    pattent = re.compile(classes_cont, re.M).findall(all_data)
    # print pattent
    for i in pattent:
        titles.append(i[2])
        urls.append('http://'+i[0][:-1])
        # print i[1]
    return titles, urls


def get_content(url):
    '''此方法接收分类url地址，如：http://wuxia.qidian.com/
        返回爬取到的分类下的书名以及对应的url地址
    '''
    book_name = []
    urls = []
    all_data = urllib2_test.getHtml(url)
    # print all_data
    comp = '<h4><a href="//book.qidian.com/info/(.*?)" target="_blank" data-eid="qd_C40" data-bid="(.*?)">(.*?)</a></h4>'
    # content2 = re.compile(comp2, re.S).findall(all_data)
    # print content2
    content = re.compile(comp, re.S).findall(all_data)
    for i in content:
        # print i[0]
        urls.append('http://book.qidian.com/info/'+str(i[0]))
        book_name.append(i[2])
    return urls, book_name


def get_book_title(url):
    '''
    此方法接收书籍url地址，如：http://book.qidian.com/info/3690849
    返回该书下所有章节的url地址，章节名称，更新时间以及长度
    :param url:
    :return:
    '''
    book_zj = []
    urls = []
    updateTime = []
    length = []
    all_data = urllib2_test.getHtml(url+'#Catalog')
    # print all_data
    comp = '<li data-rid="(\d*?)"><a href="//(.*?)" target="_blank" data-eid="(.*?)" data-cid="//(.*?)" title="首发时间：(.*?) 章节字数：(\d*?)">(.*?)</a>'
    content = re.compile(comp, re.S).findall(all_data)
    for i in content:
        urls.append('http://'+i[1])
        book_zj.append(i[6])
        updateTime.append(i[4])
        length.append(i[5])
    return urls, book_zj, updateTime, length


def get_book_content(url):
    '''此方法获取某一章节url，返回书籍内容'''
    book_content = ''
    all_data = urllib2_test.getHtml(url)
    # print all_data
    comp = '<div class="read-content j_readContent">(.*?)</div>'
    content = re.compile(comp, re.S).findall(all_data)
    for i in content:
        book_content = (i.replace('<p>', '\n'))
    return book_content

if __name__ == "__main__":
    bangdan = get_bangdan(url)
    # print bangdan[1][0]
    a = get_content(bangdan[1][0])
    b = get_book_title(a[0][0])
    print b[1][0]
    print get_book_content(b[0][0])