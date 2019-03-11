import numpy as np

x = np.array([1,2,3,4,5])
w = np.array([1,2,-1,3,2])

# Initialize sum
sum = 0 

# Perform weighted summation
for i in range(len(x)):
  sum = sum + w[i] * x[i] 

# Print summation
print "sum = ", sum

# Print summation using dot product
print "sum with dot product = ", np.dot(w,x)
