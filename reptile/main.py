#coding=utf-8
import save_database
import qidian

global appid
global appkey
appkey = 'TfRNKWnRUB3gTA2ThMuqpWo0'  # leancloud应用的id和key，用来识别应用
appid = 'N21rGWcBJ3wcqtlR1dalgbV6-gzGzoHsz'

def savebkname():
    '''这个方法将会将爬取到的书籍名称与url地址保存到leancloud'''

    database = save_database.saveInDataBase(appkey, appid)  #创建数据保存对象
    a = save_database.selectData(appkey, appid)  #创建数据查询对象
    url = a.select_classify('Book_classify', 'check', '1', 'url')

    # url = 'http://r.qidian.com/pubnewbook'

    bookname = []
    urls = []
    for i in url:
        # print i
        for j in range(1, 27):  # 27是每个分类下的最大页面，貌似每一个分类下都只有26个页面
            bookname.append(qidian.get_content(i + '?page=' + str(j))[0])  # 这个地方有个错误，把url保存到bookname表里面了
            urls.append(qidian.get_content(i + '?page=' + str(j))[1])  # 这里把bookname保存到url表里面了，数据已经创建，不好改了。先这样吧
    print bookname, urls

    # database.save_data(lists)
    database.save_book(bookname, urls, 'test')  # 保存到数据库

def savebkzj(bookname):
    '''该方法用来将书籍章节内容保存到leancoud'''
    saves = save_database.saveInDataBase(appkey, appid)
    select = save_database.selectData(appkey, appid)
    url = select.select_classify('Book_name', 'url', bookname, 'bookname', 'url')
    print url[0]
    print url[1]
    if 'http' in url[1]:
        urls, book_zj, updateTime, length = qidian.get_book_title(url[1])
        saves.save_title(urls, book_zj, updateTime, length, url[0])
    else:
        urls, book_zj, updateTime, length = qidian.get_book_title(url[0])
        saves.save_title(urls, book_zj, updateTime, length, url[1])


def savebkcontent(book_list):
    saves = save_database.saveInDataBase(appkey, appid)
    select = save_database.selectData(appkey, appid)
    try:
        url, zj = select.select_classify2('Book_title', ['bookname', 'num'], book_list, 'urls', 'book_zj')
        # print url
        if 'http://' in url:
            book_content = qidian.get_book_content(url)
            URL = url
            ZJ = zj
        else:
            book_content = qidian.get_book_content(zj)
            URL = zj
            ZJ = url

        print book_content
    except ValueError:
        savebkzj(book_list[0])
        url, zj = select.select_classify2('Book_title', ['bookname', 'num'], book_list, 'urls', 'book_zj')
        # print url
        if 'http://' in url:
            book_content = qidian.get_book_content(url)
            URL = url
            ZJ = zj
        else:
            book_content = qidian.get_book_content(zj)
            URL = zj
            ZJ = url

        print book_content



if __name__ == '__main__':
    # savebkname()
    bookname = raw_input('输入书名：')
    zj = raw_input('选择章节：')
    book_list = []
    book_list.append(bookname)
    book_list.append(int(zj))
    # print book_list
    savebkcontent(book_list)