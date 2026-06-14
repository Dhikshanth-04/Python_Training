import matplotlib.pyplot as plt
import seaborn as sbn

"""
Distribution plot is used to visualise, how the data is spread across the range. Used to understand the frequency and distribution of the dataset.
"""

x = [10,20,20,30,30,40,40,50,100]
sbn.histplot(x, kde=True)
plt.show()