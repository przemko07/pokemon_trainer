import sys

from data import * 
from data_reader import * 
from logic import * 
from subprogram import *


read_database()

try:
    args = sys.argv[1:]
    main = MainProgramFactory(args)
    main.enter(args)
except SubProgramException as e:
    print("Error:" + str(e))


#print ("Grass deals " + str(calculate_effectivness("Grass", "Dark") * 100) + "% dmg to Dark")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Water") * 100) + "% dmg to Water")
#print ("Grass deals " + str(calculate_effectivness("Grass", "Steel") * 100) + "% dmg to Steel")