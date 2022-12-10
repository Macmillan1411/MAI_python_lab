import telebot
import requests
from keys import API_KEY

TOKEN = API_KEY

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start,help'])
def start(message):
	bot.send_message(message.chat.id,"type a country name to get its flag")


@bot.message_handler(content_types=['text'])
def get_user_text(message):
	
	try:
		name = str(message.text)
		resp = requests.get(f'https://restcountries.com/v3.1/name/{name}')
		flag = resp.json()[0]['flags']['png']
		print(flag)
		bot.send_photo(message.chat.id,flag)
		
	except:
		bot.send_message(message.chat.id,"Please type a country name!")

bot.polling(non_stop=True)




