import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()


sepal_length = iris.data[:, 0]


plt.hist(sepal_length, bins=10, edgecolor="black")


plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length (Iris Dataset)")


plt.show()
