from parser import *
from subprograms import *
#
# http://smlweb.cpsc.ucalgary.ca/start.html
#
# pokemonlist where gen equal gen1 orderby name
# pokemonlist where name not equal diglet take 10
# counter pokemonlist where name close4 bulba
#
# =============================== LL lanugage ================================
# MAIN -> ACTION COLLECTION.
# ACTION -> counter
#         | .
# COLLECTION -> COLLECTION OPERATION
#             | SOURCE.
# SOURCE -> pokemonlist
#         | chartlist.
# OPERATION -> OPERATION OPERATION
#            | where FILTER
#            | orderby field
#            | take amount
#            | skip amount
#            | reverse.
# FILTER -> field AGREE OP value.
# AGREE -> not
#        | .
# OP -> equal
#     | contains
#     | greater
#     | less
#     | start_with
#     | end_with
#     | close1
#     | close2
#     | close3
#     | close4
#     | close5
#     | close6
#     | close7
#     | close8
#     | close9.
#
#
#

class GrammarException(Exception):
    pass

# ========================== LL TRANSFORM lanugage ===========================
# MAIN0 -> ACTION0 COLLECTION1.
def MAIN0(parser):
    action = ACTION0(parser)
    collection = COLLECTION1(parser)
# ACTION0 -> counter
#          |.
def ACTION0(parser):
    value = parser.peek()
    if (value == None):
        raise GrammarException("Not supported")
    if (value == "counter"):
        return Action(true)
    else:
        return Action(false)
# COLLECTION1 -> SOURCE1 COLLECTION2.
def COLLECTION1(parser):
    source = SOURCE1()
    collection = COLLECTION2()
# COLLECTION2 -> OPERATION5 COLLECTION2
#              |.
# SOURCE1 -> pokemonlist
#          | chartlist.
# OPERATION5 -> where FILTER9 OPERATION6
#             | orderby field OPERATION6
#             | take amount OPERATION6
#             | skip amount OPERATION6
#             | reverse OPERATION6.
# OPERATION6 -> OPERATION8 OPERATION6
#             |.
# OPERATION8 -> where FILTER9 OPERATION9
#             | orderby field OPERATION9
#             | take amount OPERATION9
#             | skip amount OPERATION9
#             | reverse OPERATION9.
# OPERATION9 -> OPERATION19 OPERATION9
#             |.
# FILTER9 -> field AGREE18 OP20 value.
# AGREE18 -> not
#          |.
# OPERATION19 -> where FILTER9 OPERATION20
#              | orderby field OPERATION20
#              | take amount OPERATION20
#              | skip amount OPERATION20
#              | reverse OPERATION20 .
# OPERATION20 -> OPERATION19 OPERATION20
#              |.
# OP20 -> equal
#       | contains
#       | greater
#       | less
#       | start_with
#       | end_with
#       | close1
#       | close2
#       | close3
#       | close4
#       | close5
#       | close6
#       | close7
#       | close8
#       | close9.
#



