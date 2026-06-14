import seaborn as sns
import matplotlib.pyplot as plt

"""
A box plot in seaborn, used to visualize the distribution of numerical data using quartiles. Besides finds the outliers of data.
"""

# Sample data
data = [10, 12, 13, 15, 18, 20, 22, 25, 100]  # 100 is an outlier

sns.boxplot(data=data)

plt.title("Box Plot Example (Outlier Detection)")
plt.show()