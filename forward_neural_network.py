import math

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# -------- USER INPUT --------
x1 = float(input("Enter input x1: "))
x2 = float(input("Enter input x2: "))
target = float(input("Enter target output: "))

# -------- WEIGHTS --------
w13 = float(input("Enter weight w13: "))
w23 = float(input("Enter weight w23: "))

w14 = float(input("Enter weight w14: "))
w24 = float(input("Enter weight w24: "))

w35 = float(input("Enter weight w35: "))
w45 = float(input("Enter weight w45: "))

print("\n---- FEEDFORWARD PROCESS ----")

# Hidden layer neuron H3
a3 = (w13 * x1) + (w23 * x2)
y3 = sigmoid(a3)
print("Hidden neuron H3 output:", round(y3, 4))

# Hidden layer neuron H4
a4 = (w14 * x1) + (w24 * x2)
y4 = sigmoid(a4)
print("Hidden neuron H4 output:", round(y4, 4))

# Output neuron O5
a5 = (w35 * y3) + (w45 * y4)
y5 = sigmoid(a5)
print("\nFinal Output:", round(y5, 4))

# -------- ERROR --------
error = target - y5
print("Error:", round(error, 4))

