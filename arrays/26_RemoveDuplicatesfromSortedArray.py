class Solution:
    """
    1.结果是，不重复元素依次放入到nums
    2.当前元素,
        不重复，放入到nums中，index++
        重复，不需要操作，遍历下一个.
    3.
    """
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp_dict = {}
        index = 0
        for i in range(len(nums)):
            if nums[i] not in tmp_dict:
                # print('index:', index, 'i:', i, 'add :', nums[i])
                nums[index] = nums[i]
                index += 1
                tmp_dict[nums[i]] = True
        nums[:] = nums[:index]
        # print(nums)
        return nums


def test_removeDuplicates():
    """
    1.
    :return:
    """
    s = Solution()
    nums = [1, 1, 2]
    s.removeDuplicates(nums)
    print('af remove:', nums)
    target = [1, 2]
    assert nums == target


test_removeDuplicates()
