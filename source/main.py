from data import * 
from data_reader import * 
from logic import * 


read_database()

print ("Grass deals " + str(calculate_effectivness("Grass", "Dark") * 100) + "% dmg to Dark")
print ("Grass deals " + str(calculate_effectivness("Grass", "Water") * 100) + "% dmg to Water")
print ("Grass deals " + str(calculate_effectivness("Grass", "Steel") * 100) + "% dmg to Steel")