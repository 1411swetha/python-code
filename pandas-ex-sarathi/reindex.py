import pandas as pd

data = [['John', 50, 'Austin', 70],
        ['Cataline', 45 , 'San Francisco', 80],
        ['Matt', 30, 'Boston' , 95]]

columns = ['Name', 'Age', 'City', 'Marks']

#row indexes
idx = ['x', 'y', 'z']

df = pd.DataFrame(data, columns=columns, index=idx)

print(df)

new_idx = ['a', 'y', 'z']

new_df = df.reindex(new_idx)

print(new_df)