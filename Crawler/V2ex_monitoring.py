from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, time
import slackweb

if __name__ == '__main__':

    url_list = [
        "https://www.v2ex.com/go/gts",
        "https://www.v2ex.com/go/cloud",
        "https://www.v2ex.com/go/qna",
        "https://www.v2ex.com/go/cdn",
        "https://www.v2ex.com/go/jobs",
        "https://www.v2ex.com/go/programmer"
    ]

    slack = slackweb.Slack('')

    id_list2 = []
    while True:
        id_list = []
        for index, list in enumerate(url_list):
            html = urlopen(list)
            bsObj = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
            links = bsObj.findAll('span',{"class":"item_title"})
            #print(links)
            #获取文件标题
            title = links[0].get_text()

            print(title)
            is_qiniu = bool(re.search('七牛|7牛',title))
            #print(is_qiniu)

            href = links[0].a['href']

            id = re.search('[0-9]+',href).group()
            id_list.append(int(id))

            #test = bool((id_list[index] > id_list2[index])&is_qiniu)
            target_text = 'https://www.v2ex.com'+href
            try:
                html2 = urlopen(target_text)
                bsObj2 = BeautifulSoup(html2, 'html.parser', from_encoding='utf-8')
                links2 = bsObj2.findAll('div', {"class": "topic_content"})
                content = links2[0].get_text()

            except Exception as e:
                content=''
                print("valueErroe",e)
            finally:

                if (id_list[index] > id_list2[index])&is_qiniu:
                     slack.notify(username='【舆情监控】'+title +'-V2EX',text = target_text + '\n' + content,mrkdwn = True)
                     id_list2[index] = id_list[index]
        time.sleep(170)

