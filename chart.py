import matplotlib.pyplot as plt
products = ['product A','product B','product C','product D']
inventory = [45,88,21,63]
plt.figure(figsize=(8,5))
plt.bar(products,inventory,color='teal',edgecolor='black',width=0.6)
plt.title('Current Stock InventoryLevel',fontsize=14)
plt.xlabel('Product Catalogue',fontsize=12)
plt.ylabel('Units Available',fontsize=12)
plt.show()
