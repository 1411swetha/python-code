#we can create DataFrame using list of list using DataFrame() constructor by parsing list,columns keyvalues to it
import pandas as pd
my_lst = [[1, 'mine'], [2, 'is'], [3, 'mine']]

df = pd.DataFrame(my_lst, columns=['id', 'data'])

print(df)