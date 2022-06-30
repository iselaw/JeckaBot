import sqlite3

import telebot
import gspread
import os
import time
from time import sleep
import random
from pyrogram.errors import FloodWait
from datetime import datetime
from requests import get
from telebot import types
from fuzzywuzzy import fuzz
import pytz
import requests
import re
import xmltodict
import urllib.request as urllib2
from telebot.types import InputMediaAudio
from typing import Any

UseridMas = []
masScore = []
if os.path.exists('../data/UseridMas.txt'):
    f4 = open('../data/UseridMas.txt', 'r', encoding='UTF-8')
    for x4 in f4:
        UseridMas.append(x4.strip())
    f4.close()
if os.path.exists('../data/balls.txt'):
    f5 = open('../data/balls.txt', 'r', encoding='UTF-8')
    for x5 in f5:
        masScore.append(int(x5))
    f5.close()
n = len(UseridMas)
count = 0
while count < n:
    db = sqlite3.connect('../db/JeckaBot.db')
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO Users (userId, nickname, balance, active) VALUES (?, ?, ?, ?);", (UseridMas[count], f"username{count}", masScore[count], 1))
    except:
        print(UseridMas[count])
    db.commit()
    db.close()
    count = count + 1
