import matplotlib.pyplot as plt


dept = ['office','Eco','sale','buy']
gratudet = [2,3,8,4]
ungratudet = [12,4,3,2]
diploma = [2,2,3,2]
master = [5,6,4,2]

#this one is little bit diffrent than others
plt.stackplot(dept,gratudet,ungratudet,diploma,master,labels=['gratudet','unngratudet','diploma','master'])
plt.legend()
plt.savefig('stackplot.pnggratudet') # for saving your figure in dir
plt.show() 
plt.close() #for close up the figure