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
    vbucks = types.KeyboardButton('Вбаксы')
    vbgift = types.KeyboardButton('Подарки')
    cods = types.KeyboardButton('Коды')
    nitro = types.KeyboardButton('Дискорд нитро')
    bp = types.KeyboardButton('Боевой пропуск')
    exclusive = types.KeyboardButton('Эксклюзивы')
    contacts = types.KeyboardButton('Контакты')
    nabori = types.KeyboardButton('Наборы')
    call = types.KeyboardButton('Уведомления')
    markup.add(vbucks,vbgift,cods, nitro,bp,nabori,contacts,exclusive,call)
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

@bot.message_handler(commands=['call'])
def welcome(message):
    bot.send_message(message.chat.id, 'Добро пожаловать в Eleven shop!'
                                      ' Здесь Вы сможеет купить в баксы подарком,'
                                      ' коды, эксклюзивы и многое другое! Более точно можно'
                                      ' ознакомиться нажав /help')
bot.polling(none_stop=True)
