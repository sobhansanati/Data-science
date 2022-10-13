import matplotlib.pyplot as plt 



a = [1,3,5,7,9] 
b = [2,4,6,8,10]
c = [1,2,3,4,5] 

plt.plot(c,a,marker='.',linestyle ='--',markerfacecolor='blue',color='black') #after marker attribute we have an linestyle / there is new attribute named (makerfacecolor)
plt.plot(c,b,marker='.',linestyle='--',markerfacecolor='yellow',color='purple') # now this dim is for y x part with linestyle (--) , we had diffrent type of linestyle such as * / s / p

plt.xlabel('x values') #we can set an label for each lines for this one its x
plt.ylabel('y values') # we can set an label for each lines for this one its y
plt.title('simple chart')  # we aslo can set a title for our chart what we liked to call it it dosent matter 
plt.legend(c) #legend function its for guidance 
plt.show()
