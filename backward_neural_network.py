import math

# Sigmoid and its derivative
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def sigmoid_derivative(y):
    return y * (1 - y)

# -------- USER INPUT --------
x1 = float(input("Enter input x1: "))
x2 = float(input("Enter input x2: "))
target = float(input("Enter target output: "))

# -------- INITIAL WEIGHTS --------
w13 = float(input("Enter weight w13: "))
w23 = float(input("Enter weight w23: "))

w14 = float(input("Enter weight w14: "))
w24 = float(input("Enter weight w24: "))

w35 = float(input("Enter weight w35: "))
w45 = float(input("Enter weight w45: "))

learning_rate = float(input("Enter learning rate η: "))

print("\n---- FEEDFORWARD ----")
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

# -------- BACKPROPAGATION --------
delta5 = error * sigmoid_derivative(y5)
delta3 = delta5 * w35 * sigmoid_derivative(y3)
delta4 = delta5 * w45 * sigmoid_derivative(y4)

# Update weights
w35 += learning_rate * delta5 * y3
w45 += learning_rate * delta5 * y4

w13 += learning_rate * delta3 * x1
w23 += learning_rate * delta3 * x2

w14 += learning_rate * delta4 * x1
w24 += learning_rate * delta4 * x2

print("\n---- UPDATED WEIGHTS ----")
print(f"w13 = {round(w13, 4)}, w23 = {round(w23, 4)}")
print(f"w14 = {round(w14, 4)}, w24 = {round(w24, 4)}")
print(f"w35 = {round(w35, 4)}, w45 = {round(w45, 4)}")
