#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # # Solution 1
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j];

        # # Solution 2
        # map = {};
        # for i in range(0, len(nums)):
        #     map[nums[i]] = i;
        
        # for i in range(0, len(nums)):
        #     key = target - nums[i];
        #     if (key in map) and (map[key] != i):
        #         return [i, map[key]];

        # Solution 3
        map = {};
        for i in range(0, len(nums)):
            key = target - nums[i];
            if (key in map) and (map[key] != i):
                return [map[key], i];
            else:
                map[nums[i]] = i;
        
# @lc code=end

