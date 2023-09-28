import pandas as pd

# Create a list of lists
list_of_lists = [
    {"Name":"Dhruv", "Age": 20},
    {"Name":"Rahul", "Age": 21},
]

# Create a dataframe from the list of lists
df = pd.DataFrame(list_of_lists)
# Print the dataframe
print(df)