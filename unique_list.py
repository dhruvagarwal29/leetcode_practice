from typing import List

def unique(numberslist:List):
    frequency_count = {}

    for num in numberslist:
        if num in frequency_count:
            frequency_count[num] = 1 + frequency_count.get(num,0)
        else:
            frequency_count[num] = 1

    return [k for k,v in frequency_count.items() if v == 1]

# space complexity - O(n)
# time complexity - O(n)

# another solution
def unique1(numberslist):
    # sort the number
    numberslist.sort()
    print(numberslist)

    unique = [numberslist[0]]
    for i in range(1,len(numberslist)):
        if numberslist[i-1]!= numberslist[i]:
            unique.append(numberslist[i])
        else:
            if unique and unique[-1] == numberslist[i]:
                unique.pop()
                print(unique)

    
    return unique  


    
if __name__=="__main__":
    s =  [1, 1, 10, -4, -4, 2, 7, 7, 8,8, -2, 98, 98, 10, 8, 2]
    print(unique1(s))

