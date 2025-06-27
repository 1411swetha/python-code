#python script to group a DataFrame by the department and coluculate the average salary
import pandas as pd

df = pd.DataFrame({
    'name' : ["pragni", "john", "mice"],
    'depatment' : ["ece", "cse", "ece"],
    'salary' : [5000, 6000, 8000]
})

res = df.groupby('depatment')['salary'].mean().reset_index()

print(res)