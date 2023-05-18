# ADD STRINGS
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
#NOTES - my solution was faster than 81% of solutions because I used a dictionary
# rather than looping through or sorting lists. Other (slower) solutions included:
#--return sorted(s) == sorted(t)
#--creating a dictionary but sorting through keys

#9 PALINDROME NUMBER
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_reversed = str(x)[::-1]
        return str(x) == x_reversed

#NOTES - to reverse a number you do need to convert it to a string to use slicing,
#reverse() or sort() and sorted() methods.

#28 FIND THE FIRST INDEX OF THE FIRST OCCURENCE IN A STRING
#Given two strings needle and haystack, return the index of the first occurrence of needle 
# in haystack, or -1 if needle is not part of haystack.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        return haystack.find(needle)