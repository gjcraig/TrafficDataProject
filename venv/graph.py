from functions import *
import matplotlib.pyplot as plt
import math
from random import gauss

# use for testing
my_mean = 2.9
my_variance = 1.4
random_numbers = [gauss(my_mean, math.sqrt(my_variance)) for i in range(15)]

data = df("Road_Safety_Data.csv")

# Bar chart

x = ['Fatal', 'Serious', 'Slight']
counts = [severity(1), severity(2), severity(3)]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, counts, color='green')
plt.title("Number of Accidents at each Severity Level")
plt.xticks(x_pos, x)
#  plt.show()

# example 2 sample t-test using known values
A = [3.04, 1.71, 3.30, 2.88, 2.11, 2.60, 2.92, 3.60, 2.28, 2.82, 3.03, 3.13, 2.86, 3.49, 3.11, 2.13, 3.27]
B = [2.56, 2.77, 2.70, 3.00, 2.98, 3.47, 3.26, 3.20, 3.19, 2.65, 3.00, 3.39, 2.58]
print("mean of A = ", mean(A))  # should be 2.840
print("mean of B = ", mean(B))  # should be 2.9808
print("var of A = ", (svar(A)))  # should be 0.520
print("var of B = ", (svar(B)))  # should be 0.3093
student_two(A, B, 1)  # should be - 0.92
