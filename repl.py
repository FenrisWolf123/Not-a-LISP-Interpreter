from lisp import interpret_line,variables

while True:
    line = input('lisp>>')
    if line == 'exit()':
        break
    elif line == 'var_heap()':
        print(variables)
        continue
    interpret_line(line)