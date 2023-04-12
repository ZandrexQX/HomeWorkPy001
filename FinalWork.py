import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
print(lst)
data = pd.DataFrame({'whoAmI':lst})

data.loc[data['whoAmI']=='robot', 'robot'] = True
data.loc[data['whoAmI']!='robot', 'robot'] = False
data.loc[data['whoAmI']=='human', 'human'] = True
data.loc[data['whoAmI']!='human', 'human'] = False

print(data)
   