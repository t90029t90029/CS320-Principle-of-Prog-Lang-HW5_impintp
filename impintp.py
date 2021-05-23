# Imp interpreter
#
# Usage: linux> ./python3 impintp.py 
#        ...<type input here>...
#        ^D
#

# Imp - an imperative expression language:
#
#   Expr -> num                   # integer    
#        |  var                   # string 
#        |  (Op Expr Expr)        # binop     
#        |  (:= var Expr)         # assign     
#        |  (print Expr)          # output     
#        |  (seq Expr Expr)       # sequence      
#        |  (if Expr Expr Expr)   # if-stmt    
#        |  (while Expr Expr)     # while-loop  
#   Op   -> + | - | * | / | < | =
#
#   Name : Shang Chun, Lin
import sys
from sexpr import *

vars = {}    # variable store

# Interpret function
# - e is an Imp program in nested list form
def eval(e):
    # e is an atom
    if type(e) is str:
        if e.isdigit():
            return int(e)
        if e not in vars :
            vars[e] = 0
        return vars[e]
    # e is a list
    assert type(e) is list, "Invalid exp form " + str(e)
    key = e[0]
    # bin-op (op e1 e2)
    if   key == '+': v = eval(e[1]) + eval(e[2])
    elif key == '-': v = eval(e[1]) - eval(e[2])
    elif key == '*': v = eval(e[1]) * eval(e[2])
    elif key == '/': v = eval(e[1]) // eval(e[2])
    elif key == '<': v = eval(e[1]) < eval(e[2])
    elif key == '=': v = eval(e[1]) == eval(e[2])
    # assign (:= x e)
    elif key == ':=': 
        assert type(e[1]) is str, "Invalid assign " + str(e)
        v = eval(e[2])
        vars[e[1]] = v
    # output (print e)
    elif key == 'print':
        v = eval(e[1])
        print(v)
    # sequence (seq e1 e2)
    elif key == 'seq': 
        eval(e[1])
        v = eval(e[2])
    # if-stmt (if c t f)
    elif key == 'if':
        if eval(e[1]) :
            v = eval(e[2])
        else:
            v = eval(e[3])
    # while-loop (while c b)
    elif key == 'while': 
        if eval(e[1]):
            eval(e[2])
            eval(e)
        v = 0
    else:
        raise Exception("Illegal exp: " + str(e))
    return v

if __name__ == "__main__":
    prog = sys.stdin.read()
    lst = sexpr(prog)
    print("result:", eval(lst))
