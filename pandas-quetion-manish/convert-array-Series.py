import pandas as pd
import numpy as np

data = np.array([1, 2, 3, 4])

output = pd.Series(data)
print(output)
out2 = pd.Series(data, index=['a', 'b', 'c', 'd'])
print(out2)