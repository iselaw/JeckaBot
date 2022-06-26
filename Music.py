import random
import os
import requests
from telebot.types import InputMediaAudio
from bs4 import BeautifulSoup
from telebot import types
from Login import *
masaudio = []
if os.path.exists('data/AudioMas.txt'):
    f6 = open('data/AudioMas.txt', 'r', encoding='UTF-8')
    for x6 in f6:
        masaudio.append(x6.strip())
    f6.close()

def audio_processing(message, isFirstAudio):
    key_like = types.InlineKeyboardButton(text='❤', callback_data='audioLike')
    key_nextTrack = types.InlineKeyboardButton(text='>>>', callback_data='audionext')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(key_like)
    keyboard.add(key_nextTrack)
    lenghtAudioMas = len(masaudio)
    audio = random.randrange(0, lenghtAudioMas - 1, 3)
    audioo = masaudio[audio]
    nextAudio(message, audioo, keyboard, isFirstAudio)

def nextAudio(message, audioo, keyboard, isFirstAudio):
    if isFirstAudio == False:
        bot.edit_message_media(chat_id=message.chat.id, message_id=message.message_id, media=InputMediaAudio(audioo),
                               reply_markup=keyboard)
    if isFirstAudio == True:
        bot.send_audio(chat_id=message.chat.id, audio=audioo, reply_markup=keyboard)

def LikePlayList(message):
    PlayList = open('usersPlayLists/music' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    i = 0
    isPList = True
    for x7 in PlayList:
        i = + 1
        if x7.strip() == str(message.audio.file_unique_id):
            isPList = False
            bot.send_message(message.chat.id, "Трек уже есть")
    if isPList == True:
        PlayList = open('usersPlayLists/music' + str(message.chat.id) + '.txt', 'a', encoding='UTF-8')
        PlayList.write(message.audio.file_id + '\n' + message.audio.file_unique_id + '\n')
        bot.send_message(message.chat.id, "{} - Трек сохранен".format(message.audio.file_name))
    PlayList.close()

def PlayList(message):
    List = []
    ListPlay = open('usersPlayLists/music' + str(message.chat.id) + '.txt', 'r', encoding='UTF-8')
    for x8 in ListPlay:
        List.append(x8.strip())
    for i in range(0, len(List), 2):
        audioo = List[i]
        bot.send_audio(chat_id=message.chat.id, audio=audioo)
