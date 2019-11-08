from data import * 
from data_reader import * 
from logic import * 

read_database()

efc = calculate_effectivness("Grass", "Dark")

print ("Grass deals " + (efc * 100) + "% dmg to Dark")