#coding:utf-8

def mergeList(left, right):
    """
    合并两个有序列表
    """
    assert sorted(left) == left
    assert sorted(right) == right

    ret = []
    index_left = 0
    idnex_right = 0

    while index_left < len(left) and idnex_right < len(right):
        min_value = left[index_left]
        if left[index_left] < right[idnex_right]:
            index_left += 1
        else:
            min_value = right[idnex_right]
            idnex_right += 1
        ret.append(min_value)
    # left
    if index_left < len(left):
        ret.extend(left[index_left:])
    
    if idnex_right < len(right):
        ret.extend(right[idnex_right:])

    print(ret, index_left, idnex_right, left, right)
    return ret
    # return sorted(left+right)

def mergeSort(nums):
    """
    1.分治
    2.合并, 两个有序list
    """
    if len(nums) <= 1:
        # return [min(nums), max(nums)]
        return nums

    mid = len(nums)//2
    left = mergeSort(nums[:mid])
    right = mergeSort(nums[mid:])

    return  mergeList(left, right)


def test_mergeSort():
    nums = [10, 4, 6, 3, 8, 2, 5, 7]
    assert sorted(nums) == mergeSort(nums)
