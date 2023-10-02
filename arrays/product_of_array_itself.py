"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # make 2 arrays one will go from start to end and other will be vice versa

        prefix_multiplier = []
        suffix_multiplier = []
        multiplier = 1

        for num in nums:
            prefix_multiplier.append(multiplier)
            multiplier *= num
        
        # reset the multiplier 
        multiplier = 1 

        for i in range(len(nums)-1,-1,-1):
            suffix_multiplier.append(multiplier)
            multiplier *= nums[i]
        
        for i in range(len(nums)):
            nums[i] = prefix_multiplier[i] * suffix_multiplier[-i-1] # suffix from reverse
        
        return nums
    
    """
    save the memory 
    """

    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        
        prefix_multiplier = []
        result = [1] * len(nums)
        print(len(nums))
        multiplier = 1
        for i in range(len(nums)):
            result[i] = multiplier
            multiplier *= nums[i]
        
        multiplier = 1
        for i in range(len(nums)-1,-1,-1):
            result[i] *= multiplier
            multiplier *= nums[i]
        
        return result

        

if __name__=="__main__":
    obj = Solution()
    print(obj.productExceptSelf1([1,2,3,4]))
    