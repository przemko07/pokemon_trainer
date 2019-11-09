from data import *
from linq import *

SUPER_EFFECTIVE = 1.6
NORMAL = 1.0
NOT_VERY_EFFECTIVE = 0.625
WEAK = 0.391

def calculate_effectivness(type_from, type_to):
    effectivness = Linq(all_effectivnesses).FirstOrNone(lambda x: x.type == type_from )
    if (effectivness == None):
        return NORMAL
    
    if (Linq(effectivness.super).contains(type_to)):
        return SUPER_EFFECTIVE
    elif (Linq(effectivness.not_very).contains(type_to)):
        return NOT_VERY_EFFECTIVE
    elif (Linq(effectivness.weak).contains(type_to)):
        return WEAK
    else:
        return NORMAL

        