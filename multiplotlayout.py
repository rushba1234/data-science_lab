import matplotlib.pyplot as plt

# 1. Share common timeline variables
days = [1, 2, 3, 4, 5]
website_views = [120, 240, 190, 400, 310]
conversions = [5, 12, 8, 25, 15]

# 2. Setup grid configuration (1 row, 2 distinct columns)
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# 3. Construct Left Graph (Index 0)
axes[0].plot(days, website_views, color='blue', marker='s')
axes[0].set_title('Daily Web Traffic')
axes[0].set_xlabel('Days')
axes[0].set_ylabel('Website Views')
axes[0].grid(True)

# 4. Construct Right Graph (Index 1)
axes[1].bar(days, conversions, color='purple')
axes[1].set_title('Daily Completed Conversions')
axes[1].set_xlabel('Days')
axes[1].set_ylabel('Goal Completions')
axes[1].grid(True)

# 5. Adjust padding constraints automatically
plt.tight_layout()

# 6. Render overall canvas
plt.show()
