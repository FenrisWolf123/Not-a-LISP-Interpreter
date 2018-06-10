class Stack:
    def __init__(self, iterable=[]):
        self._stack = []
        if iterable != []:
            while iterable != []:
                self.push(iterable.pop(0))
    
    def __str__(self):
        return str(self._stack)
    
    def pop(self):
        return self._stack.pop()

    def is_empty(self):
        return self._stack == []

    def push(self, data):
        self._stack.append(data)

    def peek(self):
        return self._stack[-1]

    def __len__(self):
        return len(self._stack)

if __name__ == '__main__':
    x = Stack([1,2,3,4,5])
    
    n = int(input())
    for _ in range(n):
        x.push(int(input()))

    print(x)

    for _ in range(len(x)):
        print(x.pop())

    print(x.is_empty())