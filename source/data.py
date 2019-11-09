######################################################
# Pokemon DataBase

# https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number
class Pokemon:
    def __init__(self, generation, local_id, global_id, name, types, is_alola):
        self.generation = generation
        self.local_id = local_id
        self.global_id = global_id
        self.name = name
        self.types = types
        self.is_alola = is_alola

# https://gamepress.gg/pokemongo/pokemon-go-type-chart
class Effectivness:
    def __init__(self, type, super, not_very, weak):
        self.type = type
        self.super = super
        self.not_very = not_very
        self.weak = weak

all_types = [
    "Bug", "Dark", "Dragon", "Electric", "Fairy", "Fighting",
    "Fire", "Flying", "Ghost", "Grass", "Ground", "Ice",
    "Normal", "Poison", "Psychic", "Rock", "Steel", "Water"
]
all_pokemons = []
all_effectivnesses = []
