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
#NOTES - only beats 16% of solutions
#Faster Solution:
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         i = 0
#         j = 0
#         length = len(nums)
#         while i + j < length:
#             if nums[i] == 0:
#                 item = nums.pop(i)
#                 nums.append(item)
#                 j = j + 1
#             else:
#                 i = i + 1
        
#         return nums

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         heap = []
#         heapify(heap)
#         for i in range(len(nums)):
#             if nums[i] == 0:
#                 heappush(heap, i)
#             else:
#                 if len(heap) != 0:
#                     index = heappop(heap)
#                     nums[index] = nums[i]
#                     nums[i] = 0
#                     heappush(heap,i)

# class Solution(object):
#     def moveZeroes(self, nums):    
#         a = nums.count(0)
#         for x in range(1,a+1):
#             nums.remove(0)
#             nums.append(0)

# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         for item in nums:
#             if item == 0:
#                 nums += [nums.pop(nums.index(item))]
#         return nums
