import pandas as pd
df = pd.read_excel("student_records.xlsx")
##import the sheet also exlicitly
df = pd.read_excel("student_records.xlsx", "Sheet2")
print(df)

##head function will display first 5 rec by default or we can mention no
df.head()
df.head(10)
##tail function will display last 5 rec by default or we can mention no
df.tail()
df.tail(10)

##descrbe the DataFrame
df.describe()
##shape of dataframe
df.shape
##display columns
df.columns

##convert rows into columns
pd.melt()
##convert  columns into rows
df.pivot()
##display unique values
df.unique()
df['country'].unique()
##check the count
df['emp.no'].count()
df.count()
##avg salary
df['salary'].mean()
##spliting full name to two
df1= df['student_name'].str.strip()
firstname= df1.str.split(' ').str[0]
lastname= df1.str.split(' ').str[1]

##null value checking
df['Telugu'].isnull() ##it will give true or false
df[df['Telugu'].isnull()] ##this used to print those values if nulls are there

##Slcing DF
#df[start:stop:step]
df[0:10:1]
df[0:10:2]

##listng column values
df["student_name"]
df[["student_name", "Telugu"]]
##listing columns with slicing
df[["student_name", "Telugu"]][0:10:1]

##iterrows function
for row in df.iterrows():
    print(row)

##loc concepts
#df.loc[rowno, [coumn1.cloumn2.....]]
df.loc[1]
df.loc[1, ["Telugu"]]
df.loc[2,"English"]
df.loc[1, ["Telugu","Maths"]]
df.loc[0:10]
df.loc[0:10, ["Telugu","Maths"]]

##iloc examples
df.iloc[2,3]
df.iloc[0:10]
df.iloc[1,2,3,4]
df.iloc[0:10, [3,4]]
#df.iloc[row-no, [colno1,colno2,colno3,colno4]]
df.iloc[1, [1,2,3,4]]

##sorting values
df.sort_values("student_name")
df.sort_values("student_name")[0:10]
df.sort_values("Telugu")
##by default it will give the ascending order values of first column
df.sort_values(["Telugu","English"])
##it will give the deending order values of first column
df.sort_values(["Telugu","English"], ascending=False)

##Manuplating data
#add column
df["Total"] = "Total"
df["percentage"] = "Percentage"
#add column with condition
df["Total"] = df["Telugu"] + df["English"] + df["Maths"] + df["Sceinces"] + df["Social"] + df["Hindi"]
df["percentage"] = (df["Total"] / 600 ) * 100

##remove column
df["Total-dup"] = "Total"
####This will delete column from Tble in cmd line temprarly and print the response
df.drop(columns="Total-dup")
##This will delete column from Tble completely using inplace=True
df.drop(columns="Total-dup", inplace=True)

##get the duplicates
df.duplicated()
##remove duplicates
df.drop_duplicates()
##completely removes from table
df.drop_duplicates(inplace=True)

##Nan values handling
df.fillna(8)
df.fillna(8, inplace=True)
df["Telugu"].fillna(0)

##drop NaN values
df.dropna()
df.dropna(inplace=True)

##conditional handling

#print the details of students how got 80% above(single condition)
res = df.loc[df["percentage"] > 80]
print(res)
##compound condition
res = df.loc[(df["percentage"] > 60) & (df["percentage"] < 80)]
print(res)

##Grade
# <40 fail
# >40 to <60 pass
# >60 to <75 first class
# >75 disinction

df["Grade"] = "Grade"

df.loc[df["percentage"] < 40, ["Grade"]] = "Fail"

df.loc[(df["percentage"] > 40) & (df["percentage"] < 60), ["Grade"]] = "Pass"

df.loc[(df["percentage"] > 60) & (df["percentage"] < 75), ["Grade"]] = "First class"

df.loc[df["percentage"] > 75, ["Grade"]] = "Distiction"

##write to excel

df.to_excel("updated_student_records.xlsx")
df.to_excel("updated_student_records.xlsx", index=False)

###read and write to csv
df = pd.read_csv("file.csv")
filter_output = df[df["age"] > 80]
filter_output.to_csv("out.csv", index=False)

###read and write to DB(mysql)
from pymysql import connect
from sqlalchemy import create_engine
import pandas as pd

engg = create_engine("mysql+pymysql://root:admin123@localhost:3308/ZCITY")

query = "select * from PURCHASER"
connection = engg.connect()
target_df = pd.read_sql(query, connection)
tg_count = target_df.count()
