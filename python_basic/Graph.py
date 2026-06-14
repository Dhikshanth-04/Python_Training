import matplotlib.pyplot as plt

months = ["Jan","Feb","Mar","Apr"]

sales = [100,150,120,200]

plt.plot(
    months,
    sales,
    color="green",
    marker="o",
    linewidth=3
)

plt.title("Monthly Sales")

plt.xlabel("Months")

plt.ylabel("Sales")

plt.show()