class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        sum = int(num1) + int(num2)

        return str(sum)

#242 VALID ANAGRAM
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for item in s:
            if item in s_dict:
                s_dict[item] += 1
            else:
                s_dict[item] = 1
        for item in t:
            if item in t_dict:
                t_dict[item] += 1
            else:
                t_dict[item] = 1

        if s_dict == t_dict:
            return True       