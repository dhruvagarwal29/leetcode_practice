"""

290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a 
bijection between a letter in pattern and a non-empty word in s. 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""


from collections import Counter
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        """
        This is a good question and needs some technique

        # in this hashmap is used and previously we will see if the lenght is unmatched 
        as well as if the set of these 2 strings are same or not 

        # then we are going to use hashmap to check if the pattern is there if it is then 
        # the value of that pattern is same which is coming in, if not then false 
        # if pattern is not there then put it and if it completes the loop then it is 
        True
        """


        words = s.split(" ")

        if (len(pattern))!= len(words): 
            return False
    
        # now check for the elements if they asre same in the words and pattern is 
        #different then it is false eg - pattern -> "ab", words - "dog dog"

        if len(set(pattern)) != len(set(words)):
            return False
        
        hashmap = {}

        for character, word in zip(pattern, words):
            if character in hashmap:
                if hashmap[character] != word:
                    return False
            # else if insert the word in hashmap at character position
            hashmap[character] = word
            
        return True

    # another way of doing this is by counting the values for both the strings and comparing
    # but it will not pass all the test cases 

    # also zip_longest can be used 

    def wordPattern1(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        pcount = Counter(pattern)
        scount = Counter(s)
        print(pcount, scount)
        # sum the values of these counters

        p = sum(pcount.values())
        s = sum(scount.values())
        print(p,s)
        for a,b in zip(pcount.values(), scount.values()):
            if a==b:
                return True
            else:
                return False




if __name__=="__main__":
    obj = Solution()

    print(obj.wordPattern("abba","dog cat cat dog"))
    print(obj.wordPattern1("abba","dog cat cat dog"))    


