

# Description

This is an implementation of the [Perceptron](https://en.wikipedia.org/wiki/Perceptron) algorithm done in Python.

# Buid & Run

This is a simple class that can be used in any way you need. To run it, you'll need to install the requirements in the root of this repo.
1. Clone this repo and set your $PWD to it's root
2. Install the requirements: `pip install -r requirements.txt`
3. Use the class to train a perceptron:
```python
from perceptron import Perceptron

perc = Perceptron()
perc.fit(dataset, expected_outputs_for_dataset)

input_to_classify = [1, 1, 1, -1, -1]

perc.predict(input_to_classify)
```

# Examples
You can find examples on how to use this Perceptron class in this repo's [perceptron.ipynb](./perceptron.ipynb) notebook.
