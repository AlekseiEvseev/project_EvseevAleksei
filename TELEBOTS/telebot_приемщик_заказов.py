# Бот приемщик заказов

# 1. Напишите бота, который будет предлагать пользователю
# предоформить заказ
# 2. Должны быть кнопки с наименованием товаров
# 3. У пользователя должна быть возможность просмотреть
# стоимость своего заказа
# 4. Записи должны заноситься в таблицу SQL.

!pip install telebot

import telebot
from telebot import types
import sqlite3
import pandas as pd

user = None
item = None
volume = None

bot = telebot.TeleBot('6653715761:AAHAC87lflhjuTYNJVXIC5IeePmlKgjPpYw')
@bot.message_handler(commands=['purchase'])
def purchase(message):
  global user
  markup = types.ReplyKeyboardMarkup()
  kn1 = types.KeyboardButton('Яблоки')
  kn2 = types.KeyboardButton('Груши')
  markup.row(kn1,kn2)
  kn3 = types.KeyboardButton('Капуста')
  kn4 = types.KeyboardButton('Мандарины')
  markup.row(kn3,kn4)
  kn5 = types.KeyboardButton('Расчет')
  markup.row(kn5)
  bot.send_message(message.chat.id,"Выбери товар:", reply_markup=markup)
  user = message.from_user.id
  bot.register_next_step_handler(message,reply)

def reply(message):
  global item
  item = message.text
  #print (item)
  if item in ('Яблоки', 'Груши', 'Капуста', 'Мандарины'):
    bot.send_message(message.chat.id,"Введи количество в килограммах: ")
    bot.register_next_step_handler(message,volume_f)
  if item in ('Расчет'):
    checkout(message,user)

def checkout(message,user):
  con = sqlite3.connect('fruits.db')
  query = f"SELECT purchase.item, price.price, purchase.volume FROM purchase JOIN price ON purchase.item = price.sku WHERE purchase.uid = {user}"
  dfprice = pd.read_sql(query,con)
  total = 0
  for index, row in dfprice.iterrows():
    vol = row[2]
    pr =  row[1]
    temp_total = int(vol) * int(pr)
    total = total + temp_total
  bot.send_message(message.chat.id,f"Сумма к оплате {total}")

def volume_f(message):
  global volume
  volume = message.text
  bot.register_next_step_handler(message,insertion_bd(user,volume,item))
  bot.clear_step_handler_by_chat_id(message.chat.id)
  purchase(message)

print (user,volume,item)
def insertion_bd(user,volume,item):
  con = sqlite3.connect('fruits.db')
  print (user,volume,item)
  cur = con.cursor()
  create_table = """CREATE TABLE IF NOT EXISTS purchase (
    uid INTEGER,
    volume INTEGER,
    item TEXT);"""
  cur.execute(create_table)
  con.commit()
  insertquery = f"""INSERT INTO purchase (uid,volume,item)
  VALUES
  ('{user}','{volume}','{item}');"""
  cur.execute(insertquery)
  con.commit()
  con.close()

bot.polling(none_stop=True)

import sqlite3
import pandas as pd

con = sqlite3.connect('fruits.db')
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
df.to_sql('price', con, index=False)