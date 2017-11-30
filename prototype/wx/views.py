# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from django.views.decorators.csrf import csrf_exempt
import xml.etree.ElementTree as ET
from django.utils.encoding import smart_str
import hashlib

# Create your views here.

@csrf_exempt
#@ensure_csrf_cookie
def index(request):
    if request.method == 'GET':
        signature = request.GET.get('signature', None)
        timestamp = request.GET.get('timestamp', None)
        nonce = request.GET.get('nonce', None)
        echostr = request.GET.get('echostr', None)

        token = 'Dinghaoyong_wx_233'
        
        if timestamp == None or nonce == None:
            hashstr = ""
        else:
           
            hashlist = [token, timestamp, nonce]
            hashlist.sort()
            hashstr = ''.join([s for s in hashlist])
            
            hashstr = hashlib.sha1(hashstr.encode(encoding='utf-8')).hexdigest()
            
        if hashstr == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("This is not a valid wx request!")
    elif request.method == 'POST':
        data = smart_str(request.body)
        print data

        xml = ET.fromstring(data)

        fromUser = xml.find('ToUserName').text
        toUser = xml.find('FromUserName').text
        msgType = xml.find('MsgType').text

        if msgType == 'text':
            content = u"您好,欢迎来到顶好用!功能正在开发中!"
            replyMsg = TextMsg(toUser, fromUser, content)
            print replyMsg
            return HttpResponse(replyMsg.send())

class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text
        self.MsgId = xmlData.find('MsgId').text

import time
class TextMsg(Msg):
    def __init__(self, toUserName, fromUserName, content):
        self.__dict = dict()
        self.__dict['ToUserName'] = toUserName
        self.__dict['FromUserName'] = fromUserName
        self.__dict['CreateTime'] = int(time.time())
        self.__dict['Content'] = content
        
    def send(self):
        XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{FromUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml>
        """
        return XmlForm.format(**self.__dict)
