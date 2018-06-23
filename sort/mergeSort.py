#coding:utf-8

def mergeList(left, right):
    """
    合并两个有序列表
    """
    assert sorted(left) == left
    assert sorted(right) == right

    return sorted(left+right)

def mergeSort(nums):
    """
    1.分治
    2.合并, 两个有序list
    """
    if len(nums) <= 2:
        return [min(nums), max(nums)]

    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return  mergeList(left, right)


def test_mergeSort():
    nums = [10, 4, 6, 3, 8, 2, 5, 7]
    assert sorted(nums) == mergeSort(nums)
