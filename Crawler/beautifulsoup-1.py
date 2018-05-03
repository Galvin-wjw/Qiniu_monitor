from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e: #抛出属性不存在的异常
        return None
    return title

if __name__ == '__main__':
    title  = getTitle("http://jssdk.demo.qiniu.io/")
    if title == None:
        print("title could not be found")
    else:
        print(title)