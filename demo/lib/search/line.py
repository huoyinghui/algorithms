def line_search(arr, value):
    for index, v in enumerate(arr):
        if v == value:
            return index

    return -1

def bic_search(arr, value):
    low, hight = 0, len(arr)-1

    


def test_line_search():
    nums = [0, 2, 5, 8, 9]
    assert 0 ==  line_search(nums, 0)
    assert 1 ==  line_search(nums, 2)
    assert 2 ==  line_search(nums, 5)
    assert 3 ==  line_search(nums, 8)
    assert 4 ==  line_search(nums, 9)
    assert -1 ==  line_search(nums, 7)