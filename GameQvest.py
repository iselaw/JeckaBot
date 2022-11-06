import random
from telebot import types
from Login import *
def Qvestt(message, res=False):
	photo1 = open('GameQvest/putnic.jpg', 'rb')
	keygameqvest1 = types.InlineKeyboardMarkup()
	key_askTraveler = types.InlineKeyboardButton(text='Надо бы спросить его', callback_data='askTraveler')
	keygameqvest1.add(key_askTraveler)
	bot.send_photo(chat_id=message.chat.id, photo=photo1, caption='Однажды, в теплый светлый день, Жека вышел из своего дома для того, что бы отправиться за припасами на рынок города.\n\nПо дороге в город вы встречаете напуганного путника.', reply_markup=keygameqvest1)

def Qvest2(message, isFirst, res=False):
	keygameqvest2 = types.InlineKeyboardMarkup()
	key_blacksmith = types.InlineKeyboardButton(text='Пойти до Кузнеца', callback_data='blacksmith')
	keygameqvest2.add(key_blacksmith)
	key_Market = types.InlineKeyboardButton(text='Пойти на Рынок', callback_data='Market')
	keygameqvest2.add(key_Market)
	key_Castle = types.InlineKeyboardButton(text='Пойти в сторону жуткого заброшенного Замка',
											callback_data='Castle')
	keygameqvest2.add(key_Castle)
	if isFirst==True:
		photo1 = open('GameQvest/putnic.jpg', 'rb')
		bot.send_photo(chat_id=message.chat.id, photo=photo1,
					   caption="Путник поведал:\n\"Зря ты без оружия гуляешь по этим местам, Заброшенный Замок неподалеку заселили силы зла во главе с темным рыцарем Листатом. За все время нахождения в замке, прислужники Листата уже похитили 5 девушек из местных деревень и убили 4 торговцев\n\n... Когда я проходил мимо Замка, я наткнулся на группу скелетов-гоблинов, которые начали атаковать меня, я еле убежал от них. Может мне показалось, но еще в небе я увидел огромного красного дракона...\n\n"
							   "И вроде бы он что-то держал в лапах, что-то похожее на мешки с золотом. Советую тебе быть осторожным, лучше купи снаряжение у Кузница в городе\".\nВы прибыли в город. Куда вы хотите отправиться?",
					   reply_markup=keygameqvest2)
	else:
		photo3 = open('GameQvest/Рынок.jpg', 'rb')
		bot.send_photo(chat_id=message.chat.id, photo=photo3,caption="Хммм странно, почему-то сегодня на рынке никого нет, куда же все подевались?",reply_markup=keygameqvest2)


def QvestBlacksith1(message, text, res=False):
	photo2 = open('GameQvest/kuznec.jpg', 'rb')
	keygameqvest3 = types.InlineKeyboardMarkup()
	key_CastleBlacksith = types.InlineKeyboardButton(text='Расскажи про заброшенный замок', callback_data='CastleBlacksith')
	keygameqvest3.add(key_CastleBlacksith)
	key_MarketBlacksith = types.InlineKeyboardButton(text='Почему рынок сегодня не работает?', callback_data='MarketBlacksith')
	keygameqvest3.add(key_MarketBlacksith)
	key_ArmorBlacksith = types.InlineKeyboardButton(text='Ты можешь продать или изготовить для меня доспехи ?', callback_data='ArmorBlacksith')
	keygameqvest3.add(key_ArmorBlacksith)
	bot.send_photo(chat_id=message.chat.id, photo=photo2,caption=text, reply_markup=keygameqvest3)

def	QvestCastle1(message, res=False):
	keygameqvest4 = types.InlineKeyboardMarkup()
	key_CastleOver = types.InlineKeyboardButton(text='Пойти к заброшенному замку', callback_data='CastleOver')
	keygameqvest4.add(key_CastleOver)
	key_CastleDracon = types.InlineKeyboardButton(text='Пойти к Дракону', callback_data='CastleDracon')
	keygameqvest4.add(key_CastleDracon)
	key_QvestCastle1NO = types.InlineKeyboardButton(text='Вернуться назад', callback_data='QvestCastle1NO')
	keygameqvest4.add(key_QvestCastle1NO)
	bot.send_message(message.chat.id, 'Пойти к Заброшенному Замку или Пойти к Дракону ?', reply_markup=keygameqvest4)

def BlacksithPurchase(message, brokenTools, res=False):
	keygameqvest5 = types.InlineKeyboardMarkup()
	key_PriceArmor = types.InlineKeyboardButton(text='Купить доспехи ', callback_data='PriceArmor')
	keygameqvest5.add(key_PriceArmor)
	if (brokenTools==False):
		key_WoodMetal = types.InlineKeyboardButton(text='Где я могу взять металл и дерево?', callback_data='WoodMetal')
		keygameqvest5.add(key_WoodMetal)
	bot.send_message(message.chat.id, 'Ну что? ', reply_markup=keygameqvest5)

def ResourceExtraction(message, res=False):
	keygameqvest6 = types.InlineKeyboardMarkup()
	key_TreeMining = types.InlineKeyboardButton(text='Отправиться добывать дерево', callback_data='TreeMining')
	keygameqvest6.add(key_TreeMining)
	key_MetalMining = types.InlineKeyboardButton(text='Отправиться добывать металл', callback_data='MetalMining')
	keygameqvest6.add(key_MetalMining)
	key_MetalMining = types.InlineKeyboardButton(text='Вернуться и купить Доспехи', callback_data='BuyArmor')
	keygameqvest6.add(key_MetalMining)
	bot.send_message(message.chat.id, 'Куда отправимся в первую очередь?', reply_markup=keygameqvest6)

def TreeMining(message, res=False):
	keygameqvest7 = types.InlineKeyboardMarkup()
	key_TreeMiningON = types.InlineKeyboardButton(text='Высокое и тонкое', callback_data='TreeMiningON')
	keygameqvest7.add(key_TreeMiningON)
	key_TreeMiningExit = types.InlineKeyboardButton(text='Низкое и толстое', callback_data='TreeMiningExit')
	keygameqvest7.add(key_TreeMiningExit)
	bot.send_message(message.chat.id, 'Вы видите 2 разных дерева\nПервое дерево - Высокое и тонкое\nВторое дерево - Низкое и толстое\nКакое дерево будете рубить?', reply_markup=keygameqvest7)

def MetalMining(message, res=False):
	keygameqvest8 = types.InlineKeyboardMarkup()
	key_TreeMiningExit = types.InlineKeyboardButton(text='Из Первой жилы', callback_data='MetalMiningExit')
	keygameqvest8.add(key_TreeMiningExit)
	key_MetalMiningON = types.InlineKeyboardButton(text='Из Второй жилы', callback_data='MetalMiningON')
	keygameqvest8.add(key_MetalMiningON)
	bot.send_message(message.chat.id,
					 'Вы видите две разные жилы металла\nВ первой Жиле Вы видите остатки чужой кирки и помимо металла еще какую-то примесь\nВо второй Жиле Вы видите много металла прям на поверхности\nИз какой жили вы будете добывать металл?',
					 reply_markup=keygameqvest8)

def Outlaw(message, res=False):
	keygameqvest9 = types.InlineKeyboardMarkup()
	key_OutlawYes = types.InlineKeyboardButton(text='Пойти к Бандитам', callback_data='OutlawYes')
	keygameqvest9.add(key_OutlawYes)
	key_OutlawNo = types.InlineKeyboardButton(text='Вернуться назад', callback_data='OutlawNo')
	keygameqvest9.add(key_OutlawNo)
	bot.send_message(message.chat.id,
					 'На нашу деревню часто начали нападать бандиты, их лагерь расположен за городом. Мэр города платит 100 золотых монет тому, кто прогонит',
					 reply_markup=keygameqvest9)

def BanditBattle(message, res=False):
	keygameqvest10 = types.InlineKeyboardMarkup()
	key_BanditDogovor = types.InlineKeyboardButton(text='Попробовать договориться с Бандитом', callback_data='BanditDogovor')
	keygameqvest10.add(key_BanditDogovor)
	key_BanditBattle = types.InlineKeyboardButton(text='Начать бой с Бандитом ', callback_data='BanditBattle')
	keygameqvest10.add(key_BanditBattle)
	bot.send_message(message.chat.id,
					 'Вы пришли в лагерь бандитов. Перед вами стоит самый главный бандит. Вы видите, что у него хороший стальной шлем, но одет он в тканевые тряпки.',
					 reply_markup=keygameqvest10)

def BanditDogovor(message, res=False):
	keygameqvest11 = types.InlineKeyboardMarkup()
	key_DieBandit = types.InlineKeyboardButton(text='Отдать все золото и вернуться к Кузнецу', callback_data='DieBandit')
	keygameqvest11.add(key_DieBandit)
	key_BanditBattle2 = types.InlineKeyboardButton(text='Начать бой с Бандитом ', callback_data='BanditBattle2')
	keygameqvest11.add(key_BanditBattle2)
	bot.send_message(message.chat.id,
					 'Выворачивай карманы и пошел отсюда !!!\n ПОКА ЦЕЛ !!!! ',
					 reply_markup=keygameqvest11)

def BanditBattleExit(message, res=False):
	keygameqvest12 = types.InlineKeyboardMarkup()
	key_BlowHead = types.InlineKeyboardButton(text='Ударить мечом по голове', callback_data='BlowHead')
	keygameqvest12.add(key_BlowHead)
	key_HeartBeat = types.InlineKeyboardButton(text='Ударить мечом в сердце', callback_data='HeartBeat')
	keygameqvest12.add(key_HeartBeat)
	bot.send_message(message.chat.id,
					 'Выберите куда ударить бандита',
					 reply_markup=keygameqvest12)

def ReceivingMoney(message, res=False):
	keygameqvest13 = types.InlineKeyboardMarkup()
	key_ReceivingMoney = types.InlineKeyboardButton(text='Отправиться к мэру города за наградой', callback_data='ReceivingMoney')
	keygameqvest13.add(key_ReceivingMoney)
	bot.send_message(message.chat.id,
					 'После победы Вам нужно отправиться к мэру города за наградой',
					 reply_markup=keygameqvest13)

def	BlacksmithArmorPayment(message, res=False):
	keygameqvest14 = types.InlineKeyboardMarkup()
	key_BlacksmithArmorPayment = types.InlineKeyboardButton(text='Отправиться к Кузнецу за доспехами', callback_data='BlacksmithArmorPayment')
	keygameqvest14.add(key_BlacksmithArmorPayment)
	bot.send_message(message.chat.id,
					 'Вы отправляетесь к Кузнецу',
					 reply_markup=keygameqvest14)

def Castle(message, res=False):
	keygameqvest15 = types.InlineKeyboardMarkup()
	key_CastleArmor = types.InlineKeyboardButton(text='Отправиться к Жуткому заброшенному замку', callback_data='CastleArmor')
	keygameqvest15.add(key_CastleArmor)
	bot.send_message(message.chat.id,
					 'Вы надели доспехи и готовы отправиться к Жуктому заброшенному замку',
					 reply_markup=keygameqvest15)

def MistakeBroken(message, res=False):
	keygameqvest16 = types.InlineKeyboardMarkup()
	key_MistakeBroken = types.InlineKeyboardButton(text='Вернуться к кузнецу', callback_data='MistakeBroken')
	keygameqvest16.add(key_MistakeBroken)
	bot.send_message(message.chat.id,
					 'Отправтесь к кузнецу для покупки доспехов',
					 reply_markup=keygameqvest16)

def GotIt(message, res=False):
	keygameqvest17 = types.InlineKeyboardMarkup()
	key_GotIt = types.InlineKeyboardButton(text='Пойти к кузнецу за доспехами', callback_data='GotIt')
	keygameqvest17.add(key_GotIt)
	bot.send_message(message.chat.id,
					'Отправтесь к кузнецу для покупки доспехов',
					reply_markup=keygameqvest17)

def СhoosePath(message, res=False):
	keygameqvest18 = types.InlineKeyboardMarkup()
	key_СhoosePathCastle = types.InlineKeyboardButton(text='Заброшенный замок', callback_data='СhoosePathCastle')
	keygameqvest18.add(key_СhoosePathCastle)
	key_СhoosePathDragon = types.InlineKeyboardButton(text='Место, куда улетел дракон', callback_data='СhoosePathDragon')
	keygameqvest18.add(key_СhoosePathDragon)
	bot.send_message(message.chat.id,
					 'В какую сторону идти?',
					 reply_markup=keygameqvest18)

def DragonDialogue(message, res=False):
	keygameqvest19 = types.InlineKeyboardMarkup()
	key_DragonDialogue = types.InlineKeyboardButton(text='Подойти к дракону ', callback_data='DragonDialogue')
	keygameqvest19.add(key_DragonDialogue)
	bot.send_message(message.chat.id,
					 'Думаю, стоит приблизиться к дракону, кажется он хочет что-то сказать',
					 reply_markup=keygameqvest19)

def DragonExit(message, res=False):
	keygameqvest20 = types.InlineKeyboardMarkup()
	key_DragonExitGold = types.InlineKeyboardButton(text='Хочу Разбогатеть', callback_data='DragonExitGold')
	keygameqvest20.add(key_DragonExitGold)
	key_DragonExitLove = types.InlineKeyboardButton(text='Хочу Найти любовь', callback_data='DragonExitLove')
	keygameqvest20.add(key_DragonExitLove)
	key_DragonExitOver = types.InlineKeyboardButton(text='Хочу, чтобы ты служил мне ', callback_data='DragonExitOver')
	keygameqvest20.add(key_DragonExitOver)
	bot.send_message(message.chat.id,
					 'Что ты попросишь?',
					 reply_markup=keygameqvest20)

def SkeletonsOfbBry(message, res=False):
	keygameqvest21 = types.InlineKeyboardMarkup()
	key_SkeletonsOfbBry = types.InlineKeyboardButton(text='Атаковать скелетов', callback_data='SkeletonsOfbBry')
	keygameqvest21.add(key_SkeletonsOfbBry)
	bot.send_message(message.chat.id,
					 'Вы достали меч и готовы атаковать скелетов в ответ',
					 reply_markup=keygameqvest21)

def Ingot(message, res=False):
	keygameqvest22 = types.InlineKeyboardMarkup()
	key_IngotYes = types.InlineKeyboardButton(text='Подобрать свиток', callback_data='IngotYes')
	keygameqvest22.add(key_IngotYes)
	bot.send_message(message.chat.id,
					 'Возьми свиток',
					 reply_markup=keygameqvest22)

def Demon(message, res=False):
	keygameqvest23 = types.InlineKeyboardMarkup()
	key_Demon = types.InlineKeyboardButton(text='Подойти к демону', callback_data='Demon')
	keygameqvest23.add(key_Demon)
	bot.send_message(message.chat.id,
					 'Вы увидели демона',
					 reply_markup=keygameqvest23)

def Demon2(message, res=False):
	keygameqvest24 = types.InlineKeyboardMarkup()
	key_Demon2 = types.InlineKeyboardButton(text='Выслушать демона', callback_data='Demon2')
	keygameqvest24.add(key_Demon2)
	bot.send_message(message.chat.id,
					 'Демон начал рассказывать',
					 reply_markup=keygameqvest24)

def Demon3(message, res=False):
	keygameqvest25 = types.InlineKeyboardMarkup()
	key_DemonAmuletYes = types.InlineKeyboardButton(text='Принять Амулет', callback_data='DemonAmuletYes')
	keygameqvest25.add(key_DemonAmuletYes)
	key_DemonAmuletNo = types.InlineKeyboardButton(text='Отказаться', callback_data='DemonAmuletNo')
	keygameqvest25.add(key_DemonAmuletNo)
	bot.send_message(message.chat.id,
					 'Твое решение?',
					 reply_markup=keygameqvest25)

def Boss1(message, res=False):
	keygameqvest26 = types.InlineKeyboardMarkup()
	key_BossAmuletYes = types.InlineKeyboardButton(text='Использовать Амулет для Атаки', callback_data='BossAmuletYes')
	keygameqvest26.add(key_BossAmuletYes)
	key_BossAmuletNo = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='BossAmuletNo')
	keygameqvest26.add(key_BossAmuletNo)
	key_BossExit = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='BossExit')
	keygameqvest26.add(key_BossExit)
	bot.send_message(message.chat.id,
					 'Вы увидели демона Сашаеля, как вы хотите его атаковать?',
					 reply_markup=keygameqvest26)

def Demon4(message, res=False):
	keygameqvest27 = types.InlineKeyboardMarkup()
	key_Demon4 = types.InlineKeyboardButton(text='Пойти дальше', callback_data='Demon4')
	keygameqvest27.add(key_Demon4)
	bot.send_message(message.chat.id,
					 'Вы забрали сердце',
					 reply_markup=keygameqvest27)

def Demon5(message, res=False):
	keygameqvest28 = types.InlineKeyboardMarkup()
	key_DemonHeartYes = types.InlineKeyboardButton(text='Отдать сердце', callback_data='DemonHeartYes')
	keygameqvest28.add(key_DemonHeartYes)
	key_DemonHeartNo = types.InlineKeyboardButton(text='Отказаться', callback_data='DemonHeartNo')
	keygameqvest28.add(key_DemonHeartNo)
	bot.send_message(message.chat.id,
					 'Твое решение?',
					 reply_markup=keygameqvest28)

def MainBoss(message, res=False):
	keygameqvest29 = types.InlineKeyboardMarkup()
	key_MainBossNo = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='MainBossNo')
	keygameqvest29.add(key_MainBossNo)
	key_MainBossExit = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='MainBossExit')
	keygameqvest29.add(key_MainBossExit)
	bot.send_message(message.chat.id,
					 'Что вы будете делать?',
					 reply_markup=keygameqvest29)

def VinBoss(message, res=False):
	keygameqvest30 = types.InlineKeyboardMarkup()
	key_VinBoss = types.InlineKeyboardButton(text='Освободить девушку и забрать золото', callback_data='VinBoss')
	keygameqvest30.add(key_VinBoss)
	bot.send_message(message.chat.id,
					 'Освободить девушку и забрать все золото',
					 reply_markup=keygameqvest30)

def SashaelKill(message, res=False):
	keygameqvest31 = types.InlineKeyboardMarkup()
	key_SashaelKill = types.InlineKeyboardButton(text='Пойти дальше', callback_data='SashaelKill')
	keygameqvest31.add(key_SashaelKill)
	bot.send_message(message.chat.id,
					 'Вы забрали сердце',
					 reply_markup=keygameqvest31)

def SashaelKill2(message, res=False):
	keygameqvest32 = types.InlineKeyboardMarkup()
	key_SashaelKillYes = types.InlineKeyboardButton(text='Отдать сердце', callback_data='SashaelKillYes')
	keygameqvest32.add(key_SashaelKillYes)
	key_SashaelKillNo = types.InlineKeyboardButton(text='Отказаться', callback_data='SashaelKillNo')
	keygameqvest32.add(key_SashaelKillNo)
	bot.send_message(message.chat.id,
					 'Твое решение?',
					 reply_markup=keygameqvest32)

def MainBoss2(message, res=False):
	keygameqvest33 = types.InlineKeyboardMarkup()
	key_Died = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='Died')
	keygameqvest33.add(key_Died)
	key_HeartAttack = types.InlineKeyboardButton(text='Съесть сердце Сашаеля и атаковать', callback_data='HeartAttack')
	keygameqvest33.add(key_HeartAttack)
	key_ScrollAttack = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='ScrollAttack')
	keygameqvest33.add(key_ScrollAttack)
	bot.send_message(message.chat.id,
					 'Что вы будете делать?',
					 reply_markup=keygameqvest33)

def VinBoss2(message, res=False):
	keygameqvest34 = types.InlineKeyboardMarkup()
	key_VinBoss2 = types.InlineKeyboardButton(text='Освободить девушку и забрать золото', callback_data='VinBoss2')
	keygameqvest34.add(key_VinBoss2)
	bot.send_message(message.chat.id,
					 'Освободить девушку и забрать все золото',
					 reply_markup=keygameqvest34)

def TenYears(message, res=False):
	keygameqvest35 = types.InlineKeyboardMarkup()
	key_TenYears = types.InlineKeyboardButton(text='Спустя 10 лет', callback_data='TenYears')
	keygameqvest35.add(key_TenYears)
	bot.send_message(message.chat.id,
					 'Что же произошло?',
					 reply_markup=keygameqvest35)

def JekaDemon(message, res=False):
	keygameqvest36 = types.InlineKeyboardMarkup()
	key_JekaDemon = types.InlineKeyboardButton(text='Наброситься на врага', callback_data='JekaDemon')
	keygameqvest36.add(key_JekaDemon)
	bot.send_message(message.chat.id,
					 'Атакуем',
					 reply_markup=keygameqvest36)

def JekaDemon2(message, res=False):
	keygameqvest37 = types.InlineKeyboardMarkup()
	key_JekaDemon2 = types.InlineKeyboardButton(text='Продолжить', callback_data='JekaDemon2')
	keygameqvest37.add(key_JekaDemon2)
	bot.send_message(message.chat.id,
					 'Что же будет дальше',
					 reply_markup=keygameqvest37)

def MainBoss3(message, res=False):
	keygameqvest38 = types.InlineKeyboardMarkup()
	key_Died2 = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='Died2')
	keygameqvest38.add(key_Died2)
	key_HeartAttack2 = types.InlineKeyboardButton(text='Съесть сердце Сашаеля и атаковать', callback_data='HeartAttack2')
	keygameqvest38.add(key_HeartAttack2)
	bot.send_message(message.chat.id,
					 'Что вы будете делать?',
					 reply_markup=keygameqvest38)

def TakeSword(message, res=False):
	keygameqvest39 = types.InlineKeyboardMarkup()
	key_TakeSword = types.InlineKeyboardButton(text='Взять Меч', callback_data='TakeSword')
	keygameqvest39.add(key_TakeSword)
	bot.send_message(message.chat.id,
					 'Взять меч',
					 reply_markup=keygameqvest39)

def MainBoss4(message, res=False):
	keygameqvest40 = types.InlineKeyboardMarkup()
	key_SwordAttack = types.InlineKeyboardButton(text='Атаковать клинком Бездны', callback_data='SwordAttack')
	keygameqvest40.add(key_SwordAttack)
	bot.send_message(message.chat.id,
					 'Что вы будете делать?',
					 reply_markup=keygameqvest40)

def Boss2(message, res=False):
	keygameqvest41 = types.InlineKeyboardMarkup()
	key_BossAmuletNo2 = types.InlineKeyboardButton(text='Атаковать без усилений', callback_data='BossAmuletNo2')
	keygameqvest41.add(key_BossAmuletNo2)
	key_BossExit2 = types.InlineKeyboardButton(text='Использовать Свиток для Атаки', callback_data='BossExit2')
	keygameqvest41.add(key_BossExit2)
	bot.send_message(message.chat.id,
					 'Вы увидели демона Сашаеля, как вы хотите его атаковать?',
					 reply_markup=keygameqvest41)