def tree(arr):
    if not len(arr):
        raise Exception

    token = arr.pop(0)

    if token == '(':
        res = []

        while arr[0] != ')':
            res.append(tree(arr))

        arr.pop(0)

        return res

    elif token == ')':
        raise Exception
    else:
        return atomize(token)

def atomize(token):
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            return str(token)