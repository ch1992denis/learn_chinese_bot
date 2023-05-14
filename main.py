import os

import telebot
from telebot import types
import random
from random import choice
import time
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start']) #стартовая команда
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Учим слова HSK")
    btn2 = types.KeyboardButton("Примеры")
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id,
'''Привет!
    
Я бот-помощник в изучении китайского языка 🇨🇳

Вместе мы подготовимся к экзамену HSK: освоим базовую лексику для каждого уровня и закрепим примерами употребления новых слов

С чего начнем? Поучим слова или посмотрим на примеры употребления?''', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'HSK 1' or message.text == 'Еще слова HSK1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK1')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK1_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK1_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK1_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'HSK 2' or message.text == 'Еще слова HSK2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK2')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK2_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK2_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK2_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'HSK 3' or message.text == 'Еще слова HSK3':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK3')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK3_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK3_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK3_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'HSK 4' or message.text == 'Еще слова HSK4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK4')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK4_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK4_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK4_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'HSK 5' or message.text == 'Еще слова HSK5':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK5')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK5_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK5_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK5_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'HSK 6' or message.text == 'Еще слова HSK6':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('🔙 Вернуться к выбору уровня HSK')
        btn2 = types.KeyboardButton('Еще слова HSK6')
        btn3 = types.KeyboardButton('Главное меню')
        markup.add(btn1, btn2, btn3)
        with open('HSK6_vocabulary.txt', 'r', encoding='utf-16') as file:
            HSK6_words = file.readlines()
        for i in range(5):
            temp = random.choice(HSK6_words)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'Примеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        btn2 = types.KeyboardButton('Еще примеры')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Я тут подготовил для тебя чуть более 2000 предложений и словосочетаний, погнали!", reply_markup=markup)
        time.sleep(2)
        with open('Examples.txt', 'r', encoding='utf-16') as file:
            examples = file.readlines()
        for i in range(5):
            temp = random.choice(examples)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)
    elif message.text == 'Еще примеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Главное меню')
        btn2 = types.KeyboardButton('Еще примеры')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Примеров много не бывает 😉", reply_markup=markup)
        time.sleep(2)
        with open('Examples.txt', 'r', encoding='utf-16') as file:
            examples = file.readlines()
        for i in range(5):
            temp = random.choice(examples)
            temp = temp[:temp.find(' ')] + '||' + temp[temp.find(' '):] + '||'
            bot.send_message(message.from_user.id, temp, parse_mode="MarkdownV2", reply_markup=markup)

    elif message.text == 'Главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Учим слова HSK")
        btn2 = types.KeyboardButton("Примеры")
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Итак, продолжим изучение слов или перейдем к примерам?", reply_markup=markup)

    elif message.text == 'Учим слова HSK':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("HSK 1")
        btn2 = types.KeyboardButton("HSK 2")
        btn3 = types.KeyboardButton("HSK 3")
        btn4 = types.KeyboardButton("HSK 4")
        btn5 = types.KeyboardButton("HSK 5")
        btn6 = types.KeyboardButton("HSK 6")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '''Давай сперва определимся с уровнем экзамена HSK. Напомню, в моей базе хранится:
✅ 150 слов для HSK 1
✅ 300 слов для HSK 2
✅ 600 слов для HSK 3
✅ 1200 слов для HSK 4
✅ 2500 слов для HSK 5
✅ 5000 слов для HSK 6''', reply_markup=markup)

    elif message.text == '🔙 Вернуться к выбору уровня HSK':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("HSK 1")
        btn2 = types.KeyboardButton("HSK 2")
        btn3 = types.KeyboardButton("HSK 3")
        btn4 = types.KeyboardButton("HSK 4")
        btn5 = types.KeyboardButton("HSK 5")
        btn6 = types.KeyboardButton("HSK 6")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, 'Ок, выбери уровень HSK', reply_markup=markup)

    #small talk
    elif message.text == "Привет" or message.text == "привет":
        start(message)
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет или /start, и мы начнем обучение")
    elif message.text == "Пока" or message.text == "пока":
        bot.send_message(message.from_user.id, "Заходи еще, 5000 слов сами себя не выучат!")

bot.polling(none_stop=True, interval=0)
