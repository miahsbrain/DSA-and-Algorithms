'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''

from typing import List

nums_list = [
    {'nums': [1,1,1,2,2,3], 'k': 2},
    {'nums': [1], 'k': 1},
]

class Solution:
    @staticmethod
    def topKFrequent(nums: List[int], k: int) -> bool:
        # create a list to store the count of each value but in a clever way
        count = {}
        freq = [[] for _ in range(len(nums + 1))]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        # Proven approach
        for v, c in count.items():
            freq[c].append(v)
        
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

                


# Check answer
if __name__ == '__main__':
    for nums in nums_list:
        print(Solution.topKFrequent(nums['nums'], nums['k']))