import numpy as np


def relu(x):
	"""Return ReLU activation for a scalar or NumPy array."""
	return np.maximum(0, x)


if __name__ == "__main__":
	input_values = np.array([-4.0, -1.5, -0.1, 0.0, 0.2, 1.0, 3.3])
	outputs = relu(input_values)

	for value, result in zip(input_values, outputs):
		print(f"x = {value: .2f} -> relu(x) = {result: .4f}")
