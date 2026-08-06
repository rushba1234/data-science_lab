import matplotlib.pyplot as plt

# Given data
rollnos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

marks = [22, 87, 5, 43, 56, 73, 55, 54, 11, 20, 51, 5, 79, 31, 27]

# Create scatter plot
plt.scatter(rollnos, marks, color="blue", marker="o")

# Labels and title
plt.xlabel("Roll Number")
plt.ylabel("Marks")
plt.title("Scatter Plot of Roll Numbers vs Marks")

# Show plot
plt.show()
