"""
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, 
sort them in-place so that objects of the same color are adjacent, 
with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, 
white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:

        """
        We are going to make a hashmap of the nums which has the frequencies of 
        {0,1,2} and based on these frequencies we will overwrite the nums with
        respective values.
        Counter can be used, but for now I am using list and making counter in it.
        """

        frequency = [0] * 3

        for num in nums:
            if num == 0:
                frequency[num] += 1
            elif num == 1:
                frequency[num] += 1
            else:
                frequency[num] += 1

        # print(frequency)

        for index in range(len(nums)):
            if index < frequency[0]:
                nums[index] = 0
            elif index >= frequency[0] and index < frequency[0] + frequency[1]:
                nums[index] = 1
            else:
                nums[index] = 2

        return nums             


if __name__=="__main__":
    obj = Solution()
    nums = [2,0,2,1,1,0,0,0,0]
    print(obj.sortColors(nums))
        