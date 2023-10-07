"""
11. Container With Most Water

You are given an integer array height of length n. 
There are n vertical lines drawn such that the two 
endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis 
form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1
"""

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:

        """
        THIS IS THE BRUTE FORCE METHOD IT GIVES TLE IN LEETCODE
        O(n^2)
        """

        result_area = 0

        for left in range(len(height)):
            for right in range(left+1, len(height)):

                # area calculation 
                area = (right - left) * min(height[left], height[right])

                result_area = max(area, result_area)
        
        return result_area

    # OPTIMAL SOLUTION 
    def maxArea1(self, height):
        """ initialize 2 points one on starting index and other on end, then check for the
        area now increase the height which is lesser than the other height"""
        ## O(n) solution
        left = 0 
        right = len(height) - 1
        result_area = 0
        
        while left < right:

            area = (right-left) * min(height[left], height[right])

            result_area = max(area, result_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result_area



if __name__=="__main__":
    height = [1,8,6,2,5,4,8,3,7]
    obj = Solution()
    
    print(obj.maxArea(height))
    print(obj.maxArea1(height))