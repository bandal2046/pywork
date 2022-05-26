import requests
import re,time
import pymongo
from bs4 import BeautifulSoup as bf
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pathlib import Path

def get_books_by_url():
    '''
    获取最新电影
    :return:Title and UrlStr
    '''
    url = "https://www.ygdy8.com/html/gndy/dyzz/index.html"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
    r = requests.get(url, headers=headers)
    #print(r.encoding)
    #decode转码报错,使用errors="ignore"忽略部分转码错误
    htmlY = r.content.decode(encoding="gb18030",errors="ignore")
    #print(type(htmlY))
    soup = bf(htmlY, 'lxml')

    date = []#Movie详情
    for ul in soup.select('.ulink'):
        titleY = ul.get_text()#标题
        pattern = re.compile('《(.*?)》', re.S)
        title = re.findall(pattern,titleY)
        #print(title[0])

        urlstr = ul['href']
        date.append({'Title':title[0],'UrlStr':urlstr})
    return date

def get_page(a):
    '''
    从豆瓣列表页检索电影评分值
    :return:

    option = ChromeOptions()
    option.add_argument("--headless")  # 指定无头模式
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_argument("--window-size=1600,900")
    option.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=option)
    '''
    browser = webdriver.Chrome()
    movie = []
    for i in range(len(a)):
        browser.get('https://search.douban.com/movie/subject_search?search_text='+a[i]['Title'])
        Page = bf(browser.page_source, 'lxml')
        #print(Page)

        #获取分数
        score = []
        for ul in Page.select('.rating_nums'):
            score.append(ul.get_text())
        #print(score)
        if score:
            #print(score[0])#获取列表第一行分数
            if int(float(score[0])) >= 7:
                movie.append({'name':a[i]['Title'],
                              'Score':score[0],
                              'Url':a[i]['UrlStr']})
        else:
            print('未搜索到电影:'+a[i]['Title'])
        Page.clear()
        score.clear()
    if movie:
        print('本次豆瓣查询高于等于七分的共计:%s部'%(len(movie)))
    else:
        print('未检索到任何电影信息！')
    time.sleep(2)
    browser.close()
    return  movie

def save_M(m):
    '''
    获取到评分后保存至数据库中
    :return:
    '''
    Number = []
    for i in range(len(m)):
        b = 'Movie'+str(i+1)
        Number.append(b)
    #print(len(name))
    d = dict(zip(Number,m))

    client = pymongo.MongoClient()
    db = client['Movie']

    collist = db.list_collection_names()
    # collist = mydb.collection_names()
    if "data" in collist:  # 判断 data 集合是否存在
        details = db["data"]
        details.drop()
        print("集合已存在！删除后重新创建插入数据！")
        #保存插入至数据库
        details.insert_one(d)
    else:
        print("集合不存在，插入数据！")
        details = db["data"]
        #保存插入至数据库
        details.insert_one(d)

def downloadUrl():
    '''
    1、从数据库中获取电影在目标页面中获取磁力链接
    2、写入保存至text文本
    :return:
    '''
    browser = webdriver.Chrome()
    client = pymongo.MongoClient()
    db = client['Movie']
    details = db["data"]
    #x = details.find({},{'_id':0})
    #print(type(x))
    for x in details.find({},{'_id':0}):
        #print(x.items())从数据库中查询出字典形式的数据
        for key,value in x.items():
            #print(value['name'])#循环读取自动中的值
            browser.get('https://www.ygdy8.com' + value['Url'])
            Page = bf(browser.page_source, 'lxml')
            #print(Page.find('div',id='Zoom').span.a['href'])
            #获取到下载磁力链接
            MagnetUrl = Page.find('div',id='Zoom').span.a['href']
            a = value['name'].replace('/', '&')#处理正斜杆导致路径错误的问题
            #拼接Text文件名称
            name = '《%s》'%(a)+'_'+value['Score']
            #调用创建写入文件函数
            save_file(name,MagnetUrl)
            Page.clear()
    browser.close()
def save_file(FileName,Url):
    '''
    保存文件操作
    :param FileName:
    :param Url:
    :return:
    '''
    # 打开一个文件
    #Url = "magnet:?xt=urn:btih:da48d0341b1a9a1cbad77a069c7a4ece61ac2a83&dn=%e9%98%b3%e5%85%89%e7%94%b5%e5%bd%b1www.ygdy8.com.%e5%90%89%e7%a5%a5%e5%a6%82%e6%84%8f.HD.1080p.%e5%9b%bd%e8%af%ad%e4%b8%ad%e8%8b%b1%e5%8f%8c%e5%ad%97.mkv&tr=udp%3a%2f%2ftracker.opentrackr.org%3a1337%2fannounce&tr=udp%3a%2f%2fexplodie.org%3a6969%2fannounce&tr=udp%3a%2f%2fexodus.desync.com%3a6969%2fannounce"
    #name = '人潮汹涌'+'_'+'7.0'
    my_file = Path("C:/Users/Administrator/Desktop/Movie/%s.txt"%(FileName))
    if my_file.is_file():
        print("指定的文件已存在！")
    else:
        with open("C:/Users/banda/Desktop/Movie/%s.txt"%(FileName), "w") as fo:
            fo.write(Url)
        #print("是否已关闭 : ", fo.closed)
        print("已创建文件：%s"%(FileName))

name = get_books_by_url()
c = get_page(name)
save_M(c)
downloadUrl()
###save_file()