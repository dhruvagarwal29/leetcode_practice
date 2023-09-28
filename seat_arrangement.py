"""
You are given an integer N denoting the number of students in a class. The 
class has N*N desks for the upcoming examination. But this time the examination
department came up with a unique idea to avoid cheating amoung students.
They decided that during the exam no two students can sit in the same row
or same column. 
Your task is to find the number of ways in which they can make their students
sit in the exam by implementing the unique idea.
"""

#### solution 

"""
No two students can sit together is the key here

possibility of two cases

1) N is odd

2) N is even 

"""

class Solution:
    def factorial(self,number):
        if number == 0:
            return 1 
        elif number < 0:
             return "Factorial for number is not defined "
        else:
            return number * self.factorial(number-1)
    
    def seat_arrangement(number):
        # if number is even 
        
        




