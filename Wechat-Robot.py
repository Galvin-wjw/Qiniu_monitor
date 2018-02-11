import itchat
import requests
import json
from itchat.content import *

itchat.auto_login(enableCmdQR=2,hotReload = True)

#itchat.send('Hello, filehelper', toUserName='filehelper') #发送给File Transfer
'''
回复发给自己的文本消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    return msg.text
'''
# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
    appkey = "296890405d324da3a89c89d56401d7f3"
    url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
    req = requests.get(url)
    content = req.text
    data = json.loads(content)
    answer = data['text']
    return answer

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def simple_reply(msg):
    #return 'I received: %s' % msg.text
    itchat.send('%s' % tuling(msg['Text']), msg['FromUserName'])


itchat.run(True)
