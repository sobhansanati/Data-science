import matplotlib.pyplot as plt



a = [10,5,12,16,20,25]
b = [15,20,30,40,50,60]
c = [3,5,12,14,16,3]
# in the past part we used plot function but here we try another wichs called plt.scatter()
plt.scatter(b,a,marker="*",color='purple') #new attribute called line width = and markersize =
plt.scatter(b,c,marker="*",color='black')
plt.show()
