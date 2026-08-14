import telebot 
from random import randint
from random import choice
from config import token
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token) 
classes = [Pokemon, Wizard, Fighter]

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Добро пожаловать! Создайте покемона командой /go или просматрите все команды командой /help")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "Команды: /go - Создать покемона, /info - Просмотреть информацию о покемоне\n/heal - Подлечить покемона, /feed - Покормить покемона\n/start - Показать начяльные команды")

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        random_class = classes[randint(0, len(classes) - 1)]
        pokemon = random_class(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, pokemon.show_link())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_nummber())
        bot.send_video(message.chat.id, pokemon.show_animation())
        bot.send_message(message.chat.id, 'вы можете подлечить покемона командой /heal')
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['pikachu'])
def pikachu(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username, 25)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, pokemon.show_link())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_nummber())
        bot.send_video(message.chat.id, pokemon.show_animation())
    else:
        bot.reply_to(message, "Ты уже создал себе пикачу")

@bot.message_handler(commands=['heal'])
def heal(message):
    pokemon = Pokemon.pokemons[message.from_user.username]
    pokemon_hp = pokemon.hp
    if pokemon.hp < pokemon.maxhp:
        if pokemon.bonus > 0:
            heal_num = pokemon.maxhp - pokemon.hp
            if pokemon.bonus >= heal_num:
                pokemon.hp += pokemon.bonus
                pokemon.bonus -= heal_num
            else:
                pokemon.hp += pokemon.bonus
                pokemon.bonus -= pokemon.bonus
            heel_last_num = pokemon.hp - pokemon_hp
            bot.send_message(message.chat.id, f'Вы подлечили своего покемона на {heel_last_num} хп. Теперь у него {pokemon.hp} хп')
        else:
            bot.send_message(message.chat.id, f'У вашего покемона нет бонуса для лечения. У него {pokemon.hp}/{pokemon.maxhp}. Для получения бонуса выйграйте бой')
    else:
        bot.send_message(message.chat.id, f'У вашего покемона полное здоровье. У него {pokemon.hp} хп')

@bot.message_handler(commands=['info'])
def info_main(message):
    global Pokemon
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.send_message(message.chat.id, 'У вас пока нет покемона создпете его через команду /go')

@bot.message_handler(commands=['feed'])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pokemon = Pokemon.pokemons[message.from_user.username]
        bot.reply_to(message, pokemon.feed())
    else:
        bot.send_message(message.chat.id, 'У вас пока нет покемона создпете его через команду /go')

bot.infinity_polling(none_stop=True)
