# 1207. Unique Number of Occurrences
# Given an array of integers arr, return true if the number of occurrences of each value
#  in the array is unique or false otherwise.

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        seen = set()
        dict = {}
        for item in arr:
            if item in dict:
                dict[item] += 1
            else:
                dict[item] = 1
        for value in dict.values():
            if value in seen:
                return False
            else:
                seen.add(value)

        return True


# 2215. Find the Difference of Two Arrays
# Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
# answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
# answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
# Note that the integers in the lists may be returned in any order.

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        answer = []
        set1 = set(nums1)
        set2 = set(nums2)
        distinct1 = set1 - set2
        distinct2 = set2 - set1
        answer = [list(distinct1)] + [list(distinct2)]

        return answer


# 383. Ransom Note
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed 
# by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransom_dict = {}
        magazine_dict = {}
        for char in ransomNote:
            if char in ransom_dict:
                ransom_dict[char] += 1
            else:
                ransom_dict[char] = 1
        
        for char in magazine:
            if char in magazine_dict:
                magazine_dict[char] += 1
            else:
                magazine_dict[char] = 1
           
        for value in magazine_dict:
            if magazine_dict.get(value) >= ransom_dict.get(value):
                continue
            else:
                return False
            
        return True

# 771. Jewels and Stones
# You're given strings jewels representing the types of stones that are jewels, and stones
#  representing the stones you have. Each character in stones is a type of stone you have. 
#  You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count = 0
        jewels = set(jewels)
        for stone in stones:
            if stone in jewels:
                count += 1
                
        return count


# 1426. Counting Elements
# Given an integer array arr, count how many elements x there are, such that x + 1 is also in arr. 
# If there are duplicates in arr, count them separately.

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr_set = set(arr)
        count = 0
        for x in arr:
            if x + 1 in arr_set:
                count +=1 
            
        return count

# 1832. Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is 
# a pangram, or false otherwise.

class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        
        sen = set(sentence)
        
        return len(sen) == 26
        

            

                