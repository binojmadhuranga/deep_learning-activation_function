import numpy as np


def leaky_relu(x, alpha=0.01):
	"""Return Leaky ReLU activation for a scalar or NumPy array."""
	return np.where(x > 0, x, alpha * x)


if __name__ == "__main__":
	input_values = np.array([-3.0, -1.0, -0.2, 0.0, 0.4, 1.2, 2.5 ,400])
	outputs = leaky_relu(input_values, alpha=0.05)

	for value, result in zip(input_values, outputs):
		print(f"x = {value: .2f} -> leaky_relu(x) = {result: .4f}")
