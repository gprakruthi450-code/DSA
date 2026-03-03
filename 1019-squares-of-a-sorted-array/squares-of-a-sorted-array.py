class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0 #left pointer
        right = n - 1 #right pointer
        pos = n - 1 # position to find the biggest element in the array

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] ** 2
                left += 1
            else:
                result[pos] = nums[right] ** 2
                right -= 1

            pos -= 1   # MUST be outside if-else

        return result  # MUST be outside while
     

     
         

        