import matplotlib.pyplot as plt

age = [15,20,30,40,50,60] #match the ages with names
names = ["p1","p2","p3","p4","p5","p6"]

                        #also we have to match the colors with names and ages 
plt.bar(names,age,color=['red','blue','green','purple','black','yellow'],label='chart1',width=0.4)
plt.xlabel("name")
plt.ylabel("age")
plt.title("scatter chrt")
plt.legend()
plt.show()