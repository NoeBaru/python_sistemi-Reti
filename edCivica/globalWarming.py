import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import csv

anno = []
anomaly = []

data_file = open("./anomaly.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)

for row in data_reader:
    anno.append(row[0])
    anomaly.append(float(row[1]))

data_file.close()

fig, (ax1) = plt.subplots(1, 1) #crea la figura e i grafici avendo x e y
fig.suptitle('GLOBAL WARMING - temperature global anomaly')

ax1.plot(anno, anomaly, 'red')
ax1.set_xlabel('years')
ax1.set_ylabel('anomaly (°C)')
ax1.grid()

ax1.set_xticks(anno[::3]) #imposta l'intervallo sull'asse x per visualizzare solo ogni 3° anno

plt.show()