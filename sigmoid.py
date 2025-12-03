import numpy as np


def sigmoid(x):
   
    return 1 / (1 + np.exp(-x))

if __name__ == "__main__":
    sample_values = np.linspace(-6, 6, num=11)
    outputs = sigmoid(sample_values)

    for value, result in zip(sample_values, outputs):
        print(f"x = {value: .2f} -> sigmoid(x) = {result: .4f}")