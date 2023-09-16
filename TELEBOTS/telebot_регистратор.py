
# Бот регистратор

# 1. Бот должен регистрировать человека на мероприятия
# 2. Записи должны содержать:
# • Имя
# • Фамилию
# • Дату
# • Организацию
# 3. Все записи должны заноситься в БД

!pip install telebot

import telebot
import sqlite3
import pandas as pd

name = None
surname = None
date = None
org = None

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')
@bot.message_handler(commands=['reg'])
def startreg(message):
  startmes = f'Привет {message.from_user.first_name}, я предназначен для регистрации на мероприятие. Для отображения всех команд введи /help'
  bot.send_message(message.chat.id, startmes)
  bot.send_message(message.chat.id, 'Введи имя')
  bot.register_next_step_handler(message,funcname)

def funcname(message):
  global name
  name = message.text
  print(name)
  bot.send_message(message.chat.id, 'Введи фамилию')
  bot.register_next_step_handler(message,funcsurname)

def funcsurname(message):
  global surname
  surname = message.text
  print(surname)
  bot.send_message(message.chat.id, 'Введи дату в формате dd.mm.yyyy')
  bot.register_next_step_handler(message,funcdate)

def funcdate(message):
  global date
  date = message.text
  print(date)
  bot.send_message(message.chat.id, 'Введи организацию')
  bot.register_next_step_handler(message,funcorg)

def funcorg(message):
  global org
  org = message.text
  print (org)
  insertion(name,surname,date,org)
  bot.send_message(message.chat.id,'Вы успешно зарегистрированы')


def insertion(name,surname,date,org):
  con = sqlite3.connect("registration.db")
  cursor = con.cursor()
  createtable ="""CREATE TABLE IF NOT EXISTS persons (
    Name TEXT,
    Surname TEXT,
    Date TEXT,
    Organization TEXT);"""
  cursor.execute(createtable)
  con.commit()
  insertquery = (f"""INSERT INTO persons (Name,Surname,Date,Organization)
  VALUES ('{name}','{surname}','{date}','{org}');""")
  cursor.execute(insertquery)
  con.commit()
  con.close()

@bot.message_handler(commands=['report'])
def report(message):
  bot.send_message(message.chat.id,'Отчет выгружается, ожидайте...')
  con = sqlite3.connect("registration.db")
  query = "SELECT * FROM persons;"
  df = pd.read_sql(query,con)
  df.to_excel('report.xlsx', index = False)
  doc = open('report.xlsx', 'rb')
  bot.send_document(message.chat.id, doc)

@bot.message_handler()
def help(message):
  bot.send_message(message.chat.id,"Извини не понимают тебя, воспользуйся командой /help")

bot.infinity_polling()