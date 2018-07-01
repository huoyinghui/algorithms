from heapq import heappush, heappop


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
