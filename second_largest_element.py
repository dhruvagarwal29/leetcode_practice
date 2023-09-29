"""
FInd the second largest element from the list
"""

# brute force 
"""
time complexity - O(nlogn)
"""
def second_largest(numbers):

    numbers.sort()
    result = numbers[-1]
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] < result:
            return numbers[i]

print(second_largest([1,2,3,4,7,100,7]))

# better approach 

"""
First pass - find largest 
Second pass - find 2nd largest

time complexity - O(2n) -> O(n)
"""

def second_largest1(numbers):

    # first pass find largest
    largest = numbers[0]
    for num in numbers:
        if largest < num:
            largest = num
    
    # seocnd pass 
    second_largest = numbers[0]

    for num in numbers:
        if num < largest and num > second_largest:
            second_largest = num
        
    return second_largest

print(second_largest1([1,2,3,4,7,100,7]))


# optimal approach 

def second_largest2(numbers):

    largest = numbers[0]
    # second largest can be a negative number for starting 
    second_largest = -1

    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    return second_largest

print(second_largest2([1,2,3,4,7,7,5]))