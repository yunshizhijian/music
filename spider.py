# -*- coding:utf-8 -*-
import requests
import re
import json
def get_mp3_by_sid(sid):
    #根据sid,下载MP3
    #根据歌曲id获取歌曲地址并且下载
   # sid = '323025'
    api='http://musicapi.qianqian.com/v1/restserver/ting?method=baidu.ting.song.play&format=jsonp&callback=jQuery17208098337996053833_1513859108469&songid=%s&_=1513859109906' % sid
    #访问api
    response = requests.get(api)
    data =response.text
    data1 = re.findall(r'\((.*)\)',data)[0]
    data2 = json.loads(data1)
    #取得歌曲信息(名字,歌曲,地址)
    mp3_name = data2['songinfo']['title']
    mp3_url =  data2['bitrate']['file_link']
    #发送http请求
    print(mp3_name)
    response = requests.get(mp3_url)
     #持久化 写文件
    filename ='%s.mp3'%mp3_name
    with open(filename,'wb')as f:
       f.write(response.content)
def get_sids_by_name(query):
    #根据查询内容获取sid
    api = 'http://music.baidu.com/search'
    data = {
        'key':query
    }
    response =requests.get(api,params=data)
    html =response.text
    sids = re.findall(r'sid&quot;:(\d+),',html)
    return sids
sids =get_sids_by_name('6')
for sid in sids:
    get_mp3_by_sid(sid)