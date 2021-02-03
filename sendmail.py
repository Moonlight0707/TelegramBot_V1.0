import smtplib
import config
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText  

def doka_send(body):
	smtpObj = smtplib.SMTP(config.type_mail, 587)	#Подключение к серверу электронной почты ('smtp.gmail.com','smtp.yandex.ru'....)
	smtpObj.starttls() 								#Шифрование с помощью протокола TLS
	smtpObj.login(config.login,config.password) 	#Авторизация
	msg = MIMEMultipart()							#Многокомпонентный объект

	msg['From'] = config.login_rec 					#Отправитель  
	password = config.password						#Отправитель-пароль                        
	msg['To'] = config.login_rec					#Получатель
	msg['Subject'] = 'Номер клиента' 				#Тема сообщения
	##body = ""										#Текст сообщения
	
	msg.attach(MIMEText(body, 'plain'))  
	smtpObj.send_message(msg) 
	smtpObj.quit()
