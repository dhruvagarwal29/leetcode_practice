"""
1984. Minimum Difference Between Highest and Lowest of K Scores

You are given a 0-indexed integer array nums, where nums[i] represents
 the score of the ith student. You are also given an integer k.
Pick the scores of any k students from the array so that 
the difference between the highest and the lowest of the k scores is minimized.
Return the minimum possible difference.

Example 1:
Input: nums = [90], k = 1
Output: 0
Explanation: There is one way to pick score(s) of one student:
- [90]. The difference between the highest and lowest score is 90 - 90 = 0.
The minimum possible difference is 0.

Example 2:
Input: nums = [9,4,1,7], k = 2
Output: 2
Explanation: There are six ways to pick score(s) of two students:
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 4 = 5.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 1 = 8.
- [9,4,1,7]. The difference between the highest and lowest score is 9 - 7 = 2.
- [9,4,1,7]. The difference between the highest and lowest score is 4 - 1 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 4 = 3.
- [9,4,1,7]. The difference between the highest and lowest score is 7 - 1 = 6.
The minimum possible difference is 2.
"""

from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        first we sort the given array and then
        we have to put 2 pointers such that one is at 0 and other is at k - 1
        making sliding window of k size 
        """
        nums.sort()
        left = 0
        right = k -1 
        difference = float("inf")
        while right < len(nums):
            """ while loop condition will fail when right (means windows last index) is 
            equal to the len(nums) showing that the loop is complete"""
            difference = min(difference, nums[right] - nums[left])

            left += 1
            right += 1
        
        return difference

if __name__=="__main__":
    obj = Solution()
    print(obj.minimumDifference([1,9,7,4], 2))
