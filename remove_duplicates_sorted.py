"""
26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, 
remove the duplicates in-place such that each unique 
element appears only once. The relative order of the 
elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:

Change the array nums such that the first k elements 
of nums contain the unique elements in the order 
they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left = 0
        right = 1
        counter = 1 # it has to be one as there will be one element which is unique

        while right < len(nums):
            if nums[left] != nums[right]:
                nums[counter] = nums[right]
                counter+=1
            left += 1
            right += 1
        
        return counter
    

if __name__=="__main__":
    obj = Solution()
    print(obj.removeDuplicates([1,1,2]))