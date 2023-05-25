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

#58 RETURN LENGTH OF LAST WORD
# Given a string s consisting of words and spaces, return the length of the last word 
# in the string.
# A word is a maximal 
# substring
#  consisting of non-space characters only.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        return len(words[-1])

#other faster solutions
# import sys
class Solution(object):
    def lengthOfLastWord(self, s):
        s1=s.strip()
        t=s1.split(' ')
        return len(t[-1])

class Solution(object):
    def lengthOfLastWord(self, s):
        arr = s.strip().split()
        return len(arr[-1])

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split()[-1])

#151 REVERSE WORDS IN A STRING
# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters. The words in s will be separated by 
# at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words. The 
# returned string should only have a single space separating the words. Do not include any extra
#  spaces.

#MY SOLUTION - beats 80% time and 20% memory
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

#OTHER SOLUTIONS
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=s.split()
        l=l[::-1]
        return ' '.join(l)

class Solution:
  def reverseWords(self, s):
    return ' '.join(reversed(s.split()))

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        
        words = s.split(" ")
        o = " ".join(words[::-1])
        return " ".join(o.split()).strip()

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        words = (s.strip()).split()

        for i in range(len(words)/2):
            words[i], words[len(words)-1-i] = words[len(words)-1-i], words[i]
        return " ".join(words)

#best memory solution
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = []
        i = 0
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            else:
                k = ""
                while i < len(s) and s[i]!= " ":
                    k += s[i]
                    i += 1
                #print(k)
                l.append(k)
        #print(l)
        return " ".join(l[::-1])

