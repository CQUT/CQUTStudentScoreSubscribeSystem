#coding=gbk
import urllib2
import urllib
import cookielib
import re
import os
import datetime

class LoginCQUTCookie:
    #һЩ����
    loginPageUrl = 'http://i.cqut.edu.cn/zfca/login?service=http%3A%2F%2Fi.cqut.edu.cn%2Fportal.do'
    loginUrl = 'http://i.cqut.edu.cn/zfca/login?service=http%3A%2F%2Fi.cqut.edu.cn%2Fportal.do'
    def __init__(self, username, password):
        self.username = username
        self.password = password
    def login(self):
        saveCookie = cookielib.MozillaCookieJar()#ʹ��Cookie
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(saveCookie))
        #��ʼ��ȡ�����ַ
        rep = opener.open(self.loginPageUrl)
        html = rep.read()
        lt = re.findall(r'lt" value="(.*)"', html)  #��ȡlt��value
        postdata = urllib.urlencode({
                                    'useValidateCode':'0',
                                    'isremenberme':'0',
                                    'ip':'',
                                    'username':self.username,
                                    'password':self.password,
                                    'losetime':'30',
                                    'lt':lt[0],
                                    '_eventId':'submit',
                                    'submit1':''
                                     })
        rep = opener.open(self.loginUrl,postdata)    #ģ���½
        return saveCookie

cookie = LoginCQUTCookie('11303070104','52511515').login()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

rep = opener.open('http://i.cqut.edu.cn/zfca?yhlx=student&login=122579031373493679&url=stuPage.jsp')    #����ѧ��ϵͳ
fc = open('classes.txt')
for cno in fc:
    cno = re.findall('([0-9]+)', cno)[0]
    if len(cno) < 9:
        continue
    os.mkdir('./'+cno)
    print cno+' class is getting... ----- '+datetime.datetime.now().__str__()
    for i in range(1,45):
        sno = cno+"{0:0>2}".format(i)
        rep = opener.open('http://xgxt.i.cqut.edu.cn/xgxt/xsxx_xsgl.do?method=showPhoto&xh='+sno)    #��ȡ��Ƭ
        f = open(cno+'/'+sno+'.jpg','wb')
        f.write(rep.read())
        f.close()
        