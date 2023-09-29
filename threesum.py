"""
15. 3Sum

Given an integer array nums, return all the 
triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
"""

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
        two ways to solve this question
        1) without using set 
        2) with using set 
        """

        # first sort the array so it will be helpful in removing the duplicates from nums

        nums.sort()
        result = [] 
        for index, num in enumerate(nums):

            # removing duplicates 

            if index > 0 and num == nums[index-1]:
                continue
                
            left = index + 1
            right = len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]

                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    result.append([num, nums[left], nums[right]])
                    left += 1 # increasing the decreasing the pointers for checking full loop
                    right -= 1
                    """ here we are again removing the duplicates which could be 
                      present after left and before right"""
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right += 1
        return result

    """
    now with using set
    """
    def threesum_with_set(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for index, num in enumerate(nums):
            left = index + 1
            right = len(nums) - 1

            while left < right:
                current_sum = num + nums[left] + nums[right]

                if current_sum < 0:
                    left +=1
                elif current_sum >0 :
                    right -=1
                else:
                    result.add(tuple([num, nums[left], nums[right]]))
                    left += 1
                    right -= 1
        
        return result



if __name__=="__main__":
    obj = Solution()
    print(obj.threeSum([-1,0,1,2,-1,-4]))
    print(obj.threesum_with_set([-1,0,1,2,-1,-4]))

        

