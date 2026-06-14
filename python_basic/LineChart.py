import matplotlib.pyplot as plt
mon = ["Jan","Feb","Mar","Apr","Jun"]
proA = [10, 20, 30, 40, 50]
proB = [15, 25, 35, 45, 55]

plt.figure(figsize=(8,5))
plt.plot(mon, proA, label = "Product A", linestyle = "-.")
plt.plot(mon, proB, label = "Product B", linestyle=":")
plt.legend()
plt.grid()
plt.show()