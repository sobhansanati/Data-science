import matplotlib.pyplot as plt

#these are not updated values 
population = [8.38,2.93,0.741,0.675,3.97,15.46,3.38]
city = ['newyork','toronto','seattsle','vancouver','los angeles','istanbul','dubai']
color = ['grey','yellow','blue','purpule','red','lemon','gold']
#now we use bar function
plt.pie(population,labels=city,explode=(0,0,0,0,0,0,0),shadow=False)
plt.show()
