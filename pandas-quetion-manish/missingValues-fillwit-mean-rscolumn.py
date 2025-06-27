import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['sw', 'pr', 'ar'],
    'age' : [10, np.nan, 15],
    'class' : [5, 6, np.nan]
})

df['age'].fillna(df['age'].mean(), inplace=True)
df['class'].fillna(df['class'].mean(), inplace=True)
print(df)