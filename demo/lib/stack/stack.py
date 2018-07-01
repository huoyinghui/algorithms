from collections import deque


class Stack(object):
    
    def __init__(self):
        self._deque = deque()

    def push(self, value):
        self._deque.append(value)

    def pop(self):
        return self._deque.pop()
    
    def is_empty(self):
        return len(self._deque) == 0

def test_print_nums_use_stask():
    s = Stack()
    n = 3
    while n > 0:
        s.push(n)
        n -= 1
    
    while not s.is_empty():
        print(s.pop())



def hanoi_move(n, src, dest, tmp):
    if n < 1:
        return

    # src, tmp, 
    hanoi_move(n-1, src, tmp, dest) 
    print('n:{} Move {} -> {}'.format(n, src, dest))
    hanoi_move(n-1, tmp, dest, src)

def test_hanoi():
    print('test_hanoi')
    hanoi_move(2, 'A', 'B', 'C')

    

def test_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    assert 3 == s.pop()
    assert 2 == s.pop()
    assert 1 == s.pop()


def main():
    pass

if __name__ == '__main__':
    main()