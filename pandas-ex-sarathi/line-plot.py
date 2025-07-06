import pandas as pd


data = {'units': [1, 2, 3, 4, 5],
        'price': [7, 12, 8, 13, 16]}
# Create a DataFrame df
df = pd.DataFrame(data)

df.plot(x='units', y='price')