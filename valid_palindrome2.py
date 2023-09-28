"""
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

"""

class Solution:
    def validPalindrome(self, s: str) -> bool:

        """ This is the helper function to check whether the substring of the string is
        palindrome or not !!"""
        def isPalindrome(s:str, left:int, right:int):
            while left <= right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True 
        

        """solution start from here using 2 pointers, we have to check it simultaneously
         by adding one element to star(left) or removing one by end(right) """
        
        left, right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                # Try removing either the character at left or right
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)
            left += 1
            right -= 1
        return True
    
if __name__=="__main__":
    obj = Solution()
    print(obj.validPalindrome("abc"))