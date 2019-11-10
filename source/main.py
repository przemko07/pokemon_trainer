import sys

from data import * 
from data_reader import * 
from logic import * 
from subprogram import *


#gen = PokemonGen()
#localId = PokemonLocalId()
#globalId = PokemonGlobalId()
#name = Option("name", [PokemonName()])
#type = PokemonType()
#alola = PokemonAlola()
#search = Search(gen, localId, globalId, name, type, alola)
#search = Option("search", [name, type])


main = MultiProgram(
    [
        Option("search",
            [
                Option("gen", [PokemonGen()]),
                Option("local-id", [PokemonLocalId()]),
                Option("global-id", [PokemonGlobalId()]),
                Option("name", [PokemonName()]),
                Option("type", [PokemonType()]),
                Option("alola", [PokemonAlola()]),
            ]
        ),
        Option("counter-atack",
            [
                Option("gen:local-id", [PokemonLocalId()]),
                Option("global-id", [PokemonGlobalId()]),
                Option("name", [PokemonName()]),
                Option("type", [PokemonType()]),
            ]
        ),
        Option("counter-def",
            [
                Option("gen:local-id", [PokemonLocalId()]),
                Option("global-id", [PokemonGlobalId()]),
                Option("name", [PokemonName()]),
                Option("type", [PokemonType()]),
            ]
        ),
        Option("counter",
            [
                Option("gen:local-id", [PokemonLocalId()]),
                Option("global-id", [PokemonGlobalId()]),
                Option("name", [PokemonName()]),
                Option("type", [PokemonType()]),
            ]
        ),
    ]
)

main.enter(sys.argv[1:])


#read_database()
#
#print ("Grass deals " + str(calculate_effectivness("Grass", "Dark") * 100) + "% dmg to Dark")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Water") * 100) + "% dmg to Water")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Steel") * 100) + "% dmg to Steel")