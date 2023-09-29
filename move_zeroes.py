"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of 
it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        
        """ O(n) solution using two point"""
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1

        return nums
    
    def moveZeroes1(self, nums: List[int]) -> None:
        """ O(n^2) solution using two point"""

        for num in nums:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        
        return nums

if __name__=="__main__":
    obj = Solution()
    print(obj.moveZeroes([0,1,4,5,0,4]))
    print(obj.moveZeroes1([0,1,4,5,0,4]))