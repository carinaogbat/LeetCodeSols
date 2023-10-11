# 392. Is Subsequence
# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions 
# of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        i = j = count = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                count +=1
                i += 1
            j += 1

        return count == len(s)


# 1768. Merge Strings Alternately
# You are given two strings word1 and word2. Merge the strings by adding letters in 
# alternating order, starting with word1. If a string is longer than the other, append 
# the additional letters onto the end of the merged string.
# Return the merged string.

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_word = []
        i = j = 0
        while i < len(word1) and j < len(word2):
            new_word.append(word1[i])
            new_word.append(word2[j])
            i += 1
            j += 1
        
        while i < len(word1):
            new_word.append(word1[i])
            i += 1

        while j < len(word2):
            new_word.append(word2[j])
            j += 1

        return "".join(new_word)


# 344. Reverse String
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        left = 0
        right = len(s) - 1
        while left < right:
            left_temp = s[left]
            right_temp = s[right]
            s[left] = right_temp
            s[right] = left_temp
            left += 1
            right += 1
        
        return s


