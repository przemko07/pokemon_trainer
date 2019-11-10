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
        Print(
            [
                Where(
                    [
                        Option("gen", [GenFilter()]),
                        Option("local-id", [LocalIdFilter()]),
                        Option("global-id", [GlobalIdFilter()]),
                        Option("name", [NameFilter()]),
                        Option("type", [TypeFilter()]),
                        Option("alola", [AlolaFilter()]),
                    ]
                ),        
                #OrderBy(
                #    [
                #        NamedParameter("gen"),
                #        NamedParameter("local-id"),
                #        NamedParameter("global-id"),
                #        NamedParameter("name"),
                #        NamedParameter("type"),
                #    ]
                #)
            ]
        )#,
        #Option("counter-atack",
        #    [
        #        Option("gen:local-id", [PokemonLocalId()]),
        #        Option("global-id", [PokemonGlobalId()]),
        #        Option("name", [PokemonName()]),
        #        Option("type", [PokemonType()]),
        #    ]
        #),
        #Option("counter-def",
        #    [
        #        Option("gen:local-id", [PokemonLocalId()]),
        #        Option("global-id", [PokemonGlobalId()]),
        #        Option("name", [PokemonName()]),
        #        Option("type", [PokemonType()]),
        #    ]
        #),
        #Option("counter",
        #    [
        #        Option("gen:local-id", [PokemonLocalId()]),
        #        Option("global-id", [PokemonGlobalId()]),
        #        Option("name", [PokemonName()]),
        #        Option("type", [PokemonType()]),
        #    ]
        #),
    ]
)

read_database()

try:
    main.enter(sys.argv[1:])
except SubProgramException as e:
    print("Error:" + str(e))


#print ("Grass deals " + str(calculate_effectivness("Grass", "Dark") * 100) + "% dmg to Dark")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Water") * 100) + "% dmg to Water")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Steel") * 100) + "% dmg to Steel")