import telebot 
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 
pikachu_nummer = 0

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, pokemon.show_link())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_nummber())
        bot.send_video(message.chat.id, pokemon.show_animation())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['pikachu'])
def go(message):
    global pikachu_nummer
    if pikachu_nummer == 0:
        pokemon = Pokemon(message.from_user.username, 25)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_message(message.chat.id, pokemon.show_link())
        bot.send_photo(message.chat.id, pokemon.show_img())
        bot.send_message(message.chat.id, pokemon.show_nummber())
        bot.send_video(message.chat.id, pokemon.show_animation())
        pikachu_nummer += 1
    else:
        bot.reply_to(message, "Ты уже создал себе пикачу")

bot.infinity_polling(none_stop=True)


