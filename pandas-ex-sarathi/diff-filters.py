import pandas as pd

data = {'Name': ['John', 'Cataline', 'Matt'],
        'Age': [50, 45, 30],
        'City': ['Austin', 'San Francisco', 'Boston'],
        'Marks' : [70, 80, 95]}

# Create a DataFrame df
df = pd.DataFrame(data)

##based on condition
#new_df = df[(df.Name == "John") | (df.Marks > 90)]
new_df = df[(df["Name"] == "John") | (df["Marks"] > 90)]
print (new_df)

sec_df= df.query('Name == "John" or Marks > 90')
print (sec_df)



