"""
You are given an integer N denoting the number of students in a class. The 
class has N*N desks for the upcoming examination. But this time the examination
department came up with a unique idea to avoid cheating amoung students.
They decided that during the exam no two students can sit in the same row
or same column. 
Your task is to find the number of ways in which they can make their students
sit in the exam by implementing the unique idea.
"""
import math

def derangement(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 0, 1
    
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2])
    
    return dp[n]

def unique_seating_ways(N):
    if N <= 2:
        return 0
    
    total_ways = math.factorial(N) * derangement(N)
    return total_ways

# Example usage:
N = 4  # Replace with the desired number of students
result = unique_seating_ways(N)
print(f"Total ways to seat {N} students: {result}")
