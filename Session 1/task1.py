import matplotlib.pyplot as plt

data =["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12"]
step = [5023, 6201,7542, 4908,7020,5832,4312,6789,5231,7392,6091,5667]
calories = [230,285,320,225,310,270,200,305,240,330,275,260]
result = []
stepCount = 0

caloriesCount = 0
for i in range(0,len(step)):
	result.append((step[i] + calories[i]) / 2)
	stepCount += step[i]
	caloriesCount += calories[i]

stepCount /= stepCount / len(step)
caloriesCount /= caloriesCount / len(calories)

print((stepCount + caloriesCount) / 2) 
plt.plot(data, step,marker="o",linestyle="--",color="#0d3b2a")
plt.ylabel('some numbers')
print(result)
plt.show()
