import pandas as pd

# Create a DataFrame
data = {
    'Name': ['John', 'Matt', 'John', 'Matt', 'Matt', 'Matt'],
    'Marks': [10, 10, 30, 15, 25, 18]
}

# Create a DataFrame df
df = pd.DataFrame(data)

# mean marks of John and Matt
##aggregation first with name and then calculating the mean of marks
print(df.groupby('Name').mean())
print(df["Marks"].mean())