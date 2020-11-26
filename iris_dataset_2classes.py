from sklearn.datasets import load_iris

data = load_iris()

dataset = []
output = []

for data_row, output_row in zip(data['data'], data['target']):
    if output_row in [0,1]:
        dataset.append(data_row)
        output.append(output_row)
