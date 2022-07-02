import sqlite3
import random
import requests
from bs4 import BeautifulSoup
from telebot import types
from Login import *
def anime(message):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for rand in cur.execute('SELECT * FROM Anime WHERE ID IN (SELECT ID FROM Anime ORDER BY RANDOM() LIMIT 1)'):
        Film_name = rand[1]
        Film_KP = rand[2]
        Film_Imdb = rand[3]
        Description = rand[4]
        Image = rand[5]
        link1 = rand[6]
        link2 = link1.split('.', 1)[1]
        link3 = "https://m." + link2
        Film_itog = (f"Название Аниме: {Film_name}\nОценки Аниме:\nКинопоиск - {Film_KP}\n"
                     f"Imdb - {Film_Imdb}\n{Description}")
        db.close
        try:
            user_agent_list = [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            ]

            user_agent = random.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            page3 = BeautifulSoup(requests.get(link3, headers=headers).text, "lxml")
            film_play1 = page3.find("div", class_="tabs-b video-box").find('iframe').get('src')
            film_play = ("https:" + film_play1)
            markup = types.InlineKeyboardMarkup()
            btn_my_site = types.InlineKeyboardButton(text='Посмотреть фильм', url=film_play)
            markup.add(btn_my_site)
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)
            bot.send_message(message.chat.id, "Нажми на кнопку что бы посмотреть фильм", reply_markup=markup)
        except:
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)
def mult(message):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for rand in cur.execute('SELECT * FROM Mult WHERE ID IN (SELECT ID FROM Mult ORDER BY RANDOM() LIMIT 1)'):
        Film_name = rand[1]
        Film_KP = rand[2]
        Film_Imdb = rand[3]
        Description = rand[4]
        Image = rand[5]
        link1 = rand[6]
        link2 = link1.split('.', 1)[1]
        link3 = "https://m." + link2
        Film_itog = (f"Название Мультика: {Film_name}\nОценки Мультика:\nКинопоиск - {Film_KP}\n"
                     f"Imdb - {Film_Imdb}\n{Description}")
        db.close
        try:
            user_agent_list = [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            ]

            user_agent = random.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            page3 = BeautifulSoup(requests.get(link3, headers=headers).text, "lxml")
            film_play1 = page3.find("div", class_="tabs-b video-box").find('iframe').get('src')
            film_play = ("https:" + film_play1)
            markup = types.InlineKeyboardMarkup()
            btn_my_site = types.InlineKeyboardButton(text='Посмотреть фильм', url=film_play)
            markup.add(btn_my_site)
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)
            bot.send_message(message.chat.id, "Нажми на кнопку что бы посмотреть фильм", reply_markup=markup)
        except:
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)
def film(message):
    db = sqlite3.connect('db/JeckaBot.db')
    cur = db.cursor()
    for rand in cur.execute('SELECT * FROM Films WHERE ID IN (SELECT ID FROM Films ORDER BY RANDOM() LIMIT 1)'):
        Film_name = rand[1]
        Film_KP = rand[2]
        Film_Imdb = rand[3]
        Description = rand[4]
        Image = rand[5]
        link1 = rand[6]
        link2 = link1.split('.', 1)[1]
        link3 = "https://m." + link2
        Film_itog = (f"Название Фильма: {Film_name}\nОценки Фильма:\nКинопоиск - {Film_KP}\n"
                     f"Imdb - {Film_Imdb}\n{Description}")
        db.close
        try:
            user_agent_list = [
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
            ]

            user_agent = random.choice(user_agent_list)
            headers = {'User-Agent': user_agent}
            page3 = BeautifulSoup(requests.get(link3, headers=headers).text, "lxml")
            film_play1 = page3.find("div", class_="tabs-b video-box").find('iframe').get('src')
            film_play = ("https:" + film_play1)
            markup = types.InlineKeyboardMarkup()
            btn_my_site = types.InlineKeyboardButton(text='Посмотреть фильм', url=film_play)
            markup.add(btn_my_site)
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)
            bot.send_message(message.chat.id, "Нажми на кнопку что бы посмотреть фильм", reply_markup=markup)
        except:
            bot.send_photo(message.chat.id, photo=Image)
            bot.send_message(message.chat.id, text=Film_itog)