import numpy as np


def softmax(x):
	"""Return softmax probabilities for a 1-D NumPy array."""
	shifted = x - np.max(x)  # improves numerical stability
	exps = np.exp(shifted)
	return exps / np.sum(exps)


if __name__ == "__main__":
	input_values = np.array([2.0, 1.0, 0.1])
	probabilities = softmax(input_values)

	for idx, prob in enumerate(probabilities):
		print(f"Class {idx}: softmax = {prob: .4f}")
