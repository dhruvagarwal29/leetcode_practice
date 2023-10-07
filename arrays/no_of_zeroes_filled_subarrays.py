"""
2348. Number of Zero-Filled Subarrays

Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
Explanation: 
There are 4 occurrences of [0] as a subarray.
There are 2 occurrences of [0,0] as a subarray.
There is no occurrence of a subarray with a size more than 2 filled with 0. 
Therefore, we return 6.
Example 2:

Input: nums = [0,0,0,2,0,0]
Output: 9
Explanation:
There are 5 occurrences of [0] as a subarray.
There are 3 occurrences of [0,0] as a subarray.
There is 1 occurrence of [0,0,0] as a subarray.
There is no occurrence of a subarray with a size more than 3 filled with 0. 
Therefore, we return 9.

"""
from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        """
        This is a simple problem which has a trick of counting the zeroes
        """

        zeroes = 0 
        result_subarrays = 0

        for num in nums:
            # add all the zeroes in result_subarrays
            result_subarrays += zeroes

            if num == 0:
                zeroes += 1
                """ this is added everytime in the result and updated as well 
                when zero is increased which gives us subarrays"""
            else:
                zeroes = 0  
            
        return result_subarrays

if __name__=="__main__":

    nums = [1,3,0,0,2,0,0,4]
    obj = Solution()
    print(obj.zeroFilledSubarray(nums))