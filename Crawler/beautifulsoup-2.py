from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

namelist = bsObj.findAll("span",{"class":"green"})
for name in namelist:
    # print(name)
    # get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回 一个只包含文字的字符串
    print(name.get_text())

# text用标签的文本内容去匹配，而不是用标签的属性
sumlist = bsObj.findAll(text = "the prince")
print(len(namelist))

# keywords
alltext = bsObj.findAll(id = "text")  # bsObj.findAll("", {"id":"text"})
print(alltext[0].get_text())
