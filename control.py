from sklearn.linear_model import Perceptron
import numpy as np

test = Perceptron()
dataset = np.array(
    [[1, 1, 1, -1, -1],
     [1, -1, 1, -1, 1],
     [1, 1, -1, -1, 1]]
)

output = np.array(
    [[1, 1, -1, -1],
     [1, -1, 1, -1],
     [1, -1, -1, 1]]
)

test.fit(dataset, output)

test.predict()