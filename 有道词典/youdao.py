# -*- coding: utf-8 -*-
'''
@Author: wukong
@Date: 2019-07-09 15:08:16
'''
import requests
from bs4 import BeautifulSoup as bp


def getUrl(url): # 获取网页 返回一个html
    r = requests.get(url)
    return r.text

def parseHtml(html): # 获取一个html 返回得到翻译结果一段div元素
    soup  = bp(html,features="lxml")
    explain = soup.find('div',{'class':"trans-container"})
    return explain

def printExpain(explain): # 将 div元素中翻译结果 按照自己想要的格式 打印出来
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

def query(url): # 将上面3个函数 打包在一起
    html = getUrl(url)
    explain = parseHtml(html)
    printExpain(explain)

def main():
    print("欢迎来到简陋版有道词典")
    print("目前只能查询单词")
    print("当你想要退出时，请输入：q")
    word = None
    while word != 'q'  or word != "Q": # 当输入wei q 或 Q 时 退出 程序  ??突然不能推出程序了？？
        word = input("请输入要查询的单词：")
        if word =="0921":
            # 特殊代码：
            # 用来退出程序
            exit()
        url = 'https://www.youdao.com/w/'
        query(url+word)

if __name__ == "__main__":
    main()