import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')


#to_email_list = ['', '', '', '']
#fot email in to_email_list: 하고 이 밑을 다 들여쓰기 해서 하면 됨 이 때, msg['To'} = email 으로 바꾸기
msg = EmailMessage()
msg['Subject'] = '비가 올까요'
msg['From'] = 'totquf824@naver.com'
msg['To'] = 'sophiasoheeleem923@gmail.com', 'sujee0824@gmail.com'
msg.set_content('오겠죠:)')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('totquf824', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')