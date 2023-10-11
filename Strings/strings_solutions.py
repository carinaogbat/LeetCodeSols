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


#9 PALINDROME NUMBER
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_reversed = str(x)[::-1]
        return str(x) == x_reversed



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

#58 RETURN LENGTH OF LAST WORD
# Given a string s consisting of words and spaces, return the length of the last word 
# in the string. A word is a maximal substring consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])


#151 REVERSE WORDS IN A STRING
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by 
# at least one space. Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The 
# returned string should only have a single space separating the words. Do not include any extra
#  spaces.


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_word_string = ""
        words = s.strip()
        words_list = words.split()
        words_list.reverse()
        for word in words_list:
            reverse_word_string += word + " "

        return reverse_word_string.strip()




