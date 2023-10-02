"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the
 k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

"""

from typing import List
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        """
        We are going to use Hashmap and maxheap to get the top k elements 

        hahsmap will count the frequencies of the numbers and maxheap is going 
        to give us the top k elements

        """

        hashmap = {}
        maxheap  = []
        result = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        
        for key, value in hashmap.items():
            heapq.heappush(maxheap, (-value, key))
            """
            -value is used as y default python has minheap only and it doesnt support
            maxheap so to modify minheap as maxheap we put - sign over there in front 
            of the value which helps us to make the minheap in maxheap
            """
        
        for i in range(k):
            result.append(heapq.heappop(maxheap)[1])
        
        return result

if __name__=="__main__":
    obj = Solution()
    nums = [1,1,1,2,2,3]
    k = 2
    print(obj.topKFrequent(nums, k))