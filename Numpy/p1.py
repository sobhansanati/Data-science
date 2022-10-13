#sobhan fbouna 
#2022/08/30
#numpy


import numpy as np

#a array form of the numpy 
v1 = np.array([10,15,20,25,30,35,40])
print(v1) #numpy array also more quick than python lists
#arange (start inclusive , stop exclusive , step size)
v2 = np.arange(0,5,1)
print(v2)
#linspace(start inclusive , stop exclusive , number of elements)
v3=np.linspace(0,4,5)
print(v3)

# zero (n) returns a vector filled with n zeros
v4=np.zeros(5)
for i in range(5):
	v4[i] = i
v5 = np.loadtxt('no.txt')
v6 = np.ones(5)
print(v4)
print(v5)
print(v6)

#3 dim array
v7=np.array([[1,2,3,4],[2,4,9,5],[5,4,8,1]])
print("v7",v7)

v8 = np.zeros((10,4))
print("v8",v8)

v9 = np.ones((5,5))
print("v9",v9)

v10 = np.identity(1)
print("v10",v10) # will show us the number of the rows and cloumns


v11 = np.identity(3)
print('v11',v11)
print(v11[1][1])
print(v11,v1)


v12 = np.append(10,v7)
print("v12",v12)


v13 = np.append(100,v12)
print(v13)

v14 = np.append(1000,v13)
print("v14",v14)


#convert a multiple dim to one dim
#v15 = v14.reshape(4,30)
#print(v15)


# replace the number of 500 instead of third num of v14
v16 = np.insert(v14,2,500)
print("v16",v16)

#must be 500 has been deleted
v17 = np.delete(v16,2)
print("v17",v17)

v17[2]=40
print("v17",v17)
print(v14.ndim) # the number of ndim
print(v17.ndim)
print(np.random.randn(5))
print(np.random.normal(10,20,100))





