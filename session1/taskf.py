import numpy as np
array = np.arange(25).reshape(5, 5)
print(array)
print("the mean : " ,np.mean(array))
print("the max : " , np.max(array))
print("the sum : " , np.sum(array))
print("-"*50)
#demand 2
array = np.arange(12).reshape(3,4)
print(array)
print('-'*50)
#demand 3
array = np.random.rand(3,3)
print(array)
print('-'*50)
#inverse 
inversed_array = np.linalg.inv(array)
print(inversed_array)


