"""
program to reverse dictionary key to value and value to key

Example - 
dict1 = {1: "one", 2: "two", 3: "three", 4: "four"}

Output - 
dict1 = {'one': 1, 'two': 2, 'three': 3, 'four': 4}

"""

def reverse(dict):
    new_dict = {}
    for key,value in dict.items():
        new_dict[value] = key 
    
    return new_dict

if __name__=="__main__":
    dict1 = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(reverse(dict1))

### Smarter way to do this

def reverse_dict(dict):
    return {value: key for key, value in dict.items()}

if __name__=="__main__":
    dict1 = {1: "one", 2: "two", 3: "three", 4: "four"}
    print(reverse_dict(dict1))
