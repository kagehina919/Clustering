import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np
from sklearn.cluster import KMeans

X = np.array([1, 2], 
            [1.5, 1.8], 
            [10, 15], 
            [3.3, 5], 
            [4.1, 5.6], 
            [5.5, 7])

## plt.scatter(x[: ,0], x[:, 1] s=150)
## plt.show()

clf = KMeans(n_clusters=2)
clf.fit(x)

centeroids = clf.clusters_centers_
labels = clf.labels_

colors = ["g.", "b.", "c."]

for i in range(len(X)):
    plt.plot(X[i][0], X[i][1], colors[labels[i]], markersize = 10)
plt.plot(centroids[:,0], centroids[:,1], marker='X', s=150, linewidths=5)
plt.show()