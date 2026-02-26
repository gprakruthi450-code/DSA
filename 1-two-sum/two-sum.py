class Solution:
    def twoSum(self, nums, target): # input given function named twoSum
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target: # sum of i , j to get targret
                    return [i, j]
        