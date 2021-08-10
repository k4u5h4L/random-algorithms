'''
Find the Difference
Easy

You are given two strings s and t.

String t is generated by random shuffling string s and then add one more letter at a random position.

Return the letter that was added to t.

 

Example 1:

Input: s = "abcd", t = "abcde"
Output: "e"
Explanation: 'e' is the letter that was added.

Example 2:

Input: s = "", t = "y"
Output: "y"

Example 3:

Input: s = "a", t = "aa"
Output: "a"

Example 4:

Input: s = "ae", t = "aea"
Output: "a"
'''


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        s.sort()
        
        t = list(t)
        t.sort()
        
        for a1, a2 in zip(s, t):
            if a1 != a2:
                return a2
            
        return t[-1]
