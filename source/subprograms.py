from linq import *
from data import *
from logic import *


class SubProgramException(Exception):
    pass

class MainProgram:
    def __init__(self, actionProgram, collectionProgram)
        self.actionProgram = actionProgram
        self.collectionProgram = collectionProgram
    def enter(self):
        collection = self.collectionProgram.enter()
        self.actionProgram.enter(collection)

class ActionProgram:
    def __init__(self, name):
        self.name = name
    def enter(self, collection):
        if (name == "count"):
            print("count:" + str(len(item)))
        elif (name == None or name == "print"):
            for (item in collection):
                print(item)
            print("count:" + str(len(item)))
        else:
            raise SubProgramException("Action " + name + " not supported.")

class CollectionProgram:
    def __init__(self, sourceProgram, collectionProgram):
        self.sourceProgram = sourceProgram
        self.collection = collectionProgram
    def enter(self):
        # make logic for returning smth
        return [1, 2, 3]
        
class SourceProgram:
    def __init__(self, name):
        self.name = name
    def enter(self):
        if (name == "pokemonlist"):
            return all_pokemons
        elif (name == "chartlist"):
            # TODO: what should I return here?
            raise SubProgramException("I dont know what to do here")
        else:
            raise SubProgramException("Source " + name + " not supported.")

class MultiProgram:
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


class OrderBy(Option):
    def __init__(self, programs):
        super().__init__("order-by", programs)
    
    def enter(self, args):
        filter = super().enter(args)
        return Linq(all_pokemons).order_by(filter).collection


class Where(Option):
    def __init__(self, programs):
        super().__init__("where", programs)
    
    def enter(self, args):
        filter = super().enter(args)
        return Linq(all_pokemons).where(filter).collection


class NamedParameter(Option):
    def __init__(self, name):
        super().__init__("where", [NoneProgram()])
    
    def enter(self, args):
        super().enter(args)
        if (len(args) != 1):
            raise SubProgramException("Expecting named argument")
        return args[0]
        

class Print(Option):
    def __init__(self, programs):
        super().__init__("print", programs)
    
    def enter(self, args):
        value = super().enter(args)
        if (type(value) is list):
            for x in value:
                print(x)
            print("length:" + str(len(value)))
        else:
            print(value)

class GenFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting generation argument")
        return (lambda x: x.generation.startswith(args[0]))

class LocalIdFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting local_id argument")
        return (lambda x: x.local_id.startswith(args[0]))

class GlobalIdFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting global_id argument")
        return (lambda x: x.global_id.startswith(args[0]))

class NameFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting global_id argument")
        return (lambda x: x.name.startswith(args[0]))

class TypeFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting type argument")
        return (lambda x: Linq(x.types).any(lambda y: str(y).startswith(args[0])))

class AlolaFilter(SubProgram):
    def enter(self, args):
        if (len(args) != 1):
            raise SubProgramException("Expecting alola argument")
        return (lambda x: x.is_alola == bool(args[0]))

