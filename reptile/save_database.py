#coding=utf-8
import leancloud
import logging
# logging.basicConfig(level=logging.DEBUG)


class saveInDataBase:
    '''该类下的方法用来保存数据到leancloud'''
    def __init__(self, AppKey, AppId):
        leancloud.init(AppId, AppKey)

    def save_data(self, list):
        '''保存数据到Book_classify表'''
        Todo = leancloud.Object.extend('Book_classify')
        j = 0
        for i in list[0]:
            while j < len(list[1]):
                todo = Todo()
                todo.set('url', list[1][j])
                todo.set('title', i)
                j += 1
                break
            todo.save()

    def save_book(self, bkn, urls, types):
        '''保存数据到Book_name表，bkn与urls是一个二维数组'''
        Todo = leancloud.Object.extend('Book_name')
        i = 0
        while i < len(bkn):
            j = 0
            while j < len(bkn[i]):
                todo = Todo()
                todo.set('bookname', bkn[i][j])
                todo.set('url', urls[i][j])
                todo.set('type', types)
                j += 1
                todo.save()
            i += 1

    def save_title(self, urls, book_zj, updateTime, length, bookname):
        Todo = leancloud.Object.extend('Book_title')
        i = 0
        while i < len(urls):
            todo = Todo()
            todo.set('urls', urls[i])
            todo.set('book_zj', book_zj[i])
            todo.set('updateTime', updateTime[i])
            todo.set('length', length[i])
            todo.set('bookname', bookname)
            todo.set('num', i+1)
            i += 1
            todo.save()

    def save_content(self, bkn, URL, zj, content):
        Todo = leancloud.Object.extend('Content')
        todo = Todo()
        todo.set('bkname', bkn)
        todo.set('url', URL)
        todo.set('zj', zj)
        todo.set('content', content)
        todo.save()






class selectData:
    '''该方法用来查询，理论上通用查询'''
    def __init__(self, AppKey, AppId):
        leancloud.init(AppId, AppKey)

    def select_classify(self, clasy, titles, values, *kwr):
        '''clasy是表名，title是列名，values是列所对应的值，kwr是所需返回查询的列'''
        result = []
        # print lists
        Todo = leancloud.Object.extend(clasy)  # 创建查询实例
        query = Todo.query  # 通过采用Todo的query属性来获得query对象
        query.equal_to(titles, values)
        query_list = query.find()
        for i in query_list:
            for j in kwr:
                result.append(i.get(j))
        result = list(set(result))  # 去重操作

        return result

    def select_classify2(self, clasy, titles, values, *kwr):
        '''clasy是表名，title是列名，values是列所对应的值，kwr是所需返回查询的列'''
        result = []
        # print lists
        Todo = leancloud.Object.extend(clasy)  # 创建查询实例
        query1 = Todo.query  # 通过采用Todo的query属性来获得query对象
        query2 = Todo.query
        query1.equal_to(titles[0], values[0])
        query2.equal_to(titles[1], values[1])
        query = leancloud.Query.and_(query1, query2)
        query_list = query.find()
        j = 0
        for i in query_list:
            while j < len(kwr):
                result.append(i.get(kwr[j]))
                j += 1
        result = list(set(result))  # 去重操作
        print result

        return result
