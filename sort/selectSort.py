def selectSort(nums):
    """
    for i in range(len(nums)):
        min_index = i
        #从第i+1个， 找出元素中最小的下标
        for j in range(i+1, len(nums[i:]):
            if nums[j] < nums[i]:
                min_index = j
        # 与最小的值交换位置.
        nums[i], nums[min_index] = nums[min_index], nums[i]
    """
    for i in range(len(nums)):
        min_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        # 与交换最小值
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def test_selectSort():
    nums = [3, 5, 1, 2]
    assert sorted(nums) == selectSort(nums)
    pass
