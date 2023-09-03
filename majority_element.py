"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more 
than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # using extra O(n) space
        # c = Counter(nums)

        # for k,v in c.items():
        #     if v > len(nums)//2:
        #         return k

        # using hashmap but O(n) space
        # hashmap = {}

        # for n in nums:
        #     if n in hashmap:
        #         hashmap[n] += 1
        #     else:
        #         hashmap[n] = 1
            
        # for k,v in hashmap.items():
        #     if v > len(nums)//2:
        #         return k

        """
        O(1) space, we have to use 2 variables and also known as Boyer-Moore Voting algo
        
        """
        count = 0 
        majority_element = None

        for n in nums:
            if count == 0:
                majority_element = n 
            if majority_element == n:
                count +=1
            else:
                count-=1
                
        return majority_element