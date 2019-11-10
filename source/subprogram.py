class SubProgram:
    def enter(self, args):
        return False


class MultiProgram(SubProgram):
    def __init__(self, programs):
        self.programs = programs        
        if (len(self.programs) == 0):
            raise Exception("Can't create MultiProgram with empty programs")

    def enter(self, args):
        for program in self.programs:
            if (program.enter(args)):
                return True
        return False

class Option(MultiProgram):
    def __init__(self, option, programs):
        self.option = option.strip()
        super().__init__(programs)        
        if (len(self.option) == 0):
            raise Exception("Can't create Option with empty option")

    def enter(self, args):
        if (len(args) == 0):
            return False
        if (self.option != args[0]):
            return False

        if (len(self.programs) > 0):
            if (len(args) == 1):
                return False
            args = args[1:]
            for program in self.programs:
                if (program.enter(args)):
                    return True
        return False

class SearchPokemon(Option):
    def __init__(self, program):
        super().__init__("search", [program])
    
    def enter(self, args):
        if (len(args) == 0)
            raise Exception("Expecting search argument")
    
        Linq(all_pokemons).where(self.program(args)

class PokemonGen(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting generation argument")
        print("Searching for gen:\"" + args[0] + "\"")

class PokemonLocalId(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting local_id argument")
        print("Searching for local id:\"" + args[0] + "\"")

class PokemonGlobalId(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting global_id argument")
        print("Searching for global id:\"" + args[0] + "\"")

class PokemonName(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            return False
        print("Searching for name:\"" + args[0] + "\"")

class PokemonType(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting type argument")
        print("Searching for type:\"" + args[0] + "\"")

class PokemonAlola(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise Exception("Expecting alola argument")
        print("Searching for alola:\"" + args[0] + "\"")























