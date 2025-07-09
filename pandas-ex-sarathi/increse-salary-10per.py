
import pandas as pd 
df = pd.DataFrame({
    'name' : ['bob', 'Raj'],
    'salary': [1000, 2000]
})
print(df)
#increase salary by 10%
df['salary'] = df['salary']*1.10

print(df)
