"""
303. Range Sum Query - Immutable

Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive 
where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between 
indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

"""

class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0 
        while left <= right:
            total += self.nums[left]
            left +=1
        return total

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(obj.sumRange(0,2))