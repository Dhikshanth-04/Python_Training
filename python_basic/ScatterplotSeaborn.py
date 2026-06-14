import seaborn as sns
import matplotlib.pyplot as plt

"""
Scatter plot is used to represent the relationship between two numerical variables. Each point represents the observation, if the pts go up-positive relation, pt goes down-negative relation, random pts-no relation
"""

# Sample data
data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [20, 25, 35, 40, 55, 65, 75, 85]
}

sns.scatterplot(x="Study_Hours", y="Marks", data=data, hue="Marks")

plt.title("Study Hours vs Marks")
plt.show()