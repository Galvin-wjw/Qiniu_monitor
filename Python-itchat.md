## Python itchat包实现微信机器人回复
#### 语料库采用图灵机器人
#### 主要参考资料：
https://itchat.readthedocs.io/zh/latest/

#### 简单入门
```bash
#给文件传输助手发送一条消息
import itchat
itchat.auto_login()
itchat.send('Hello, filehelper', toUserName='filehelper')
```

#### 循环扫描新信息（心跳）
- 方法名称：start_receiving
- 所需值：无
- 返回值：无

#### 回复信息
- 方法：send（msg='Text Message', toUserName=None）
- msg：消息内容
- '@fil@文件地址'将会被识别为传送文件，'@img@图片地址'将会被识别为传送图片，'@vid@视频地址'将会被识别为小视频（itchat.send('@img@%s' % 'gz.gif')）
- toUserName：发送对象，如果留空将会发送给自己

#### 消息注册方法
- itchat将根据接收到的消息类型寻找对应的已经注册的方法。
- 如果一个消息类型没有对应的注册方法，该消息将会被舍弃。
```bash
import itchat
from itchat.content import *

# 不带具体对象注册，将注册为普通消息的回复方法
@itchat.msg_register(TEXT)
def simple_reply(msg):
    return 'I received: %s' % msg['Text']

# 带对象参数注册，对应消息对象将调用该方法
@itchat.msg_register(TEXT, isFriendChat=True, isGroupChat=True, isMpChat=True)
def text_reply(msg):
    msg.user.send('%s: %s' % (msg.type, msg.text))

```
