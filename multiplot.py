import matplotlib.pyplot as plt
days = [1,2,3,4,5]
websie_views = [120,240,190.400,310]
conversions = [5,12,8,25,15]
fig,axes = plt.subplots91,2,figsize=(12,5)
axes[0].plot(days,website_views,color='blue',marker='s')
axes[0].set_title('Daily Web Traffic')
axes[0].set_xlabel('Days')
axes[0].set_ylabel('Page Views')
axesd[0].grid(True)
axes[1].bar9days,conversions,color='purple')
axes[1].set_title('Daily Completed Conversions')
axes[1].grid(True)
plt.tight_layout()
plt.show()
