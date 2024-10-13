import random
from time import sleep

from pyrogram.errors import FloodWait
from requests import get
from telebot import types

from Login import bot
from my_package.Admin import Admin


class Love:

    def search_love(message):
        keylove = types.InlineKeyboardMarkup()
        key_love = types.InlineKeyboardButton(text='Поиск любви', callback_data='love_search_start')
        keylove.add(key_love)
        bot.send_message(message.chat.id, 'Найдем твою любовь?', reply_markup=keylove)

    def love_search_start(message, massive_love):
        perc = random.randint(18, 23)
        while perc < 100:
            try:
                text = "😇 Поиск пары в процессе ..." + str(perc) + "%"
                bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                                      text=text)

                perc += random.randint(14, 27)
                sleep(0.3)

            except FloodWait as e:
                sleep(e.x)

        lenghtMasPara = len(massive_love)
        urlNumber = random.randint(0, lenghtMasPara - 1)
        url = massive_love[urlNumber]
        bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id,
                              text="Твоя Любовь найдена  ❤ ")
        bot.send_photo(chat_id=message.chat.id, photo=get(url).content)

    @staticmethod
    def love_text_set(message):
        if 'любовь' in message.text.lower():
            Love.search_love(message)
            return True
        return False

    @staticmethod
    def love_handler(call, massive_love):
        if call.data == "love_search":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Love.search_love(call.message)
            Admin.updateStatistic(call.message, "para")
        elif call.data == "love_search_start":
            Love.love_search_start(call.message, massive_love)