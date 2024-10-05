import telebot
import gspread
# ZhekaMatuxovbotTestbot token
# bot = telebot.TeleBot('5231426811:AAEgODwFTSgKDcRnIL1smBYtDZpw2Cf5w64')
# Prod token
bot = telebot.TeleBot('5282174711:AAG0MmGq7Op3O0Uv1yfW4lraRzhysKN2V9Y')
admin = [1349611778, 425041981, 677784600]
ignoreList = [-754170909]
gs = gspread.service_account(filename='zhekamatuxovbot-87ff0c553364.json')  # подключаем файл с ключами и пр.
sh = gs.open_by_key('14RGCwOhoSadmE8iTXvnmtHqP-cRN-uK7aATWbb0fgOw')  # подключаем таблицу по ID
open_weather_token = '9ab864194f5db1221616acba01d06b92'
worksheet = sh.sheet1