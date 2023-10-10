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


# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
#  and return false if every element is distinct.
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False


# 1748. Sum of Unique Elements
# You are given an integer array nums. The unique elements of an array are the elements that appear
#  exactly once in the array.
# Return the sum of all the unique elements of nums.
class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        unique = []
        nums_dict = {}
        for num in nums:
            if num in nums_dict:
                nums_dict[num] += 1
            else:
                nums_dict[num] = 1

        for key, value in nums_dict.items():
            if value == 1:
                unique.append(key)

        return sum(unique)


# 1133. Largest Unique Number
# Given an integer array nums, return the largest integer that only occurs once. 
# If no integer occurs once, return -1.

class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                nums_dict[i] += 1
            else:
                nums_dict[i] = 1
        
        max_num = -1
        
        for key, value in nums_dict.items():
            if value == 1 and key > max_num:
                max_num = key
        
        return max_num


# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return 
# the only number in the range that is missing from the array.
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        all_nums = set()
        nums_set = set(nums)
        for i in range(0, len(nums)+1):
            all_nums.add(i)
        missing_num = all_nums - nums_set
        
        return missing_num.pop()





