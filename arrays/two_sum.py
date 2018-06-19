"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""


def two_sum(array, target):
    dic = {}
    for i, num in enumerate(array):
        if num in dic:
            return dic[num], i
        else:
            dic[target - num] = i
    return None


def two_sum_v2(array, target):
    target_dict = {}

    for index, item in enumerate(array):
        other_numb = target - item
        if other_numb in target_dict:
            return target_dict[other_numb], index
        else:
            target_dict[item] = index
    return None


def main():
    nums = [2, 7, 11, 15]
    target = 17
    # ret = two_sum(nums, target)
    ret = two_sum_v2(nums, target)
    print(ret)


if __name__ == '__main__':
    main()