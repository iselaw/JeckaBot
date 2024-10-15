import xmltodict
from telebot import types
from Login import bot
import urllib.request as urllib2

from my_package.Admin import Admin


class Horoscope:

    @staticmethod
    def handle_AriesMenu(message):
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        key_aries = types.InlineKeyboardButton(text='Овен', callback_data='aries')
        key_taurus = types.InlineKeyboardButton(text='Телец', callback_data='taurus')
        key_gemini = types.InlineKeyboardButton(text='Близнецы', callback_data='gemini')
        key_cancer = types.InlineKeyboardButton(text='Рак', callback_data='cancer')
        key_leo = types.InlineKeyboardButton(text='Лев', callback_data='leo')
        key_virgo = types.InlineKeyboardButton(text='Дева', callback_data='virgo')
        key_libra = types.InlineKeyboardButton(text='Весы', callback_data='libra')
        key_scorpio = types.InlineKeyboardButton(text='Скорпион', callback_data='scorpio')
        key_sagittarius = types.InlineKeyboardButton(text='Стрелец', callback_data='sagittarius')
        key_capricorn = types.InlineKeyboardButton(text='Козерог', callback_data='capricorn')
        key_aquarius = types.InlineKeyboardButton(text='Водолей', callback_data='aquarius')
        key_pisces = types.InlineKeyboardButton(text='Рыбы', callback_data='pisces')
        keyboard.row(key_aries, key_taurus, key_gemini, key_cancer)
        keyboard.row(key_leo, key_virgo, key_libra, key_scorpio)
        keyboard.row(key_sagittarius, key_capricorn, key_aquarius, key_pisces)
        bot.send_message(message.chat.id, 'Какой знак интересует?', reply_markup=keyboard)
        Admin.update_statistic(message, "horoscope")
        Admin.admin_notification(message, "Смотрит гороскоп")

    @staticmethod
    def handle_Aries(message, sign, engSign):
        file = urllib2.urlopen(
            'https://ignio.com/r/export/utf/xml/daily/com.xml')
        data = file.read()
        file.close()
        data = xmltodict.parse(data)
        Aries = sign + '\n' + data["horo"][engSign]["today"]
        bot.send_message(message.chat.id, Aries)

    @staticmethod
    def horoscope_handler(call):
        if call.data == "aries":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Овен", "aries")
        elif call.data == "taurus":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Телец", "taurus")
        elif call.data == "gemini":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Близнецы", "gemini")
        elif call.data == "cancer":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Рак", "cancer")
        elif call.data == "leo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Лев", "leo")
        elif call.data == "virgo":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Дева", "virgo")
        elif call.data == "libra":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Весы", "libra")
        elif call.data == "scorpio":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Скорпион", "scorpio")
        elif call.data == "sagittarius":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Стрелец", "sagittarius")
        elif call.data == "capricorn":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Козерог", "capricorn")
        elif call.data == "aquarius":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Водолей", "aquarius")
        elif call.data == "pisces":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            Horoscope.handle_Aries(call.message, "Рыбы", "pisces")