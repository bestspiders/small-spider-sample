#-*- coding:utf-8 -*-
import urllib2
import cookielib
import urllib
import requests
from lxml import etree
import random
import re
import os
import time
#获取cookie并抓取输入的地址信息
def login(base_url):
        filename='p_cookie.txt'
        print'Login....'
        s=s=requests.Session()
        cookie=cookielib.MozillaCookieJar(filename)
        opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
        url=web_date 
        data=urllib.urlencode({
            'source':'pc',
            'password':password,
            'pixiv_id':use_id,
            'return_to':'http://www.pixiv.net/'
            } )#user and pass
        headers={'Accept-Language':'zn-CH,zh;q=0.8','User-Agent':'Mozilla/5.0 (X11;     Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/47.0.2526.73 Chrome/47.0.2526.73 Safari/537.36','Referer':'http://www.pixiv.net/'}
        request=urllib2.Request(url,data,headers)
        try:
            login_pixiv=opener.open(request,timeout=20)
            print 'successful'
            cookie.save(ignore_discard=True,ignore_expires=True)
            daily_pixiv=opener.open(base_url)
            page=daily_pixiv.read()
            daily_pixiv.close()
            html=page
            return html
        except urllib2.HTTPError,e:
            print e.code
            print e.reason
#输出cookie
def Cookie_Login():
    cookie_login=cookielib.MozillaCookieJar()
    cookie_login.load('p_cookie.txt',ignore_discard=True,ignore_expires=True)
    opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie_login))
    return opener
#提取图片包地址
def get_daily(info):
    select_url = etree.HTML(info)
    half_link = select_url.xpath('/html/body//*[@class="ranking-items adjust"]//div[2]/a/@href')
    replace_link = ['http://www.pixiv.net/'+full_link for full_link in half_link]
    links=[]
    for k in range(0,len(replace_link)):
        add_links = re.sub('medium','manga',replace_link[k])
        links.append(add_links)
    return links
#访问图片包地址来源地址提取
def refer(info):
    select_url = etree.HTML(info)
    half_link = select_url.xpath('/html/body//*[@class="ranking-items adjust"]//div[2]/a/@href')
    links = ['http://www.pixiv.net/'+full_link for full_link in half_link]
    return links

#请求保存图片包的地址
def access_url(every_image):
    print every_image
    req = urllib2.Request(every_image)
    req.add_header('Host','www.pixiv.net')
    req.add_header('Referer',come_from)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    response = opener.open(req)
    html = response.read()
    response.close()
    return html

#提取每张图片地址
def analysis_image(last_url):
    select_url = etree.HTML(last_url)
    html_url = select_url.xpath('/html/body//div//img/@data-src')
    return html_url

#提取保存图片包的主题
def subject_image(info):
    select_url = etree.HTML(info)
    half_link = select_url.xpath('/html/body//*[@class="ranking-items adjust"]//section/@data-title')
    return half_link

#打开图片准备写入的地址
def open_image(all_url):
    req = urllib2.Request(all_url)
    req.add_header('Host','i3.pixiv.net')
    req.add_header('Referer',every_image)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    response = opener.open(req)
    html = response.read()
    response.close()
    return html

#写入图片二进制
def save_images(write_info):
    # basename=str(image_num)+'.jpg'
    filename = os.path.join(address+'\\'+str(k)+'\\'+str(j)+'.jpg')
    file=open(filename,"wb")
    file.write(write_info)
    file.close()

def check_image(address):
    filename = os.path.join(address+'\\'+'checkurl.txt')
    file = open(filename)
    content = file.read()
    file.close()
    match = re.compile(all_url)
    match_content = re.findall(match,content)
    return match_content

def write_url(address,all_url):
    filename = os.path.join(address+'\\'+'checkurl.txt')
    file = open(filename,'a')
    file.write('\n'+all_url)
    file.close()

#判断是否为图包的页面
def get_decide(come_from):
    print come_from
    req = urllib2.Request(come_from)
    req.add_header('Host','www.pixiv.net')
    req.add_header('Referer',web_date)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    response = opener.open(req)
    html = response.read()
    response.close()
    return html

#提取是否为图包的地址
def get_link(author_link):
    rules = re.compile('multiple')
    links = re.findall(rules,author_link)
    print links
    return links

#前5名单张格式
def get_imageurl(author_link):
    rules_tree = etree.HTML(author_link)
    rules = rules_tree.xpath('//*[@class="img-container"]//img/@src')
    rule_url = re.findall('http://.*\.pixiv.net/',rules[0])
    rule_half = re.findall('img/.*\_p0',rules[0])
    full_url = rule_url[0]+'img-original/'+rule_half[0]+'.png'
    return full_url

#5名以后的单张格式
def fifth_image(author_link):
    rules_tree = etree.HTML(author_link)
    rules = rules_tree.xpath('//*[@class="img-container"]//img/@src')
    rule_url = re.findall('http://.*\.pixiv.net/',rules[0])
    rule_half = re.findall('img/.*\_p0',rules[0])
    full_url = rule_url[0]+'img-original/'+rule_half[0]+'.jpg'
    return full_url

#主机地址
def host_url(author_link):
    rules_tree = etree.HTML(author_link)
    rules = rules_tree.xpath('//*[@class="img-container"]//img/@src')
    rule_url = re.findall('http://(.*)\.pixiv',rules[0])
    rule_full = rule_url[0]+'.pixiv.net'
    return rule_full

#打开不是图包的图片
def open_link(new_link,host):
    print new_link
    print host
    req = urllib2.Request(new_link)
    req.add_header('Host',host)
    req.add_header('Referer',come_from)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    response = opener.open(req)
    html = response.read()
    response.close()
    return html

#保存不是图包的照片
def save_singlepic(all_info):
    filename = os.path.join(address+'\\'+str(k)+'.jpg')
    print filename
    file=open(filename,"wb")
    file.write(all_info)
    file.close()

#判断状态码
def code_url(new_link,host):
    req = urllib2.Request(new_link)
    req.add_header('Host',host)
    req.add_header('Referer',come_from)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.89 Safari/537.36')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    status = urllib.urlopen(req)
    status_page = status.getcode()
    print status_page
    return status_page

 
if __name__ == '__main__':
    daily_url = 'http://www.pixiv.net/ranking.php?mode=daily'
    start_page = input('Please entry works start order number:')
    end_page = input('Please entry works end order number:')
    address = raw_input('Please entry save address:')
    use_id = raw_input('please entry your name:')
    password = raw_input('please entry your password:')
    web_date = raw_input('please entry you want to grab web:')
    info = login(daily_url)
    opener = Cookie_Login()
    for k in range(start_page-1,end_page+1):
        every_image = get_daily(info)[k]
        come_from = refer(info)[k]
        main_subject = subject_image(info)[k]
        author_link = get_decide(come_from)
        if not get_link(author_link):
            new_link = fifth_image(author_link)
            anothor_link = get_imageurl(author_link)
            host = host_url(author_link)
            try:
                all_info = open_link(new_link,host)
                save_singlepic(all_info)
            except:
                all_info = open_link(anothor_link,host)
                save_singlepic(all_info)
            
        else:
            if not os.path.exists(address+'\\'+str(k)):
                os.mkdir(address+'\\'+str(k))
            last_url = access_url(every_image)
            for j in range(0,len(analysis_image(last_url))):
                all_url = analysis_image(last_url)[j]
                write_url(address,all_url)
                check_image(address)
                if not check_image(address):
                    print 'The image has been extisted.'
                else:
                    print all_url
                    write_info = open_image(all_url)
                    save_images(write_info)
                    print 'successful save'

