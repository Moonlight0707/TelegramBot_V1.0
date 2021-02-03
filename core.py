import telebot

import config
import sendmail
import data
import pars_func

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands = ['start'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard = False)
	button1 = types.KeyboardButton('🌐 О компании')
	button2 = types.KeyboardButton('🗃 Наши проекты')
	button3 = types.KeyboardButton('🏢 Наши адреса')
	button4 = types.KeyboardButton('🤝 Стать нашим клиентом')
	button5 = types.KeyboardButton('📱 Оставить свой Telegram номер', request_contact=True)

	markup.add(button1,button2, button3, button4, button5)
	bot.send_message(message.chat.id, "Привет {0.first_name}!\nДобро пожаловать в ДОКА GROUP.\n"
		"Меня зовут {1.first_name}, и я здесь, чтобы познакомить Вас с нами!".format(message.from_user, bot.get_me()),parse_mode = 'html',reply_markup = markup)

@bot.message_handler(commands = ['help'])
def help(message):
	bot.send_message(message.chat.id, data.help_message)

@bot.message_handler(content_types = ['text'])
def reaction(message):
	if message.chat.type == 'private':
		if message.text == '🌐 О компании':
			bot.send_message(message.chat.id, data.about_company)

		elif  message.text == '🗃 Наши проекты':
			bot.send_message(message.chat.id, '\nНаши последние клиенты:\n'+pars_func.parse_clients()+'\n'+data.our_projects)

		elif  message.text == '🤝 Стать нашим клиентом':
			bot.send_message(message.chat.id, data.clients)
			data.flag = True

		elif  message.text == '🏢 Наши адреса':
			bot.send_message(message.chat.id, pars_func.parse_adres())

		elif data.number_ver(message.text) and data.flag == True and ((len(message.text)==12 and message.text[0]+message.text[1]=='+7') or (len(message.text)==11 and (message.text[0]=='7' or message.text[0]=='8'))):
			sendmail.doka_send("У нас новый клиент, его зовут {0.first_name}, обязательно позвоните ему по номеру: {1}".format(message.from_user, message.text))
			bot.send_message(message.chat.id,"Спасибо {0.first_name}!\nМы свяжемся с вами\nпо номеру: {1}.".format(message.from_user, message.text))
			data.flag=False

		elif data.number_ver(message.text) and len(message.text)!=10 and data.flag == True:
			bot.send_message(message.chat.id,"Некорректно введен номер телефона.")
			
		else:
			bot.send_message(message.chat.id, "Неизвестная команда, пожалуйста воспольуйтесь одной из перечисленных команд ⬇")

@bot.message_handler(content_types = ['contact'])
def share_phone(message):
			sendmail.doka_send("У нас новый клиент, его зовут {0}, обязательно позвоните ему по номеру: {1}".format(message.contact.first_name, message.contact.phone_number))
			bot.send_message(message.chat.id,"Спасибо {0}!\nМы свяжемся с вами\nпо номеру: {1}.".format(message.contact.first_name, message.contact.phone_number))
			data.flag=False

bot.polling(none_stop=True)