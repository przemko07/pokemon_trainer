from linq import *
from data import *
from logic import *

# http://smlweb.cpsc.ucalgary.ca/start.html
#
# LL lanugage
# print -> collection
# collection -> collection operation
#             | source
# source -> pokemonlist
#         | chartlist
# operation -> where filter
#            | orderby name
#            | first
#            | first filter
#            | take number
#            | skip number
# filter -> name equal value
# filter -> name not_equal value




class SubProgramException(Exception):
    pass


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


def MainProgramFactory(args):
    if (len(args) < 1):
        raise SubProgramException("Can't create Main factory, empty args")
    error = ""
    try:
        return PrintFactory(args)
    except SubProgramException as e:
        error = "\n" + str(e) if len(error) > 0 else str(e)
    raise SubProgramException(error)

def PrintFactory(args):
    if (len(args) < 1):
        raise SubProgramException("Can't create Print factory, empty args")
    if (args[0] == "print"): return Print([CollectionFactory(args[1:])])
    else:
        raise SubProgramException("Expecting argument (print)")    

def CollectionFactory(args):
    if (len(args) < 1):
        raise SubProgramException("Can't create Collection factory, empty args")
    if (args[0] == "where"): return Where([FilterFactory(args[1:])])
    elif (args[0] == "order-by"): return OrderBy([FilterFactory(args[1:])])
    else:
        raise SubProgramException("Expecting argument (where, order-by)")

#def WhereFactory(args):
#    if (len(args) < 2)
#        raise SubProgramException("Can't create Where factory, empty args")
#    if (args[0] != "where"):
#        raise SubProgramException("Expecting print argument")
#    try:
#        return Where([FilterFactory(args[1:])]
#    except SubProgramException as e:
#        raise SubProgramException("Can't create Where factory, FilterFactory exception") from e

#def OrderByFactory(args):
#    if (len(args) < 2)
#        raise SubProgramException("Can't create OrderBy factory, empty args")
#    if (args[0] != "order-by"):
#        raise SubProgramException("Expecting order-by argument")
#    error = ""
#    try:
#        program = GenFilterFactory(args[1:])
#    except SubProgramException as e:
#        error += "\n" + str(e) if len(error) > 0 else str(e)
#    try:
#        program = NameFilterFactory(args[1:])
#    except SubProgramException as e:
#        error += "\n" + str(e) if len(error) > 0 else str(e)
#    try:
#        program = TypeFilterFactory(args[1:])
#    except SubProgramException as e:
#        error += "\n" + str(e) if len(error) > 0 else str(e)    
#    if (len(error) > 0):
#        raise SubProgramException(error)
#    return Where([program])   

def FilterFactory(args):
    if (len(args) < 1):
        raise SubProgramException("Can't create Gen Filter factory, empty args")
    if (args[0] == "gen"): return Option("gen", [GenFilter()])
    elif (args[0] == "local-id"): return Option("local-id", [LocalIdFilter()])
    elif (args[0] == "global-id"): return Option("global-id", [GlobalIdFilter()])
    elif (args[0] == "name"): return Option("name", [NameFilter()])
    elif (args[0] == "type"): return Option("type", [TypeFilter()])
    elif (args[0] == "alola"): return Option("alola", [AlolaFilter()])
    else:
        raise SubProgramException("Expecting argument (gen, local-id, global-id, name, type, alola)")
    
















