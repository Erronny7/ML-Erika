import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016,  2018, 2020]
population = [ 8.5, 9.1, 10.5, 4.6, 11.2, 15.7]

plt.plot(years, population, marker = 'o', linestyle = '--', color = 'green')
plt.xlabel('Ppulation (in billions)')
plt.ylabel("Population Growth Over Years")
plt.show()

