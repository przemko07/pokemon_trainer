import re

from data import * 
from linq import * 

def read_database():
    read_gens_csv()
    read_chart_csv()


def read_gens_csv():
    read_gen_csv("data/pokemons_gen1.csv")
    read_gen_csv("data/pokemons_gen2.csv")
    read_gen_csv("data/pokemons_gen3.csv")
    read_gen_csv("data/pokemons_gen4.csv")
    read_gen_csv("data/pokemons_gen5.csv")

def read_gen_csv(path):
    m = re.search("pokemons_([\\w\\d]+).csv", path)
    if (m == None or m == False):
        raise Exception("Can't parse path to pokemon gen file, expected \"pokemons_([\w\d]+).csv\" but got \"" + path + "\"")
        
    gen = m.group(1)
    try:
        file = open(path, "r")
    except Exception as e:
        raise Exception("Can't parse pokemon gen file \"" + path + "\"") from e
        
    lines = file.readlines()
    if (len(lines) == 0):
        raise Exception("Can't parse pokemon gen file \"" + path + "\" without a header")
    # starting from 1 line, because 0 line is a header
    for line in lines[1:]:
        try:
            parse_gen_line_csv(gen, line)
        except Exception as e:
            raise ValueError("Can't parse pokemon gen file \"" + path + "\"") from e
    
def parse_gen_line_csv(gen, line):
    v = line.split("\t")
    if (len(v) < 4):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", expecting at least 4 columns")
    local_id = v[0]
    global_id = v[1]
    name = v[2]
    types = v[3:]

    exist_local_id = Linq(all_pokemons).where(lambda x: x.generation == gen).any(lambda x: x.local_id == local_id)
    if (exist_local_id):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", local_id doubled \"" + local_id + "\"")

    exist_global_id = Linq(all_pokemons).any(lambda x: x.global_id == global_id)
    if (exist_global_id):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", global_id doubled \"" + global_id + "\"")

    m = re.match("\\W\\w+", name)
    if (m == None or m == False):
        return Exception("Can't parse pokemon gen file line \"" + line + "\", expected name in format \\W\\w+, but got \"" + name + "\"")

    wrong_types = Linq(types).where(lambda x: not Linq(all_types).contains(x))
        
    if (len(wrong_types)):
        return Exception("Can't parse pokemon gen file line \"" +  line + "\", wrong type of pokemon, \"" + wrong_types + "\"")

    all_pokemons.append(Pokemon(gen, local_id, global_id, name, types))


def read_chart_csv():
    file = open("data/chart.csv", "r")
    lines = file.readlines()
    # starting from 1 line, because 0 lien is a header
    for line in lines[1:]:
        parse_chart_line_csv(line)
        
def parse_chart_line_csv(line):
    v = line.split("\t")
    type = v[0]
    super = v[1].split(" ")
    not_very = v[2].split(" ")
    weak = v[3].split(" ")
    all_effectivnesses.append(Effectivness(type, super, not_very, weak))


