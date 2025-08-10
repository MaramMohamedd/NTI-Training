#how to intialize a list with a specific needs (size , intial value)

def printtt(arr):
    print(arr)

#-----------------NUMPY---------------------------
import numpy as np 
arr1 = np.array([3 , 5, 6])
print("Array with 1d :\n", arr1)
arr2 = np.zeros([3 , 3])
print("Array with zeros :\n", arr2)
arr3 = np.ones([3])
print("Array with ones :\n", arr3)
arr4 = np.eye(4)
print("identity matrix :\n" , arr4)
arr5 = np.array([[3 , 4] , [5,6]])
print("Array 2d :\n", arr5)

#creating array with random values [0 ,1[
arr = np.random.rand(1 , 3)
print(arr)

#summ 
arr_sum= arr1 +3
print(arr_sum)
#mul 
arr_mul = arr1 *3
print(arr_mul)
#sub 
arr_sub  = arr1 - 3
print(arr_sub)
#div 
arr_div = arr1 / 3
print(arr_div)


#matrix mul 
mul1 = np.array([[3 , 4], [1, 1]])
mul2 = np.array([[3 , 4], [1, 1]])
res = np.dot(mul1 , mul2)
print(res)


#flatten 
flattened =mul1.flatten()
print(flattened)


arr = np.array([1 ,2 , 3 ,4 , 5])
#mean 
meann = np.mean(arr)
print(meann)
#median 
mediann = np.median(arr)
print(mediann)
#std 
stdd= np.std(arr)
print(stdd)
#concatiniation
concatenated_array  = np.concatenate((arr , [2 ,3 , 5]))
print(concatenated_array)
concatenated_array  = np.concatenate((arr , arr5.flatten()))
print(concatenated_array)

#calc avg 
#get the heighst value 
import numpy as np 
names = ["Maram" , "malak" , "tala" ,  "karma"]
ar = np.array([
    [40 , 50 ,55 , 80, 99],
    [80 , 75 ,55 , 90, 73],
    [70 , 80 ,95 , 80, 99],
    [60 , 95 ,89 , 89, 100],
])
avg_grades = np.mean(ar , axis = 1)
print("the mean grade for each student :\n")
for i , val in enumerate(avg_grades):
    print(f"{names[i]} :  {val}")


min_val = np.min(ar ,axis=1)
max_val = np.max(ar ,axis=1)
std_val = np.std(ar ,axis=1)
mean_val = np.mean(ar ,axis=1)
