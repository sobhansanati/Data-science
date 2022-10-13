import matplotlib.pyplot as plt


ages = [13,45,17,25,17,33,25,24,26,27,39,49,41,12,18,17,16]

#bins mean is range 
plt.hist(ages,bins=10,color="black",label="hist chart") #in past part we use the bar plot scatter but in this part we have hist = histogram
plt.xlabel("ages")
plt.title('histogram chart')
plt.legend()
plt.show()

#in this chart bins 5 or 10 might be more understandable