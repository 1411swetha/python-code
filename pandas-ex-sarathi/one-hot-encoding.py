import pandas as pd

data = {'Name': ['John', 'Cateline', 'Matt', 'Oliver'],
        'ID': [1, 22, 23, 36, 1]}

df = pd.DataFrame(data)
#perform one hot encoding to convert categorical values to numeric ones so that can be fed to the machine learning algorithm.
#one hot encoding 
new_df = pd.get_dummies(df.Name)
new_df.head()