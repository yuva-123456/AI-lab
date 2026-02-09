import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def plot_graph(X, Y, L, t):
    plt.scatter(X, Y)
    plt.plot(X, L)
    plt.xlabel("Hours Studied")
    plt.ylabel("Marks")
    plt.title(t)
    plt.show()

data = pd.read_csv("/content/Rounded_Student_Hours_Studied_vs_Marks_Dataset.csv")
print(data.columns)

X = data["Hours_Studied"].values
Y = data["Marks"].values

m1, c1 = 0, Y[0]
print("Slope before regression:", m1)
plot_graph(X, Y, m1 * X + c1, "Before Linear Regression")

mx, my = X.mean(), Y.mean()
m2 = np.sum((X - mx) * (Y - my)) / np.sum((X - mx) ** 2)
c2 = Y[0] - m2 * X[0]
print("Slope after regression:", round(m2, 3))
plot_graph(X, Y, m2 * X + c2, "After Linear Regression")
