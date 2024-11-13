'''
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
'''

inputs = [
    {'s': "anagram", 't': "nagaram"},
    {'s': "rat", 't': "car"},
]

class Solution:
    @staticmethod
    def isAnagram(s: str, t: str) -> bool:
        # Get a hashmap to store the count of values in each string
        smap, tmap = {}, {}
        # First case, different lengths
        if len(s) != len(t):
            return False
        # Second case, they're of thesame length. save the count of each letter in the respective hashmap
        for i in range(len(s)):
            smap[s[i]] = 1 + smap.get(s[i], 0)
            tmap[t[i]] = 1 + tmap.get(t[i], 0)

        if tmap == smap:
            return True
        return False


# Check answer
if __name__ == '__main__':
    for inp in inputs:
        print(Solution.isAnagram(inp['s'], inp['t']))