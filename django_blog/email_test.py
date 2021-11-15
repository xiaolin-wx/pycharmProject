import string
import random
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import smtplib

def sendEmail(str, receiver):
    # 设置服务器
    mail_host = 'smtp.qq.com'
    # 密码(部分邮箱为授权码)
    mail_pass = 'cjdzhofgbveubife'
    # 邮件发送方邮箱地址
    sender = '1667827660@qq.com'
    # 邮件内容设置
    message = MIMEText(str, 'plain', 'utf-8')
    # 邮件主题
    message['Subject'] = 'CDP-wiki'
    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receiver
    # 登录并发送邮件

    # 添加一个txt文本附件
    with open('abc.txt', 'r')as h:
        content2 = h.read()
    # 设置txt参数
    part2 = MIMEText(content2, 'plain', 'utf-8')
    # 附件设置内容类型，方便起见，设置为二进制流
    part2['Content-Type'] = 'application/octet-stream'
    # 设置附件头，添加文件名
    part2['Content-Disposition'] = 'attachment;filename="abc.txt"'
    # 添加照片附件
    with open('1.png', 'rb')as fp:
        picture = MIMEImage(fp.read())
        # 与txt文件设置相似
        picture['Content-Type'] = 'application/octet-stream'
        picture['Content-Disposition'] = 'attachment;filename="1.png"'
    # 将内容附加到邮件主体中
    # message.attach(part1)
    # message.attach(part2)
    # message.attach(picture)


    try:
        # 连接到服务器的两种方式
        # 1
        # smtpObj = smtplib.SMTP()
        # smtpObj.connect(mail_host, 25)
        # 2  需要ssl验证
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # 登录到服务器
        smtpObj.login(sender, mail_pass)

        # 发送
        smtpObj.sendmail(
            sender, receiver, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误

def main():
    receiver = input("请接受的qq号；")
    receiver = receiver + "@qq.com"
    # 验证码生成
    str1 = string.ascii_letters + string.digits
    str = "验证码：" + ''.join(random.sample(str1, 6))
    print(str)
    sendEmail(str=str, receiver=receiver)

if __name__ == '__main__':
    main()