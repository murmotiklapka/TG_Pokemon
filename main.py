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
        bot.send_message(message.chat.id, 'вы можете подлеить покемона командой /heal')
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=['pikachu'])
def pikachu(message):
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

@bot.message_handler(commands=['heal'])
def heal(message):
    global pokemon
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
            bot.send_message(message.chat.id, f'У вашего покемона нет бонуса для лечения. У него {pokemon.hp} хп. Для получения бонуса выйграйте бой')

bot.infinity_polling(none_stop=True)

