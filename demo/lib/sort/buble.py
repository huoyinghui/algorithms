
def buble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                print('swap:', arr[j], arr[j+1], arr)
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def test_buble_sort():
    print('test')
    nums = [1, 5, 2, 9, 0]
    assert [0, 1, 2, 5, 9] == buble_sort(nums)
    # assert 0