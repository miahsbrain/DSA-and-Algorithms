'''
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''

from typing import List
from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

class Solution:
    @staticmethod
    def groupAnagrams(strs: list[int]) -> bool:
        # Create a hashmap to store like string where the keys would be the count of characters
        result = defaultdict(list)

        for s in strs:
            count = [0] * 26
            # For every letter in s, update count value
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            result[tuple(count)].append(s)
        
        return list(result.values())


# Check answer
if __name__ == '__main__':
    print(Solution.groupAnagrams(strs))