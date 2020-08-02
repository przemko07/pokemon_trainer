from grammar_dictionary import *
from parser import *
from subprograms import *
from Linq import *
#
# http://smlweb.cpsc.ucalgary.ca/start.html
#
# pokemonlist where gen equal gen1 orderby name
# print pokemonlist where name not equal diglet take 10
# count pokemonlist where name close4 bulba
#
# =============================== LL lanugage ================================
# MAIN -> ACTION COLLECTION.
# ACTION -> ACTION_NAME.
# COLLECTION -> COLLECTION OPERATION
#             | SOURCE.
# SOURCE -> SOURCE_NAME.
# OPERATION -> OPERATION OPERATION
#            | where FILTER
#            | orderby field
#            | take amount
#            | skip amount
#            | reverse.
# FILTER -> field AGREE OP value.
# AGREE -> AGREE_NAME.
# OP -> OP_NAME.
#

class GrammarException(Exception):
    pass

# ========================== LL TRANSFORM lanugage ===========================
# MAIN -> ACTION COLLECTION.
def MAIN(parser):
    actionProgram = ACTION(parser)
    collectionProgram = COLLECTION(parser)
    return MainProgram(actionProgram, collectionProgram)
# ACTION -> ACTION_NAME.
def ACTION(parser):
    value = parser.peek()
    if (Linq(ACTIONS).contains(value)):
        parser.move()
        return ActionProgram(name)
    else:
        return ActionProgram(None)
    
        
# COLLECTION -> SOURCE1 COLLECTION1.
def COLLECTION(parser):
    sourceProgram = SOURCE()
    collection1Program = COLLECTION1()
    return CollectionProgram(sourceProgram, collection1Program)

# COLLECTION1 -> OPERATION COLLECTION1
#              | .
def COLLECTION1(parser):
    value = parser.peek()
    # TODO: check if thats the correct behaviour of <dot>
    if (value != None):
        operationProgram = OPERATION(parser)
        collection1Program = COLLECTION1(parser)
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")

# SOURCE -> SOURCE_NAME.
def SOURCE1(parser):
    value = parser.peek()
    if (Linq(SOURCES).contains(value)):
        parser.move()
        return SourceProgram(value)
    else:
        return SourceProgram(None)

# OPERATION -> where FILTER OPERATION1
#            | orderby field OPERATION1
#            | take amount OPERATION1
#            | skip amount OPERATION1
#            | reverse OPERATION1.
def OPERATION(parser):
    value1 = parser.peek()
    if  (value1 == None):
        raise GrammarException("Expecting an operation " + OPERATIONS + ".")
    parser.move()
    if (value1 == OPERATION_WHERE):
        filterProgram = FILTER()
        operation1Program = OPERATION1()
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    elif (value1 == OPERATION_ORDERBY):
        value2 = parser.peek()
        if (value2 == None):
            raise GrammarException("Expecting a filed for " + OPERATION_ORDERBY + ".")
        parser.move()
        operation1Program = OPERATION1()
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    elif (value1 == OPERATION_TAKE):
        value2 = parser.peek()
        if (value2 == None):
            raise GrammarException("Expecting an ammount for " + OPERATION_TAKE + ".")
        parser.move()
        operation1Program = OPERATION1()
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    elif (value1 == OPERATION_SKIP):
        value2 = parser.peek()
        if (value2 == None):
            raise GrammarException("Expecting an ammount for " + OPERATION_SKIP + ".")
        parser.move()
        operation1Program = OPERATION1()
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    elif (value1 == OPERATION_REVERSE):
        operation1Program = OPERATION1()
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    else:
        raise GrammarException("Expecting an operation " + OPERATIONS + ".")

# OPERATION1 -> OPERATION OPERATION1
#             | .
def OPERATION1(parser):
    value = parser.peek()
    # TODO: check if thats the correct behaviour of <dot>
    if (value != None):
        operationProgram = OPERATION();
        operation1Program = OPERATION1();
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")
    else:
        # TODO: what to do next?
        raise GrammarException("Unknown behaviour")

# FILTER -> field AGREE OP value.
# AGREE18 -> AGREE_NAME.
# OP20 -> OP_NAME.
def OP20(parser):
    # TODO: USE ops
    value = parser.peek()
    if (value == "equal"):
        parser.move()
        return values
    elif (value == "contains"):
        parser.move()
        return values
    else:
        raise GrammarException("Not supported")
































































