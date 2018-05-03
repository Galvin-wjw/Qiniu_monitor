from urllib.request import urlopen
from bs4 import BeautifulSoup
import re, time
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_mail(subject,href):
    content = 'Address:  https://segmentfault.com' + href  # 邮件正文
    tolist = ['137606834@qq.com', 'cuimingzhe@qiniu.com']
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = 'Forum-Monitoring <galvin_wong@163.com>'  # 发件人
    msg['Subject'] = Header('[Segment-Fault:]' + subject, 'utf-8').encode()  # 主题
    # msg['To'] = ' '.join(tolist)  #收件人

    # 输入Email地址和口令:
    from_addr = 'galvin_wong@163.com'
    password = 'ymy870321'
    # 输入收件人地址:
    #to_addr = '137606834@qq.com'
    # 输入SMTP服务器地址:
    smtp_server = 'smtp.163.com'
    smtp_port = 25

    server = smtplib.SMTP(smtp_server, smtp_port) # SMTP协议默认端口是25
    server.starttls()
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, tolist, msg.as_string())
    server.quit()

def get_forum_id():
    html = urlopen("https://segmentfault.com/t/%E4%B8%83%E7%89%9B%E4%BA%91%E5%AD%98%E5%82%A8")
    bsObj = BeautifulSoup(html,'html.parser',from_encoding='utf-8')
    links = bsObj.findAll('h4')
    title = links[0].get_text()
    href = links[0].a['href']
    id = re.search('[0-9]+',href).group()
    return title,id,href
# for link in links:
#     href = link.a['href']
#     #print(href)
#     #id = re.findall(r'[0-9]+',href)
#     id = re.search('[0-9]+',href).group()

if __name__ == '__main__':
   # title, id2,href = get_forum_id()
  #  print(title,id2,href)
    id1 = 323232
    while True:
        title,id2,href = get_forum_id()
        #print(id2)
        if(int(id2) > id1):
            get_mail(title,href)
            id1 = id2
        time.sleep(60)

