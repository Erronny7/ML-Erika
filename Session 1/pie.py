import matplotlib.pyplot as plt

categories = ['Category A', 'Category B', 'Category C', 'Category D','Category F']
percentages = [25, 30, 15, 10, 20]

explode = [0, 0.1, 0, 0, 0.5]
colors = ['red', 'blue', 'orange', 'green', 'skyblue']

plt.pie(percentages, explode = explode, labels = categories, colors = colors, shadow = True)
plt.title("Percentages Destribution")
plt.legend(categories)
plt.show()
