"""
Make a program to check whether the number is palindrome or not !
"""
# 121
def palindrome(num):
    if num // 10 == 0: # single digit numbers
        return False

    temp = num # saving the num
    
    reversed_num = 0 

    while temp != 0:
        """
        first iteration - 
        reversed_num = 0 * 10
        reversed_num = 0 + 1
        temp = 12

        second iteration -
        reversed_num = 1 * 10
        reversed_num = 10 + 2
        temp = 1
        and so on 

        so here we can see that multiplying by 10 and adding the remainder of temp % 10
        we can reverse the number
        """
        reversed_num = reversed_num * 10
        reversed_num += temp % 10
        temp = temp // 10
    
    if reversed_num == num:
        return True
    else:
        return False

# print(palindrome(121))

# now using the generators for infinite numbers

def infinite_sequence():
    num = 0
    while True:
        yield num
        num +=1 

# gen = infinite_sequence()
# print(next(gen))

""" Generating infinite sequences"""
# for i in infinite_sequence():
#     print(i, end=" ")

""" Checking for palindrome numberss in infinnite sequence """

for num in infinite_sequence():
    palindr = palindrome(num)
    if palindr:
        print(num)
