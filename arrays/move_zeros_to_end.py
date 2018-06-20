"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.
    move_zeros([false, 1, 0, 1, 2, 0, 1, 3, "a"])
    returns => [false, 1, 1, 2, 1, 3, "a", 0, 0]

The time complexity of the below algorithm is O(n).
"""


def move_zeros(array):
    result = []
    zeros = 0

    for i in array:
        if i is 0:  # not using `not i` to avoid `False`, `[]`, etc.
            zeros += 1
        else:
            result.append(i)
    result.extend([0] * zeros)
    return result


def move_zeros_v2(array=None):
    """
    Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
    :param array:List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    :return: array
    """
    if not array:
        return None

    for item in array:
        if item == 0:
            array.remove(item)
            array.append(item)
    return array


def main():
    nums = [0, 1, 0, 3, 12]
    move_zeros_v2(nums)
    print(nums)

if __name__ == '__main__':
    main()
