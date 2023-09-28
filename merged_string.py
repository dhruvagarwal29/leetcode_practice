"""
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge
the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the 
other, append the additional letters onto the end 
of the merged string.

Return the merged string.

Example 1:
Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        merged_string = ""

        for i in range(0, min(len(word1), len(word2))):
            merged_string += word1[i] + word2[i]
        
        if len(word1) > len(word2):
            merged_string += word1[i+1:]
        else:
            merged_string += word2[i+1:]
        
        return merged_string

if __name__=="__main__":
    obj = Solution()
    print(obj.mergeAlternately("ab", "pqrs"))