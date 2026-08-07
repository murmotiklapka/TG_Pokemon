from random import randint
import requests

class Pokemon:
    pokemons = {}

    def __init__(self, pokemon_trainer, maxhp = randint(1,100), power = randint(1,100), pokemon_number = randint(1,1025)):
        self.bonus = 0
        self.hp = maxhp
        self.maxhp = maxhp
        self.power = power   
        self.pokemon_number = pokemon_number
        self.pokemon_trainer = pokemon_trainer
        self.link = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'

        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.animation = self.get_animation()

        Pokemon.pokemons[pokemon_trainer] = self

    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chense = randint(1,100)
            if chense <= 20:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            self.bonus += self.hp * 0.5
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        
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

    def info(self):
        return f"Имя твоего покеомона: {self.name}. Абилка твоего покеомона: {self.ability}.\nХп покемона: {self.hp}. Сила покемона: {self.power}.\nБонус покемона: {self.bonus}. У тебя класс {self.__class__.__name__}"
    def show_img(self):
        return self.img
    def show_nummber(self):
        return f'Номмер: {self.pokemon_number}'
    def show_animation(self):
        return self.get_animation
    def show_link(self):
        return self.link
    def show_animation(self):
            return self.animation

class Wizard(Pokemon):
    def __init__(self, username):
        super().__init__(username)
        self.maxhp = randint(1, 200)
        self.hp = self.maxhp

class Fighter(Pokemon):
    def __init__(self, username):
        super().__init__(username)
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nБоец применил супер-атаку силой:{super_power} "

if __name__ == "__main__":
    pokemon = Pokemon("Ilya")
    wizard = Wizard("Ilya K")
    fighter = Fighter("Ilya Kamyshnikov")

    pokemon.info()
    wizard.info()
    fighter.info()

    print(wizard.attack(fighter))
    print(pokemon.attack(wizard))
    print(fighter.attack(wizard))


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
