import matplotlib.pyplot as plt

data =["2022-01-01","2022-01-02","2022-01-03","2022-01-04","2022-01-05","2022-01-06","2022-01-07","2022-01-08","2022-01-09","2022-01-10","2022-01-11","2022-01-12"]
stepCount = [5023, 6201,7542, 4908,7020,5832,4312,6789,5231,7392,6091,5667]

plt.plot(data, stepCount)
plt.ylabel('some numbers')
plt.show()
