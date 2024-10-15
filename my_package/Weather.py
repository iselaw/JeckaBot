import sqlite3
from datetime import datetime

import requests

from Login import *
from my_package.Admin import Admin


class Weather:

    @staticmethod
    def text_city(message, city_name):
        try:
            bot.send_message(chat_id=message.chat.id, text=Weather.get_weather(city_name, open_weather_token))
        except:
            bot.send_message(chat_id=message.chat.id,
                             text="К сожалению, пока не могу подсказать погоду. Что-то поломалось(")

    @staticmethod
    def get_weather(city_name, open_weather_token):
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorn": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }
        try:
            City = city_name
            r = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid={open_weather_token}&units=metric"
            )
            data = r.json()

            cur_city = data["name"]
            cur_weather = data["main"]["temp"]
            cur_humidity = data["main"]["humidity"]
            cur_pressure = data["main"]["pressure"]
            cur_wind = data["wind"]["speed"]
            cur_sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
            weather_description = data["weather"][0]["main"]
            if weather_description in code_to_smile:
                wd = code_to_smile[weather_description]
            else:
                wd = "Не пойму что там, посмотри в окно"
            text = (f"Погода в городе: {cur_city}\nТемпература: {cur_weather}C° {wd}\n"
                    f"Влажность: {cur_humidity}%\nДавление: {cur_pressure} мм.рт.ст\nВетер: {cur_wind}\n"
                    f"Закат Солнца: {cur_sunrise}")
            return text

        except Exception as ex:
            text2 = 'Я не знаю такого города: ' + city_name
            return text2

    @staticmethod
    def weather_start(message):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        cur.execute("UPDATE Users SET weather = 1 WHERE userId = " + str(message.chat.id))
        db.commit()
        db.close()
        bot.send_message(chat_id=message.chat.id, text='В Каком городе тебя интересует погода ?')
        Admin.admin_notification(message, "Пошел смотреть погоду")
        Admin.update_statistic(message, "weather")

    @staticmethod
    def get_weather_text(message):
        db = sqlite3.connect('../resources/db/JeckaBot.db')
        cur = db.cursor()
        for x in cur.execute("SELECT weather FROM Users WHERE userId=" + str(message.chat.id)):
            weatherStatus = x[0]
            if weatherStatus == 1:
                Weather.text_city(message, message.text)
                cur.execute("UPDATE Users SET weather = 0 WHERE userId = " + str(message.chat.id))
                db.commit()
                return True
        db.close()
        if 'погода ' in message.text.lower():
            index = message.text.lower().find("погода ")
            city_name = message.text.lower()[index + len("включи "):].strip()
            Weather.text_city(message, city_name)
            return True
        if 'погода' in message.text.lower():
            Weather.weather_start(message)
            return True
        return False