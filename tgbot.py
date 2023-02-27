import telebot
from telebot import types
bot = telebot.TeleBot('6015057702:AAHA4oBHgxFcg5JgpGEmxGD4Ddy4n9IhnDE')

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['help'])
def help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    vbucks = types.KeyboardButton('/vbucks')
    vbgift = types.KeyboardButton('/vbucks_gift')
    cods = types.KeyboardButton('/code')
    nitro = types.KeyboardButton('/discord_nitro')
    bp = types.KeyboardButton('/battle_pass')
    exclusive = types.KeyboardButton('/exclusive')
    contacts = types.KeyboardButton('/contacts')
    nabori = types.KeyboardButton('/packs')
    markup.add(vbucks,vbgift,cods, nitro,bp,nabori,contacts,exclusive)
    bot.send_message(message.chat.id, 'Меню взаимодействия:', reply_markup=markup)

@bot.message_handler(commands=['vbucks'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['vbgift'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['cods'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['nitro'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['bp'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['nabori'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['exclusive'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')

@bot.message_handler(commands=['contacts'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')
bot.polling(none_stop=True)
