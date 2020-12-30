#!/usr/bin/env python
# coding: utf-8

# # **Assignment For Numpy**

# Difficulty Level **Beginner**

# 1. Import the numpy package under the name np

# In[2]:


import numpy as np


# 2. Create a null vector of size 10 

# In[3]:


np.zeros(10)


# 3. Create a vector with values ranging from 10 to 49

# In[14]:


arr = np.arange(10,50)
arr


# 4. Find the shape of previous array in question 3

# In[91]:


arr = np.arange(10,50)
arr.shape


# 5. Print the type of the previous array in question 3

# In[92]:


arr = np.arange(10,50)
arr.dtype


# 6. Print the numpy version and the configuration
# 

# In[8]:


print(np.__version__)
print(np.show_config())


# 7. Print the dimension of the array in question 3
# 

# In[93]:


arr = np.arange(10,50)
arr.ndim


# 8. Create a boolean array with all the True values

# In[94]:


bool_arr = np.ones(10, dtype=bool)
print(bool_arr)


# 9. Create a two dimensional array

# In[50]:


x = np.ones((2, 2))


# 10. Create a three dimensional array
# 
# 

# In[18]:


np.ones((3, 3, 3))


# Difficulty Level **Easy**

# 11. Reverse a vector (first element becomes last)

# In[95]:


arr = np.arange(10,50)
np.flip(arr)


# 12. Create a null vector of size 10 but the fifth value which is 1 

# In[96]:


x = (np.arange(10) == 4).astype(int)
print(x)


# 13. Create a 3x3 identity matrix

# In[97]:


x = np.identity(3)
print(x)


# 14. arr = np.array([1, 2, 3, 4, 5]) 
# 
# ---
# 
#  Convert the data type of the given array from int to float 

# In[98]:


arr = np.array([1, 2, 3, 4, 5])
y = arr.astype(float)
print(y)


# 15. arr1 =          np.array([[1., 2., 3.],
# 
#                     [4., 5., 6.]])  
#                       
#     arr2 = np.array([[0., 4., 1.],
#      
#                    [7., 2., 12.]])
# 
# ---
# 
# 
# Multiply arr1 with arr2
# 

# In[99]:


arr1 = np.array([[1., 2., 3.],
                        [4., 5., 6.]])  
arr2 = np.array([[0., 4., 1.],
                       [7., 2., 12.]])

new_arr = arr1 * arr2

print(new_arr)


# 16. arr1 = np.array([[1., 2., 3.],
#                     [4., 5., 6.]]) 
#                     
#     arr2 = np.array([[0., 4., 1.], 
#                     [7., 2., 12.]])
# 
# 
# ---
# 
# Make an array by comparing both the arrays provided above

# In[39]:


arr1 = np.array([[1., 2., 3.],
            [4., 5., 6.]]) 
arr2 = np.array([[0., 4., 1.],
            [7., 2., 12.]])
comparison = arr1 == arr2
equal_arrays = comparison.all() 
  
print(equal_arrays) 


# 17. Extract all odd numbers from arr with values(0-9)

# In[103]:


arr = np.arange(10)
arr = np.where(arr % 2 == 0)
print(arr)


# 18. Replace all odd numbers to -1 from previous array

# In[106]:


arr = np.arange(10)
arr[arr % 2 == 1] = -1
print(arr)    


# 19. arr = np.arange(10)
# 
# 
# ---
# 
# Replace the values of indexes 5,6,7 and 8 to **12**

# In[36]:


arr = np.arange(10)
arr[4:8] = 12
arr


# 20. Create a 2d array with 1 on the border and 0 inside

# In[63]:


arr = np.ones((6, 6))
print(arr)
arr[1:-1 , 1:-1] = 0
print("\n The new Array is: ", "\n\n", arr)


# Difficulty Level **Medium**

# 21. arr2d = np.array([[1, 2, 3],
# 
#                     [4, 5, 6], 
# 
#                     [7, 8, 9]])
# 
# ---
# 
# Replace the value 5 to 12

# In[107]:


arr2d = np.array([[1, 2, 3],

            [4, 5, 6], 

            [7, 8, 9]])

arr2d[1, 1] = 12
print(arr2d)


# 22. arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# 
# ---
# Convert all the values of 1st array to 64
# 

# In[108]:


arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr3d[0, :] = 64
print(arr3d)


# 23. Make a 2-Dimensional array with values 0-9 and slice out the first 1st 1-D array from it

# In[112]:


x = np.arange(10).reshape(2,5)
y = (x[:1, :])
print(y)


# 24. Make a 2-Dimensional array with values 0-9 and slice out the 2nd value from 2nd 1-D array from it

# In[113]:


x = np.arange(10).reshape(2,5)
y = x[1, 1]
print(y)


# 25. Make a 2-Dimensional array with values 0-9 and slice out the third column but only the first two rows

# In[114]:


x = np.arange(10).reshape(2,5)
y = x[:2, 2]
print(y)


# 26. Create a 10x10 array with random values and find the minimum and maximum values

# In[120]:


y = np.random.random((10, 10))
print("The 10x10 Array is: ", "\n\n", y)
print("\n The Minimum value is: ", y.min())
print("\n The Maximum value is; ", y.max())


# 27. a = np.array([1,2,3,2,3,4,3,4,5,6]) b = np.array([7,2,10,2,7,4,9,4,9,8])
# ---
# Find the common items between a and b
# 

# In[121]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
print(np.intersect1d(a, b))


# 28. a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# 
# ---
# Find the positions where elements of a and b match
# 
# 

# In[122]:


a = np.array([1,2,3,2,3,4,3,4,5,6]) 
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)


# 29.  names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])  data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will**
# 

# In[123]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) 
data = np.random.randn(7, 4)
data



# 30. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']) data = np.random.randn(7, 4)
# 
# ---
# Find all the values from array **data** where the values from array **names** are not equal to **Will** and **Joe**
# 
# 

# In[ ]:





# Difficulty Level **Hard**

# 31. Create a 2D array of shape 5x3 to contain decimal numbers between 1 and 15.

# In[44]:


arr = np.random.uniform(1, 15, size=(5, 3))
print(arr)


# 32. Create an array of shape (2, 2, 4) with decimal numbers between 1 to 16.

# In[45]:


arr = np.random.uniform(1, 16, size=(2,2,4))
print(arr)


# 33. Swap axes of the array you created in Question 32

# In[127]:


arr = np.random.uniform(1, 16, size=(2, 2, 4))
print("The Array is: ", "\n\n", arr)
print("\n The Swapped Array is: ", "\n\n", np.swapaxes(arr, 0, 2))


# 34. Create an array of size 10, and find the square root of every element in the array, if the values less than 0.5, replace them with 0

# In[59]:


x = np.random.random(10)
print(x)
y = np.sqrt(x)
print(y)
z = np.where(y > 0.5, y, 0)
print(z)


# 35. Create two random arrays of range 12 and make an array with the maximum values between each element of the two arrays

# In[63]:


x = np.random.random(12)
print(x)
y = np.random.random(12)
print(y)
z = np.maximum(x, y)
print(z)


# 36. names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
# 
# ---
# Find the unique names and sort them out!
# 

# In[64]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
np.unique(names)


# 37. a = np.array([1,2,3,4,5])
# b = np.array([5,6,7,8,9])
# 
# ---
# From array a remove all items present in array b
# 
# 

# In[79]:


a = np.array([1,2,3,4,5]) 
b = np.array([5,6,7,8,9])
a = np.setdiff1d(a, b)
print(a)


# 38.  Following is the input NumPy array delete column two and insert following new column in its place.
# 
# ---
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# 
# 
# ---
# 
# newColumn = numpy.array([[10,10,10]])
# 

# In[128]:


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
newColumn = np.array([[10,10,10]])
sampleArray[: , 1]  = newColumn
print(sampleArray)


# 39. x = np.array([[1., 2., 3.], [4., 5., 6.]]) y = np.array([[6., 23.], [-1, 7], [8, 9]])
# 
# 
# ---
# Find the dot product of the above two matrix
# 

# In[87]:


x = np.array([[1., 2., 3.], [4., 5., 6.]]) 
y = np.array([[6., 23.], [-1, 7], [8, 9]])
z = np.dot(x, y)
print(z)


# 40. Generate a matrix of 20 random values and find its cumulative sum

# In[90]:


x = np.random.random(20)
print(x.cumsum())

