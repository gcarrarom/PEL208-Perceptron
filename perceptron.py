import numpy as np
from copy import deepcopy
from sklearn.preprocessing import normalize


class Perceptron(object):
    '''
    THis is the class used to classify the data using a perceptron
    '''

    def __init__(self, tolerance=1e-4, learning_rate=1e-2, max_iter=1000):
        '''
        This initializes the Perceptron class with the tolerance to be used in the weight calculation

        Args:
            tolerance (float, optional): the tolerance to use for calculating the weights of the perceptron. Defaults to 1e-2.
        '''
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.synapse_array = None

    def fit(self, dataset, expected_output):
        '''
        Fits the perceptron with the new weights 

        Args:
            dataset ([[float]]): the matrix with the data to be fitted
            expected_output ([[float]]): the matrix containing the expected output of the given data
        '''
        # Initializing synapse_table
        if not self.synapse_array:
            self.synapse_array = np.zeros(len(dataset[0]))

        dataset = normalize(dataset, axis=1, norm='l1')

        convergence = False
        iter_count = 0
        while iter_count < self.max_iter: # and not convergence: Didn't work... Weird.
            # for each row of data
            convergence = True
            for dataset_row, output in zip(dataset, expected_output):
                # Calculate the new weights for the synapse Matrix
                
                previous_array = deepcopy(self.synapse_array)

                ## calculate the new weights => w i = w i + delta w i
                ## with delta w i = element i * (expected_output - output) * learning rate
                self.synapse_array += dataset_row * ( output - self.predict(dataset_row)) * self.learning_rate

                # print(
                #    f" new_weight = snapsematrix[{row_index}][{column_index}] + dataset_row[{column_index}] * (expected_output[{dataset_row_index}][{row_index}] - predict({dataset_row})[{row_index}])")

                # If all changes are less than the tolerance, we've converged
                if all((abs(previous_array) - abs(self.synapse_array)) < self.tolerance):
                    convergence = True
                else:
                    convergence = False
            iter_count += 1

    def predict(self, dataset):
        #print(f"{self.synapse_matrix} * {dataset}")
        return 1 if np.matmul(self.synapse_array, dataset) > 0 else 0


