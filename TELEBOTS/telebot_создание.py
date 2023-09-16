!pip install telebot

import telebot

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')

@bot.message_handler(commands=['start','go'])
def start(message):
  bot.send_message(message.chat.id,"Привет")

@bot.message_handler(commands=['help'])
def help(message):
  bot.send_message(message.chat.id,"Cписок доступных команд:...")

@bot.message_handler()
def help(message):
  bot.send_message(message.chat.id,"Извини не понимают тебя, воспользуйся командой /help")

bot.polling(none_stop=True)

import telebot

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')

@bot.message_handler(commands=['start'])
def start1(message):
  bot.reply_to(message,message)

bot.polling(none_stop=True)

import telebot

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')

@bot.message_handler(content_types=['document','text','photo'])
def define(message):
  if message.photo:
    bot.send_message(message.chat.id,"Eto photo")
  elif message.text:
    photo = open('pandas.pdf', 'rb')
    bot.send_document(message.chat.id, photo)
  elif message.document:
    bot.send_message(message.chat.id,"Eto document")


bot.polling(none_stop=True)

#Вложенные в сообщения кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')
@bot.message_handler(commands=['start'])
def knopki(message):
  markup = types.InlineKeyboardMarkup()
  markup.add(types.InlineKeyboardButton("Тест 1", url='https://ya.ru/'))
  markup.add(types.InlineKeyboardButton("Тест 2", url='https://ya.ru/'))
  markup.add(types.InlineKeyboardButton("Тест 3", url='https://ya.ru/'))
  markup.add(types.InlineKeyboardButton("Тест 4", url='https://ya.ru/'))
  bot.send_message(message.chat.id,"Привет",reply_markup=markup)



bot.polling(none_stop=True)

#Вложенные в сообщения кнопки с функциями и раскладкой
import telebot
from telebot import types

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')
@bot.message_handler(commands=['start'])
def knopki(message):
  markup = types.InlineKeyboardMarkup()
  kn1 = types.InlineKeyboardButton("Тест 1", url='https://ya.ru/')
  kn2 = types.InlineKeyboardButton("Тест 2", callback_data="test2")
  markup.row(kn1,kn2)
  kn3 = types.InlineKeyboardButton("Тест 3", callback_data="test3")
  kn4 = types.InlineKeyboardButton("Тест 4", callback_data="test4")
  markup.row(kn3,kn4)
  bot.send_message(message.chat.id,"Привет",reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
  if callback.data == "test3":
    bot.send_message(callback.message.chat.id,"Knopka 3 otrabotala")

bot.polling(none_stop=True)

#Вложенные в чат кнопки
import telebot
from telebot import types

bot = telebot.TeleBot('6653715761:AAHdgLPq_QMylPwh1c51g1c7Ox8h2p41WxM')
@bot.message_handler(commands=['start'])
def knopkichat(message):
  markup = types.ReplyKeyboardMarkup()
  btn1 = types.KeyboardButton("Кнопка 1")
  btn2 = types.KeyboardButton("Кнопка 2")
  markup.row(btn1,btn2)
  btn3 = types.KeyboardButton("Кнопка 3")
  btn4 = types.KeyboardButton("Кнопка 4")
  markup.row(btn3,btn4)
  bot.send_message(message.chat.id,"Привет",reply_markup=markup)
  bot.register_next_step_handler(message,reply)

def reply(message):
  if message.text == "Кнопка 4":
    bot.send_message(message.chat.id,"Knopka 4 otrabotala")


bot.polling(none_stop=True)