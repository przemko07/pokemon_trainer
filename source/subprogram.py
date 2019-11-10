from linq import *
from data import *
from logic import *

class SubProgramException(Exception):
    pass


class SubProgram:
    def enter(self, args):
        pass


class MultiProgram(SubProgram):
    def __init__(self, programs):
        self.programs = programs        
        if (len(self.programs) == 0):
            raise SubProgramException("Can't create MultiProgram with empty programs")

    def enter(self, args):
        error = ""
        for program in self.programs:
            try:
                return program.enter(args)
            except SubProgramException as e:
                if (len(error) > 0):
                    error += "\n"
                error += str(e)
        raise SubProgramException(error)

class Option(MultiProgram):
    def __init__(self, option, programs):
        self.option = option.strip()
        super().__init__(programs)        
        if (len(self.option) == 0):
            raise SubProgramException("Can't create Option with empty option")

    def enter(self, args):
        if (len(args) == 0):
            raise SubProgramException("Can't use option \"" + self.option + "\" when there are no arguments")
        if (self.option != args[0]):
            raise SubProgramException("Can't use option \"" + self.option + "\" wrong argument \"" + args[0] + "\"")
        return super().enter(args[1:])

class Find(Option):
    def __init__(self, programs):
        super().__init__("find", programs)
    
    def enter(self, args):
        filter = super().enter(args)
        return Linq(all_pokemons).where(filter).collection

class Print(Option):
    def __init__(self, programs):
        super().__init__("print", programs)
    
    def enter(self, args):
        value = super().enter(args)
        if (type(value) is list):
            for x in value:
                print(x)
        else:
            print(value)
        return None

class GenFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting generation argument")
        return (lambda x: x.generation == args[0])

#class PokemonLocalId(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise SubProgramException("Expecting local_id argument")
#        print("Searching for local id:\"" + args[0] + "\"")
#
#class PokemonGlobalId(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise SubProgramException("Expecting global_id argument")
#        print("Searching for global id:\"" + args[0] + "\"")
#
#class PokemonName(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            return False
#        print("Searching for name:\"" + args[0] + "\"")
#
#class PokemonType(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise SubProgramException("Expecting type argument")
#        print("Searching for type:\"" + args[0] + "\"")
#
#class PokemonAlola(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise SubProgramException("Expecting alola argument")
#        print("Searching for alola:\"" + args[0] + "\"")























