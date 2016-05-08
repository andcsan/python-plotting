# curva roc randômica

from sklearn import metrics
import random as rd

x = 0
true = []

while x < 100:
    true.append(rd.randint(0, 1))
    x+=1

score = [rd.random() for i in true]

fpr, tpr, thresholds = metrics.roc_curve(true, score, pos_label=1)

print("\nfpr:\n", fpr)
print("\ntpr:\n", tpr)
print("\nlimiares:\n", thresholds)

import matplotlib.pyplot as plt
plt.plot([float(i) for i in fpr], [float(i)for i in tpr], 'r-')
plt.plot([0, 1], [0, 1], 'b-')
plt.xlabel('fpr')
plt.ylabel('tpr')
plt.show()
