# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-07-09 15:08:16
'''
import requests
from bs4 import BeautifulSoup as bp


def getUrl(url):
    r = requests.get(url)
    return r.text

def parseHtml(html):
    soup  = bp(html,features="lxml")
    explain = soup.find('div',{'class':"trans-container"})
    return explain

def printExpain(explain):
    try:
        for i in explain.ul:
            if i != '\n':
                print(i.getText())
    except Exception as e:
        print(e)
        print("请检查输入的单词是否正确！！！")
    else:
        print("查询完毕")
    finally:
        print()

def query(url):
    html = getUrl(url)
    explain = parseHtml(html)
    printExpain(explain)

def main():
    print("欢迎来到简陋版有道词典")
    print("目前只能查询单词")
    print("当你想要退出时，请输入：q")
    word = None
    while word != 'q'  or word != "Q":
        word = input("请输入要查询的单词：")
        url = 'https://www.youdao.com/w/'
        query(url+word)

if __name__ == "__main__":
    main()