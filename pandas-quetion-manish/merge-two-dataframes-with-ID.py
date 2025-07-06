import pandas as pd

df1 = pd.DataFrame({
    'id' : [1,2,3],
    'name' : ["swetha", "pragni", "hannu"],
    'age' : [10, 12, 11]
})
df2 = pd.DataFrame({
    'id' : [1,2,4],
    'salary' : [5000, 6000, 8000]

})

df_merged = pd.merge(df1,df2, on='id', how='inner')
print(df_merged)


# response:- if we use inner join what ever key value matches those will be merged and remaining ignored
#    id    name  age  salary
# 0   1  swetha   10    5000
# 1   2  pragni   12    6000

import pandas as pd

df1 = pd.DataFrame({
    'id' : [1,2,3],
    'name' : ["swetha", "pragni", "hannu"],
    'age' : [10, 12, 11]
})
df2 = pd.DataFrame({
    'id' : [1,2,4],
    'salary' : [5000, 6000, 8000]

})

df_merged = pd.merge(df1,df2, on='id', how='outer')
print(df_merged)

# response:- if we use outer join all key value will be merged and remaining will get NaN value

#    id    name   age  salary
# 0   1  swetha  10.0  5000.0
# 1   2  pragni  12.0  6000.0
# 2   3   hannu  11.0     NaN
# 3   4     NaN   NaN  8000.0
