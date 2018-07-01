def select_sort(arr):
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                print('min:', min_index, arr[min_index])

        arr[i], arr[min_index] = arr[min_index], arr[i]
        print('change:', arr)

    return arr

def test_select_sort():
    print('test')
    nums = [1, 5, 2, 9, 0]
    assert [0, 1, 2, 5, 9] == select_sort(nums)
    assert 1
