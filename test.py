

nums = [3,2,4]

target = 6


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for num in nums:
            another_num = target - num
            try:
                if num == another_num:
                    continue
                another_num_index = nums.index(another_num)
            except BaseException :
                continue
            if another_num_index >=0:
                return [nums.index(num),another_num_index]

print(Solution.twoSum(Solution,nums,target))