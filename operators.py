import operator as op
import math

def logical_and(a, b):
    if a and b:
        return 1
    return 0

def logical_not(a):
    return not a

def logical_or(a, b):
    if a or b:
        return 1
    return 0

def lt(a,b):
    if a < b:
        return 1
    return 0

def gt(a,b):
    if a > b:
        return 1
    return 0

def lte(a,b):
    if a <= b:
        return 1
    return 0

def gte(a,b):
    if a >= b:
        return 1
    return 0

def null():
    pass

def equals(a, b):
    if a == b:
        return 1
    return 0

func = {
    '+': op.add,
    '-': op.sub,
    '*': op.mul,
    '/': op.truediv,
    '**': op.pow,
    '%': op.mod,
    '>': gt,
    '<': lt,
    '<=': lte,
    '>=': gte,
    '&&': logical_and,
    '||': logical_or,
    '!': logical_not, # unary
    '~': op.neg, # unary
    'sqrt': math.sqrt, # unary
    'floor': math.floor, # unary
    'ceil': math.ceil, # unary
    'def': null, 
    'if': null,  
    '=': null,
    '==': equals
}

unary = [
    '!',
    '~',
    'sqrt',
    'floor',
    'ceil',
]