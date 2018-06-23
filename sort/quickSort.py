#coding:utf-8

def quickSort(nums):
    if len(nums) < 2:
        return nums
    
    pos = nums[0]
    # less_list < pos < greater_list
    less_list = []
    greater_list = []

    # 如果出现重复元素，cnt++
    cnt = 1
    # 必须从1开始，不能保护0
    for i in nums[1:]:
        if i < pos:
            less_list.append(i)
        elif i == pos:
            # 记录重复元素
            cnt += 1
        else:
            greater_list.append(i)
    
    # print(less_list, greater_list)
    return quickSort(less_list) + [pos]*cnt + quickSort(greater_list)


def test_quickSort():
    nums = [2, 10, 5, 3, 3, 1, 9, 9]
    print('sorted:', quickSort(nums))
    assert sorted(nums) == quickSort(nums)


# log
# sort/quickSort.py('sorted:', [1, 2, 3, 3, 5, 9, 9, 10])
# 
# [2, 10, 5, 3, 3, 1, 9, 9]
# pos = 2
#     2
# 1                   10, 5, 3, 3, 9, 9
# 1 + 2 + 
#                     10
#           5,  3, 3        9, 9
#           5                     10
#     3, 3   []           9, 9  
#               cnt = 2
#     3
#   [] 3*2 []            [] 9*2 []
# 1 2 3 3  5              9 9 10
# 1,2,3,3,5,9,9,10
