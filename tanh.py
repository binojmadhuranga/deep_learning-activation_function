import numpy as np


def tanh(x):
	"""Return the hyperbolic tangent for a scalar or NumPy array."""
	return np.tanh(x)


if __name__ == "__main__":
	input_values = np.array([-3.0, -1.5, -0.5, 0.0, 0.5, 1.5, 3.0])
	outputs = tanh(input_values)

	for value, result in zip(input_values, outputs):
		print(f"x = {value: .2f} -> tanh(x) = {result: .4f}")
