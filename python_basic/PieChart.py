import matplotlib.pyplot as plt
x = [10,20,30,40,50]
y = [60,70,80,90,100]
plt.pie(x,labels=y, autopct="%1.1f%%")
plt.show()