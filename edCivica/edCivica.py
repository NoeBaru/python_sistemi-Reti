import matplotlib as mpl
mpl.use('TkAgg')

import matplotlib.pyplot as plt
import csv

mese = []
tempMedia = []
giacca = []
scuola = []
gioco = []
data_file = open("./edCivica.csv")
data_reader = csv.reader(data_file, delimiter=',')
next(data_reader)

for row in data_reader:
    mese.append(row[0])
    tempMedia.append(float(row[1]))
    giacca.append(int(row[2]))
    scuola.append(int(row[3]))
    gioco.append(int(row[4]))

data_file.close()
#print(mese)
#print(scuola)

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize = (12, 9)) #crea la figura e i grafici avendo x e y
fig.suptitle('CORRELAZIONE E CAUSALITÀ')

ax1.plot(mese, tempMedia, 'red', linewidth = 3)
ax1.set_xlabel('mese')
ax1.set_ylabel('temp media')
ax1.grid()

ax2.plot(mese, giacca, 'green', linewidth = 3)
ax2.set_xlabel('mese')
ax2.set_ylabel('h con giacca')
ax2.grid()

ax3.plot(mese, scuola, 'blue', linewidth = 3)
ax3.set_xlabel('mese')
ax3.set_ylabel('h di scuola')
ax3.grid()

ax4.plot(mese, gioco, 'black', linewidth = 3)
ax4.set_xlabel('mese')
ax4.set_ylabel('h di gioco')
ax4.grid()
ax4.set_ylim([0, 40])

#grafico unico
ax5.plot(mese, tempMedia, 'red', label = tempMedia)
ax5.plot(mese, giacca, 'green', label = giacca)
ax5.plot(mese, scuola, 'blue', label = scuola)
ax5.plot(mese, gioco, 'black', label = giacca)

plt.show()