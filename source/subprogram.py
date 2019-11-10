import sys


class SubProgram:
    def enter(self, args):
        pass


class MultiProgram(SubProgram):
    def __init__(self, programs):
        self.programs = programs        
        if (len(self.programs) == 0):
            raise Exception("Can't create MultiProgram with empty programs")

    def enter(self, args):
        error = ""
        for program in self.programs:
            try:
                return program.enter(args)
            except Exception as e:
                if (len(error) > 0):
                    error += "\n"
                error += str(e)
        raise Exception(error)

class Option(MultiProgram):
    def __init__(self, option, programs):
        self.option = option.strip()
        super().__init__(programs)        
        if (len(self.option) == 0):
            raise Exception("Can't create Option with empty option")

    def enter(self, args):
        if (len(args) == 0):
            raise Exception("Can't use option \"" + self.option + "\" when there are no arguments")
        if (self.option != args[0]):
            raise Exception("Can't use option \"" + self.option + "\" wrong argument \"" + args[0] + "\"")

        args = args[1:]
        error = ""
        for program in self.programs:
            try:
                return program.enter(args)
            except Exception as e:
                if (len(error) > 0):
                    error += "\n"
                error += str(e)
        raise Exception(error)

class Find(Option):
    def __init__(self, program):
        super().__init__("find", [program])
    
    def enter(self, args):
        filter = super().enter(args)    
        return Linq(all_pokemons).where(filter).collection

class Print(Option):
    def __init__(self, program):
        super().__init__("print", [program])
    
    def enter(self, args):
        value = super().enter(args)
        valueStr = str(value)
        print(valueStr)
        return valueStr

class GenFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting generation argument")
        return (lambda x: x.generation == args[0])

#class PokemonLocalId(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise Exception("Expecting local_id argument")
#        print("Searching for local id:\"" + args[0] + "\"")
#
#class PokemonGlobalId(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise Exception("Expecting global_id argument")
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
#            raise Exception("Expecting type argument")
#        print("Searching for type:\"" + args[0] + "\"")
#
#class PokemonAlola(SubProgram):
#    def enter(self, args):
#        if (len(args) != 1):
#            raise Exception("Expecting alola argument")
#        print("Searching for alola:\"" + args[0] + "\"")























