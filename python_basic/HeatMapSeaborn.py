import matplotlib.pyplot as plt
import seaborn as sbn
import pandas as pd

"""
Heat Map is the data visualization technique, where the relationship between the data would be represented in the matrix formats with the colors. The intensity of the colors would helpfull to analyse the relationship and patterns across the dataset variables.
"""

data = {
"age" : [25,30,35],
"salary" : [30000, 40000, 700000],
"exp" : [2,5,10]
}
df = pd.DataFrame(data)
corr = df.corr()
sbn.heatmap(corr, annot=True, cmap="coolwarm", linewidths=2)
plt.show()
