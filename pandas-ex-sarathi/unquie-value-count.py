import pandas as pd

data = [['John', 50, 'Male', 'Austin', 70],
        ['Cataline', 45 ,'Female', 'San Francisco', 80],
        ['Matt', 30 ,'Male','Boston', 95]]

# Column labels of the DataFrame
columns = ['Name','Age','Sex', 'City', 'Marks']

# Create a DataFrame df
df = pd.DataFrame(data, columns=columns)

unique_count = df['Sex'].value_counts()
print(unique_count)

count = df["Sex"].count()
print(count)

unique_type = df["Sex"].unique()
print(unique_type)