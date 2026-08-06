from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer, pokemon_number = randint(1,1326)):
        self.pokemon_number = pokemon_number
        self.pokemon_trainer = pokemon_trainer   
        self.link = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'

        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.animation = self.get_animation()

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = self.link
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['versions']['generation-vii']['ultra-sun-ultra-moon']['front_default'])
        else:
            return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-vii/ultra-sun-ultra-moon/2.png"

    def get_animation(self):
            url = self.link
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                return (data['sprites']['versions']['generation-v']['black-white']['animated']['front_default'])
            else:
                return "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/versions/generation-v/black-white/animated/shiny/2.gif"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = self.link
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    def get_ability(self):
        url = self.link
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            ability_names = [data['abilities'][0]['ability']['name']]
            return ability_names
        else:
            return "Unknown Ability"
    
    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}. Абилка твоего покеомона: {self.ability}."

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img

    def show_nummber(self):
        return self.pokemon_number

    def show_animation(self):
        return self.pokemon_number

    def show_link(self):
        return self.link

    def show_animation(self):
            return self.animation

pokemon = Pokemon("...")

print('')
print(f'основная инфа( {pokemon.info()} )\n ')
print(f'ссылка: {pokemon.show_link()}\n ')
print(f'картинка: {pokemon.show_img()}\n ')
print(f'Номер: {pokemon.show_nummber()}\n ')
print(f'анимацыя: {pokemon.show_animation()}\n ')


pikachu = Pokemon("...", 25)

print('')
print(f'основная инфа( {pikachu.info()} )\n ')
print(f'ссылка: {pikachu.show_link()}\n ')
print(f'картинка: {pikachu.show_img()}\n ')
print(f'Номер: {pikachu.show_nummber()}\n ')
print(f'анимацыя: {pikachu.show_animation()}\n ')
