"""
128. Longest Consecutive Sequence

Given an unsorted array of integers nums, 
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        """
        TLE solution, brute force - O(n^2)
        """

        longest_count = 0

        for num in nums:

            count = 0

            while num in nums:
                count += 1  
                num += 1

            longest_count = max(longest_count, count)
        
        return longest_count

    def longestConsecutive1(self, nums: List[int]) -> int:
        """
        Optimal Approach- O(n)

        eliminate the numbers if there previous number is present in list
        """

        longest = 0
        # remove duplicates
        nums = set(nums)

        for num in nums:
            count = 0

            if num - 1 not in nums:
                # checking if previous element is not there to save computations
                while num in nums:
                    num += 1
                    count += 1
            
            longest = max(longest, count)
        
        return longest
        

if __name__=="__main__":

    obj = Solution()
    print(obj.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(obj.longestConsecutive1([0,3,7,2,5,8,4,6,0,1]))