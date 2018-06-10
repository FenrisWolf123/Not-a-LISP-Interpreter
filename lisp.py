from stack import Stack
from expression import tree
from operators import func, unary
# pylint: disable=E0401,E0602
from assert_error import *
from exceptions import *
number = (int, float)
variables = {}

def interpret_line(line):
    expr = [x for x in line.replace('(', ' ( ').replace(')', ' ) ').split(' ') if x != '']

    stack = Stack()

    def evaluate(arr):
        if isinstance(arr, number):
            return arr
        if isinstance(arr, str) and arr in variables.keys():
            return variables[arr]
        for i in reversed(arr):
            if isinstance(i, number):
                stack.push(i)
            elif isinstance(i, list):
                evaluate(i)
            elif isinstance(i, str):
                if i in variables.keys():
                    stack.push(variables[i])
                elif i == 'quote':
                    try:
                        assert_quote_check(arr)
                    except:
                        print('quote takes one argument')
                        return ''
                    else:
                        stack.push(stack.pop())
                        break
                elif i == 'zip':
                    array = []
                    if len(arr) > 1:
                        for i in arr[1:]:
                            array.append(i)
                    stack.push(array)
                    break
                elif i == '[]':
                    try:
                        if len(arr) != 3:
                            raise Exception
                        operand1 = stack.pop()
                        operand2 = stack.pop()
                        assert_array_access(operand1, operand2)
                        stack.push(operand2[operand1])
                        break
                    except:
                        print('Error')
                        return ''
                elif i == 'foreach':
                    pass
                elif i == 'def':
                    try:
                        assert_def_check(arr)
                        variables[arr[1]] = stack.pop()
                        stack.push(variables[arr[1]])
                        break
                    except IncorrectArgumentListError:
                        print('def takes only 2 arguments.')
                        return ''
                    except SemanticError:
                        print('def to be used like this: (def <var-name> <val>)')
                        return ''
                    except IdentifierNameClashError:
                        print(arr[1], 'is a reseved word.')
                        return ''
                    except BadIdentifierNameError:
                        print(arr[1], 'is not a valid identifier name.')
                        return '' 
                elif i == 'if':
                    try:
                        assert_if_check(arr)
                    except:
                        print('ERROR')
                        return ''
                    else:
                        if len(arr) == 3:
                            if stack.pop():
                                stack.push(stack.pop())
                            else:
                                stack.pop()
                                stack.push(0)
                        elif len(arr) == 4:
                            if stack.pop():
                                stack.push(stack.pop())
                            else:
                                stack.pop()
                                stack.push(stack.pop())
                        break
                elif i == '=':
                    try:
                        assert_assignment(arr, variables)
                    except:
                        print('ERROR')
                        return ''
                    else:
                        stack.pop()
                        variables[arr[1]] = stack.pop()

                        stack.push(variables[arr[1]])
                elif i in unary:
                    operator = func[i]
                    try:
                        assert_unary_len(arr)
                    except:
                        print('Unary operator', i, 'takes only 1 argument.')
                        return '\0'
                    else:
                        operand = stack.pop()
                        stack.push(operator(operand))
                        break
                elif i in func.keys():
                    operator = func[i]
                    try:
                        assert_binary_len(arr)
                    except:
                        print('Binary operator', i, 'takes only 2 arguments.')
                        return '\0'
                    else:
                        operand_1 = stack.pop()
                        operand_2 = stack.pop()
                        stack.push(operator(operand_1,operand_2))
                        break
                elif arr[0] != 'def' and arr[1] not in variables:
                    print('Unknown function/variable =>', i)
                    return ''

        return stack.peek()

    print(evaluate(tree(expr)))