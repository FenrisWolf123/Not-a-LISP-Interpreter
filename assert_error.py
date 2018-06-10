import re
from operators import func
from exceptions import * 

# pylint: disable=E0702 
def assert_unary_len(arr):
    if len(arr) != 2:
        raise 0
    pass

def assert_binary_len(arr): 
    if len(arr) != 3:
        raise 0
    pass

def assert_def_check(arr):
    if len(arr) != 3:
        raise IncorrectArgumentListError # not correct number of arguments
    elif isinstance(arr[1], (int, float)):
        raise SemanticError # value first
    elif arr[1] in list(func.keys()):
        raise IdentifierNameClashError # reserved word
    elif not re.match(r'[_a-zA-Z][_a-zA-Z0-9]*', arr[1]):
        raise BadIdentifierNameError # bad identifier name
    pass

def assert_if_check(arr):
    if len(arr) != 4: 
        if len(arr) != 3:
            raise 0
    pass

def assert_quote_check(arr):
    if len(arr) != 2:
        raise 0
    pass

def assert_assignment(arr, variables):
    if len(arr) != 3:
        raise IncorrectArgumentListError
    elif not isinstance(arr[1], str):
        raise SemanticError
    elif isinstance(arr[2], (int, float)):
        if arr[1] not in variables.keys():
            raise UnknownVariableError
    elif arr[1] not in variables.keys() and arr[2] not in variables.keys():
        raise UnknownVariableError
    pass

def assert_array_access(op1, op2):
    if not isinstance(op1, (int, float)):
        raise IncorrectArgumentListError
    elif not isinstance(op2, list):
        raise IncorrectArgumentListError 
    pass