# encoding=utf-8
import requests
import smtplib
import re
from email.mime.text import MIMEText
   
date = {
    'inChina': "是",
    'addressProvince': "安徽省",
    'addressCity': "合肥市",
    'temperatureStatus': "正常",
    'temperature': 0,
    'isIll': "否",
    'closeHb': "否",
    'closeIll': "否",
    'healthDetail': "无异常",
    'isIsolation': "否",
    'isolationPlace': "无",
    'userId': "415700210020",  # 填入你的学号
    'addressInfo': "包河区安凯北区48栋1302",
    'isGraduate': "否",
    'healthStatus': "无异常",
    'isIsolate': "否",
    'isolatePlace': "无"
}
headers = {
    'Host': 'jc.ncu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 wxwork/3.1.13 MicroMessenger/7.0.1 Language/zh ColorScheme/Light',
    'token': 'eyJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJlY2hpc2FuIiwic3ViIjoiNDE1NzAwMjEwMDIwIiwiaWF0IjoxNjMwMjI1MDgxfQ.cpfAXxZpDHENFsW3RuSrbnKMUGUmewqjv46F1JgiJH07mzIcox6mBta73bdMBX2Zm_DazQENFlQfg--B2kY9Mw',  # token填入获取的token
}
   
url = 'http://jc.ncu.edu.cn/gate/student/signIn'
req = requests.post(url, headers=headers, data=date)
# 打卡完毕
   
   
ans = re.sub(u"([^\u4e00-\u9fa5])", "", req.text)
   
# 设置邮件服务器信息
qq = '349858236'  # xxxxxxxxx换成QQ号
mail_host = 'smtp.qq.com'
mail_user = qq + '@qq.com'
mail_pass = 'iadeescmbfgzbhcd'  # SMTP授权码
sender = qq + '@qq.com'
receivers = [qq + '@qq.com']
   
message = MIMEText(ans, 'plain', 'utf-8')
message['Subject'] = '打卡通知'
message['From'] = "Clock In<" + sender + ">"
message['To'] = "Clock In<" + receivers[0] + ">"
   
try:
    smtpObj = smtplib.SMTP_SSL(mail_host)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print('success')
except smtplib.SMTPException as e:
    print('error', e)
