#Question   605. Can Place Flowers LeetCode  

"""
You have a long flowerbed in which some of the plots are 
planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
 where 0 means empty and 1 means not empty, and an integer n, 
 return true if n new flowers can be planted in the flowerbed 
 without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false


"""

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        We have 3 cases here if 0th position is empty, 
        last position is empty or any middle position is empty, 
        so if to check all those 3 cases we use for loop on the 
        flowerbed and check of i==0 and flowerbed[i+1] is empty 
        means 0 then place one flower, check for another case that 
        is if last position is empty and flpwerbed[i-1] is empth 
        then place flower and decrement the n, now the last 
        condition if flower[i-1] and flower[i+1] is empty do 
        the same but all this should need a parent condition 
        and that is if flowerbed[i] ==0, these are the conditions we are using here, 

        now the edge cases if flowerbed is of only length 1, 
        then if flowerbed[0] == 0 then it is true, if 
        not and n==0 then true if not then False. 
        """
        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return True
            elif flowerbed[0]!=0 and n==0:
                return True
            else:
                return False
            
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i==0 and flowerbed[i+1] == 0:
                    n-=1
                    flowerbed[i] = 1
                elif i == len(flowerbed) -1 and flowerbed[i-1] == 0:
                    n-=1
                    flowerbed[i] = 1
                elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n-=1
                    flowerbed[i] = 1
        
        return n<=0

        