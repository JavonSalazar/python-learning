# Homework 9
# Name: Javon Salazar
# Date: 4/28/26
#Description: This homework covers over module 14 recursion.

#Question 1
#II
def factorial(n):
    if n == 0:  # base case
        return 1
    return n * factorial(n - 1)
def fibonacci(n):
    if n <= 1:  # base case
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
#IV
def binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
#V
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
#Question 2
import random

# generate list
arr = [random.randint(0, 1000000) for _ in range(1000000)]

# sort
sorted_arr = merge_sort(arr)