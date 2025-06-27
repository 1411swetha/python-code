##filter data from excel while where age is grater than 50
import pandas as pd

df = pd.read_excel("input.xlsx")

filter_df = df[df['age'] > 50]

filter_df.to_write("output.xlsx", index=False)
