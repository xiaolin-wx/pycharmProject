import smtplib
from email.mime.text import MIMEText
import string
import random

def sendEmail(str, receiver):
    #设置服务器
    mail_host = 'smtp.qq.com'
    #密码(部分邮箱为授权码)
    mail_pass = 'cjdzhofgbveubife'
    #邮件发送方邮箱地址
    sender = '1667827660@qq.com'
    #邮件内容设置
    message = MIMEText(str,'plain','utf-8')
    #邮件主题
    message['Subject'] = 'CDP-wiki'
    #发送方信息
    message['From'] = sender
    #接受方信息
    message['To'] = receiver

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(sender,mail_pass)
        #发送
        smtpObj.sendmail(
            sender,receiver,message.as_string())
        #退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

def main():
    receiver = input("请接受的qq号；")
    # receiver = receiver + "@qq.com"
    # 验证码生成
    str1 = string.ascii_letters + string.digits
    str = "验证码：" + ''.join(random.sample(str1, 6))
    print(str)
    sendEmail(str = str, receiver = receiver)

if __name__ == '__main__':
    main()