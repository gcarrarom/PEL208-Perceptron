from sklearn.datasets import load_iris

data = load_iris()

dataset = data['data']
output = []

for output_row in data['target']:
    output.append([int(output_row/2), output_row%2])
