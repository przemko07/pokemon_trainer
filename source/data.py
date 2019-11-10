from linq import *

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
        
    def __str__(self):
        global generation_padding
        global local_id_padding
        global global_id_padding
        global name_padding
        update_paddings()
        if (self.is_alola):
            return_format = "{name: <{name_padd}} alola {gen: <{gen_padd}}:{local_id: <{local_id_padd}} {global_id: <{global_id_padd}} {types}"
        else:
            return_format = "{name: <{name_padd}}       {gen: <{gen_padd}}:{local_id: <{local_id_padd}} {global_id: <{global_id_padd}} {types}"
                  
        return return_format.format(
            name = self.name,
            name_padd = name_padding,
            gen = self.generation,
            gen_padd = generation_padding,
            local_id = self.local_id,
            local_id_padd = local_id_padding,
            global_id = self.global_id,
            global_id_padd = global_id_padding,
            types = str(self.types)
        )
    

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


generation_padding = 1
local_id_padding = 1
global_id_padding = 1
name_padding = 1
last_update = -1
def update_paddings():
    global generation_padding
    global local_id_padding
    global global_id_padding
    global name_padding
    global last_update
    if (len(all_pokemons) > last_update):
        generation_padding = Linq(all_pokemons).max(lambda x: len(x.generation))
        local_id_padding = Linq(all_pokemons).max(lambda x: len(x.local_id))
        global_id_padding = Linq(all_pokemons).max(lambda x: len(x.global_id))
        name_padding = Linq(all_pokemons).max(lambda x: len(x.name))
        last_update = len(all_pokemons)
