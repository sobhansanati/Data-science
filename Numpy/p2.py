import numpy as np
v1=np.array([10,20,30])
print("v1",v1)
#v2=np.array([10,20,15,30,25,35])
#print("v2",v2)
#v3 =v1+v2
#print(v3)
#print(v2*3)
#print(np.sum(v1))
#print(np.sin(v1))
v4 = np.array([[2,3,4],[34,52,48],[2,3,4]])
print(v4)
#all of the algebra and math functions are included in numpy
print(np.diagonal(v4,-1)) 
print(np.trace(v4))
print(v4.T) # changing mag of the columns and rows
print("vstack of v1 and v4 ",np.vstack((v1,v4)))
#print(np.hstack((v1,v4)))