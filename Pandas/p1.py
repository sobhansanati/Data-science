#sobhan fbouna 
#2022/08/31

import pandas as pd
import numpy as np


df = pd.Series([10,20,30,40],['a','b','c','d'])
print(df)

name = pd.Series(['Tom','James','Ricky','Vin','Seteve','Smith','Jack'])
age = pd.Series([25,26,25,23,30,29,23])
rank = pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])
print(name)
print(age)
print(rank)


v1 = pd.Series(np.random.randn(4))
print(v1)

v2=pd.Series([2,5,3,np.nan,6])
print(v2)
print(v2.empty)


v3 = pd.Series(np.random.randn(4))
print('the objecty is empty ?',v3.empty)


v4=pd.Series(np.random.randn(4))
print(v4)
print('the dimensions of the object : ',v4.ndim,v4.size,v4.values,v4.head(2),v4.tail(2))


d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
	'Age' : pd.Series([25,26,25,23,30,29,23]),
	'rank' : pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])
}

df = pd.DataFrame(d)
print(df)
print(df.tail(3))
print(df.head(3))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df['Name'],df.Age)
print(df.T)


print(df.sort_values(by='Name'))
l =  df.copy()
print(l)
print('value counts ',df['Age'].value_counts())
p=[df[0:1],df[3:5],df[6:7]]
print('concat',pd.concat(p))
print('append',df.append(p))