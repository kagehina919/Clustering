import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import numpy as np

X = np.array([1, 2], 
            [1.5, 1.8], 
            [10, 15], 
            [3.3, 5], 
            [4.1, 5.6], 
            [5.5, 7])

plt.scatter(x[: ,0], x[:, 1] s=150)
plt.show()

colors = 10*["g", "b", "c", "r", "k"]

class KMeans:
    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter
    
    def fit(self, data):
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = self.data[i]
        
        for i in range(self.max_iter):
            self.classifications = {}

            for i in range(self.k):
                self.classifications[i] = []

            for featureset in data:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)

            prev_centroids = dict(self.centroids)

            for classification in self.classifications:
                pass
                self.centroids[classification] = np.average(self.classifications[classification], axis=0)
                
    
    def predict(self, data):
        pass