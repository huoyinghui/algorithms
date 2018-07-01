from heapq import heappush, heappop, heapify


class SmallHeap:
    def init(self):
        self.arr = list()

    def heap_insert(self, val):
        heappush(self.arr, val)

    def heapify(self):
        heapify(self.arr)

    def heap_pop(self):
        return heappop(self.arr)

    def get_top(self):
        if not self.arr:
            return
        return self.arr[0]

class BigHeap:
    def __init__(self):
        self.arr = list()

    def heap_insert(self, val):
        heappush(self.arr, (-val[0], val[1]))

    def heapify(self):
        heapify(self.arr)

    def heap_pop(self):
        # return -heappop(self.arr)
        entry = heappop(self.arr)
        return -entry[0], entry[1]

    def get_top(self):
        if not self.arr:
            return
        return -self.arr[0]

    def __len__(self):
        return len(self.arr)

class PriorityQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        # self._maxheap = [(0,'')]*maxsize
        self._maxheap = BigHeap()

    def push(self, priority, value):
        # 注意这里把这个 tuple push 进去，python 比较 tuple 从第一个开始比较
        # 这样就很巧妙地实现了按照优先级排序
        entry = (priority, value)    # 入队的时候会根据 priority 维持堆的特性
        self._maxheap.heap_insert(entry)

    def pop(self, with_priority=False):
        # entry = heappop(self._maxheap)
        entry = self._maxheap.heap_pop()
        if with_priority:
            return entry
        else:
            return entry[1]

    def is_empty(self):
        return len(self._maxheap) == 0


def heap_sort(nums):
    heap = []
    for item in nums:
        heappush(heap, item)

    order_heap = []
    while heap:
        order_heap.append(heappop(heap))

    return order_heap


def test_heap_sort():
    data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]

    assert sorted(data[:]) == heap_sort(data)


def test_priorityqueue():
    size = 5
    pq = PriorityQueue(size)
    pq.push(5, 'purple')    # priority, value
    pq.push(0, 'white')
    pq.push(3, 'orange')
    pq.push(1, 'black')

    res = []
    while not pq.is_empty():
        res.append(pq.pop())
    print(res)
    assert res == ['purple', 'orange', 'black', 'white']
    assert 1
