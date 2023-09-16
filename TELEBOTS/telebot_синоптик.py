
# Бот синоптик

# 1. Напишите бота, выдающего текущую
# температуру воздуха в градусах Цельсия
# 2. Бот должен выдавать температуру по
# наименованию города (rus/eng)
# 3. В обратном сообщении бот должен высылать
# следующее сообщение: «Сейчас в cityname
# температура воздуха xx градусов.»

!pip install telebot

import telebot
import requests
import json
api = '34ba4b20316ab16dc32e5a5be0430185'
bot = telebot.TeleBot('6653715761:AAHAC87lflhjuTYNJVXIC5IeePmlKgjPpYw')
@bot.message_handler(commands=['help'])
def start(message):
  bot.reply_to(message,"Привет, я бот синоптик. Введи название города.")
@bot.message_handler()
def get_weather(message):
  city = message.text.strip().lower()
  result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
  data = json.loads(result.text)
  statuscode = data["cod"]
  pic = open('test.png', 'rb')
  match statuscode:
    case 200:
      temp = int(data["main"]["temp"])
      cord = data["coord"]["lon"]
      cord2 = data["coord"]["lat"]
      bot.reply_to(message,f'Сейчас температура в указанном вами городе {temp} Долгота {cord}, широта {cord2}')
      if temp > 20:
        bot.send_photo(message.chat.id,pic)
    case 400:
      bot.reply_to(message,"Введи корректное наименование города")
    case _:
      bot.reply_to(message,"Ошибка сервера")
bot.polling(none_stop=True)

import requests
import json
api = '34ba4b20316ab16dc32e5a5be0430185'
city = 'Москва'
result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric')
data = json.loads(result.text)
print (data)
cord = data["coord"]["lon"]
cord2 = data["coord"]["lat"]
weather = data['weather']
print (cord)
print (cord2)
print (weather)

val = int(input("Введи число:"))
match val:
  case 1:
    print ("Добрый день")
  case 2:
    print ("Добрый вечер")
  case 3:
    print ("Доброе утро")
  case _:
    print ("Случайное значение")