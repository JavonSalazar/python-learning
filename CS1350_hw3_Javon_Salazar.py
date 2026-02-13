# Homework 3
# Name: Javon Salazar
# Date: 2/12/26
#Description: The homework assignment helps me practice my nunpy skills. 

import numpy as np


# Problem 1: Array Creation and Basic Operations

print("=== Problem 1 ===")


# Part A: Create Arrays

zeros_arr = np.zeros(8)
print("zeros_arr:", zeros_arr)

ones_matrix = np.ones((3, 4))
print("\nones_matrix:\n", ones_matrix)

range_arr = np.arange(10, 51, 5)
print("\nrange_arr:", range_arr)

linear_arr = np.linspace(0, 2, 9)
print("\nlinear_arr:", linear_arr)

# Part B: Basic Operations

a = np.array([2, 4, 6, 8, 10])
b = np.array([1, 2, 3, 4, 5])

print("\na + b:", a + b)
print("a * b:", a * b)
print("a ** 2:", a ** 2)
print("a / b:", a / b)
print("Sum of a:", np.sum(a))
print("Mean of b:", np.mean(b))


# Problem 2: Array Attributes and Statistics

print("\n\n=== Problem 2 ===")

matrix = np.arange(1, 21).reshape(4, 5)

# Part A: Attributes
print("\nMatrix:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Total elements:", matrix.size)
print("Data type:", matrix.dtype)
print("Total bytes:", matrix.nbytes)

# Part B: Statistics
print("\nOverall mean:", np.mean(matrix))
print("Overall std deviation:", np.std(matrix))
print("Min:", np.min(matrix))
print("Max:", np.max(matrix))
print("Row sums:", np.sum(matrix, axis=1))
print("Column means:", np.mean(matrix, axis=0))
print("Index of max (flattened):", np.argmax(matrix))


# Problem 3: Indexing and Boolean Selection

print("\n\n=== Problem 3 ===")

scores = np.array([
    [85, 90, 78, 92],   # Alice
    [70, 65, 72, 68],   # Bob
    [95, 98, 94, 97],   # Carol
    [60, 55, 58, 62],   # Dave
    [88, 85, 90, 87],   # Eve
    [75, 80, 77, 82]    # Frank
])

students = ['Alice', 'Bob', 'Carol', 'Dave', 'Eve', 'Frank']

# Part A: Basic Indexing

print("\nCarol Exam2:", scores[2, 1])
print("Alice scores:", scores[0])
print("All Exam3 scores:", scores[:, 2])
print("Bob & Carol Exam1 & Exam2:\n", scores[1:3, 0:2])

# Part B: Boolean Selection

mask = scores >= 90
print("\nBoolean mask (>=90):\n", mask)

print("Scores >= 90:", scores[mask])
print("Count >= 90:", np.sum(mask))

averages = np.mean(scores, axis=1)
high_students = [students[i] for i in range(len(students)) if averages[i] >= 85]
print("Students with avg >= 85:", high_students)

# Replace failing scores (<60) with 60
scores_modified = scores.copy()
scores_modified[scores_modified < 60] = 60
print("Modified scores:\n", scores_modified)


# Problem 4: Reshaping and Broadcasting

print("\n\n=== Problem 4 ===")

# Part A: Reshaping

arr = np.arange(1, 25)

matrix_4x6 = arr.reshape(4, 6)
print("\n4x6 matrix:\n", matrix_4x6)

array_3d = arr.reshape(2, 3, 4)
print("\n2x3x4 array:\n", array_3d)

flattened = array_3d.flatten()
print("\nFlattened array:", flattened)

# Part B: Broadcasting

prices = np.array([
    [1.20, 1.50, 1.30, 1.40],  # Apple
    [0.50, 0.60, 0.55, 0.45],  # Banana
    [0.80, 0.90, 0.85, 0.75]   # Orange
])

# 1. 10% discount
discounted = prices * 0.9
print("\nDiscounted prices:\n", discounted)

# 2. Adds delivery fee
delivery_fee = np.array([0.10, 0.10, 0.10, 0.10])
with_delivery = prices + delivery_fee
print("\nWith delivery fee:\n", with_delivery)

# 3. Applys tax rates
tax_rates = np.array([0.08, 0.06, 0.07, 0.05])
final_prices = prices * (1 + tax_rates)
print("\nFinal prices with tax:\n", final_prices)

# 4. Normalize by row 
row_means = np.mean(prices, axis=1).reshape(-1, 1)
normalized = prices - row_means
print("\nNormalized prices:\n", normalized)
