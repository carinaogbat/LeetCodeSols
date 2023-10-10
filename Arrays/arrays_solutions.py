#283 MOVE ZEROS
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order 
# of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)

        return nums


# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of 
# the squares of each number sorted in non-decreasing order.

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return sorted(num * num for num in nums)


# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, return the maximum number of consecutive 1's 
# in the array if you can flip at most k 0's.

class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left = current = ans = 0
        for right in range(len(nums)):
                if nums[right] == 0:
                    current += 1
                while current > k:
                    if nums[left] == 0:
                        current -=1
                    left += 1
                
                ans = max(ans, right - left + 1)
        
        return ans

