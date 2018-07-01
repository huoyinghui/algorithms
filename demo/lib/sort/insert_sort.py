def insert_sort(nums):
    """
    假设第一个有序，一次插入到有序列表
    """
    n = len(nums)

    for i in range(1, n):
        v = nums[i]
        pos = i
        while pos > 0 and v < nums[pos-1]:
            nums[pos] = nums[pos-1]
            pos -= 1

        nums[pos] = v
        pass
    return nums
    

def test_select_sort():
    print('test')
    nums = [1, 5, 2, 9, 0]
    assert [0, 1, 2, 5, 9] == insert_sort(nums)
    assert 1
