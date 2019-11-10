import re

from data import * 
from linq import * 

def read_database():
    read_gens_csv()
    read_chart_csv("data/chart.csv")


def read_gens_csv():
    read_gen_csv("data/pokemons_gen1.csv")
    read_gen_csv("data/pokemons_gen2.csv")
    read_gen_csv("data/pokemons_gen3.csv")
    read_gen_csv("data/pokemons_gen4.csv")
    read_gen_csv("data/pokemons_gen5.csv")

def read_gen_csv(path):
    m = re.search("pokemons_([\\w]+).csv", path)
    if (m == None or m == False):
        raise Exception("Can't parse path to pokemon gen file, expected \"pokemons_([\\w]+).csv\" but got \"" + path + "\"")
        
    gen = m.group(1)
    try:
        file = open(path, "r")
    except Exception as e:
        raise Exception("Can't parse pokemon gen file \"" + path + "\"") from e
        
    lines = file.readlines()
    if (len(lines) == 0):
        raise Exception("Can't parse pokemon gen file \"" + path + "\" without a file header")
    # starting from 1 line, because 0 line is a header
    for line in lines[1:]:
        try:
            parse_gen_line_csv(gen, line)
        except Exception as e:
            raise Exception("Can't parse pokemon gen file \"" + path + "\"") from e
    
def parse_gen_line_csv(gen, line):
    v = line.split("\t")
    if (len(v) < 5):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", expecting at least 4 columns")
    
    local_id = v[0]
    global_id = v[1]
    name = v[2]
    types = Linq(v[4:]).select(lambda x: x.strip()).collection
    
    m = re.search("[A-Z][a-z]+", name)
    if (m == None or m == False):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", expected name in format [A-Z][a-z], but got \"" + name + "\"")

    wrong_types = Linq(types).where(lambda x: not Linq(all_types).contains(x))
    if (len(wrong_types)):
        raise Exception("Can't parse pokemon gen file line \"" +  line + "\", wrong type of pokemon, \"" + wrong_types + "\"")

    exist_name = Linq(all_pokemons).any(lambda x: x.name == name)
    exist_local_id = Linq(all_pokemons).where(lambda x: x.generation == gen).any(lambda x: x.local_id == local_id) if local_id != " " else False
    exist_global_id = Linq(all_pokemons).any(lambda x: x.global_id == global_id) if global_id != " " else False

    is_alola = exist_name and (exist_local_id or exist_global_id)
    
    if (not is_alola):
        if (exist_local_id):
            raise Exception("Can't parse pokemon gen file line \"" + line + "\", local_id doubled \"" + local_id + "\"")

        if (exist_global_id):
            raise Exception("Can't parse pokemon gen file line \"" + line + "\", global_id doubled \"" + global_id + "\"")

        if (exist_name):
            raise Exception("Can't parse pokemon gen file line \"" + line + "\", name doubled \"" + name + "\"")

    if (len(global_id.strip()) == 0):
        raise Exception("Can't parse pokemon gen file line \"" + line + "\", global_id is empty")
    
    all_pokemons.append(Pokemon(gen, local_id, global_id, name, types, is_alola))


def read_chart_csv(path):
    try:
        file = open(path, "r")
    except Exception as e:
        raise Exception("Can't parse pokemon chart file \"" + path + "\"") from e
    lines = file.readlines()
    if (len(lines) == 0):
        raise Exception("Can't parse pokemon chart file \"" + path + "\"  without file header")
    # starting from 1 line, because 0 lien is a header
    for line in lines[1:]:
        try:
            parse_chart_line_csv(line)
        except Exception as e:
            raise Exception("Can't parse pokemon chart file \"" + path + "\"") from e

def parse_chart_line_csv(line):
    values = line.split("\t")
    if (len(values) == 0):
        raise Exception("Can't prase pokemon chart line \"" + line + "\", line can't be empty")
    
    if (len(values) > 4):
        raise Exception("Can't prase pokemon chart line \"" + line + "\", expecting columns 1-4")
    
    type = values[0]
    super = values[1].split(" ") if len(values) >= 2 else []
    not_very = values[2].split(" ") if len(values) >= 3 else []
    weak = values[3].split(" ") if len(values) == 4 else []
    
    type = type.strip()
    super = Linq(super).select(lambda x: x.strip()).where(lambda x: len(x) > 0).collection
    not_very = Linq(not_very).select(lambda x: x.strip()).where(lambda x: len(x) > 0).collection
    weak = Linq(weak).select(lambda x: x.strip()).where(lambda x: len(x) > 0).collection
    
    if (Linq(all_effectivnesses).any(lambda x: x.type == type)):
        raise Exception("Can't parse pokemon chart line \"" + line + "\", type \"" + type + "\" already added")
    
    is_wrong_type = not Linq(all_types).contains(type)
    if (is_wrong_type):
        raise Exception("Can't parse pokemon chart line \"" +  line + "\", wrong type of pokemon, \"" + type + "\"")

    wrong_types = Linq(super).where(lambda x: not Linq(all_types).contains(x))
    if (len(wrong_types)):
        raise Exception("Can't parse pokemon gen file line \"" +  line + "\", wrong super effective type of pokemon, \"" + wrong_types + "\"")

    wrong_types = Linq(not_very).where(lambda x: not Linq(all_types).contains(x))
    if (len(wrong_types)):
        raise Exception("Can't parse pokemon gen file line \"" +  line + "\", wrong not very effective type of pokemon, \"" + wrong_types + "\"")

    wrong_types = Linq(weak).where(lambda x: not Linq(all_types).contains(x))
    if (len(wrong_types)):
        raise Exception("Can't parse pokemon gen file line \"" +  line + "\", wrong weak type of pokemon, \"" + wrong_types + "\"")

    all_effectivnesses.append(Effectivness(type, super, not_very, weak))


