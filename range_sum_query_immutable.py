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
# this one is slow as sumRange is called again and again and we have to perform the while loop that 
# many times
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


# fast one, we are making one array named cummulative sum and performing the sum in init only
# to save the computations and this new array will be length + 1 size containing zeroes initially
# and then we can fill them using for loop 

# after we have the array ready then we can find out the any sum from right to left 
# just by getting the elememts from right+1 - left of the array as right has all the sum till that index and 
# we have that right at index+1 positionz


class NumArray:

    def __init__(self, nums: List[int]):
        self.cumulative_sum = [0] * (len(nums) + 1)
        
        for i in range(len(nums)):
            self.cumulative_sum[i + 1] = self.cumulative_sum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.cumulative_sum[right + 1] - self.cumulative_sum[left]
