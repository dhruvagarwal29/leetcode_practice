"""
1189. Maximum Number of Balloons

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

Example 1:
Input: text = "nlaebolko"
Output: 1
Example 2:

Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
"""

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # we are going to use hashmap to count the characters present in the ballon and then check in the
        # given text if those charactes are present then we can increse the count in the hashmap 
        # and while giving the ouput we have to divide the "o" and "l" charaacter by 2 as it is 
        # appearing twice in the balloon and return the min values in the hashmap

        hashmap = {"b":0, "a":0,"l":0,"o":0,"n":0}

        for i in range(len(text)):
            if text[i] in hashmap:
                hashmap[text[i]] = 1 + hashmap.get(text[i],0)

        hashmap["o"]//=2
        hashmap["l"]//=2

        return min(hashmap.values())
    
if __name__ == "__main__":

    sol = Solution()

    print(sol.maxNumberOfBalloons("BalloonBalllooonfbdbsd"))