from stack import Stack

def check_brackets(arr):
    brackets = Stack()
    for ch in arr:
        if ch == '(':
            brackets.push(ch)
        elif ch == ')':
            if brackets.is_empty():
                return False
            else:
                brackets.pop()

    if brackets.is_empty():
        return True
    else:
        return False