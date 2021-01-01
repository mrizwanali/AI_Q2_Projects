#!/usr/bin/env python
# coding: utf-8

# # Numpy_Assignment_2::

# ## Question:1

# ### Convert a 1D array to a 2D array with 2 rows?

# #### Desired output::

# array([[0, 1, 2, 3, 4],
#         [5, 6, 7, 8, 9]])

# In[7]:


import numpy as np


# In[8]:


a = np.arange(0, 10).reshape(2, 5)
a


# ## Question:2

# ###  How to stack two arrays vertically?

# #### Desired Output::
array([[0, 1, 2, 3, 4],
        [5, 6, 7, 8, 9],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# In[33]:


a = np.arange(0, 10).reshape(2, 5)
b = np.ones(10).astype(np.int8).reshape(2, 5)
c = np.vstack((a, b))
c


# ## Question:3

# ### How to stack two arrays horizontally?

# #### Desired Output::
array([[0, 1, 2, 3, 4, 1, 1, 1, 1, 1],
       [5, 6, 7, 8, 9, 1, 1, 1, 1, 1]])
# In[34]:


a = np.arange(0, 10).reshape(2, 5)
b = np.ones(10).astype(np.int8).reshape(2, 5)
c = np.hstack((a, b))
c


# ## Question:4

# ### How to convert an array of arrays into a flat 1d array?

# #### Desired Output::
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# In[37]:


a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8 ,9]])
b = a.flatten()
b


# ## Question:5

# ### How to Convert higher dimension into one dimension?

# #### Desired Output::
array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
# In[41]:


a = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8 ,9], [10, 11, 12, 13, 14]])
b = a.ravel()
b


# ## Question:6

# ### Convert one dimension to higher dimension?

# #### Desired Output::
array([[ 0, 1, 2],
[ 3, 4, 5],
[ 6, 7, 8],
[ 9, 10, 11],
[12, 13, 14]])
# In[44]:


a = np.arange(0, 15)
b = a.reshape(5, 3)
b


# ## Question:7

# ### Create 5x5 an array and find the square of an array?

# In[54]:


a = np.random.random((5, 5))
print(a)
b = np.square(a)
print("\n\n Square of Array is: ", "\n\n", b)


# ## Question:8

# ### Create 5x6 an array and find the mean?

# In[55]:


a = np.random.random((5, 6))
print(a)
b = np.mean(a)
print("\n\n Mean of Array is: ", b)


# ## Question:9

# ### Find the standard deviation of the previous array in Q8?

# In[56]:


a = np.random.random((5, 6))
print(a)
b = np.std(a)
print("\n\n Standard Deviation of Array is: ", b)


# ## Question:10

# ### Find the median of the previous array in Q8?

# In[57]:


a = np.random.random((5, 6))
print(a)
b = np.median(a)
print("\n\n Median of Array is: ", b)


# ## Question:11

# ### Find the transpose of the previous array in Q8?

# In[61]:


a = np.random.random((5, 6))
print(a)
b = np.transpose(a)
print("\n\n Transpose of Array is: ", "\n\n", b)


# ## Question:12

# ### Create a 4x4 an array and find the sum of diagonal elements?

# In[60]:


a = np.random.random((4, 4))
print(a)
b = np.diagonal(a)
print("\n\n Sum of Diagonal Elements is: ", "\n\n", b)


# ## Question:13

# ### Find the determinant of the previous array in Q12?

# In[66]:


a = np.random.random((4, 4))
print(a)
b = np.linalg.det(a)
print("\n\n Determinent of Array is: ", "\n\n", b)


# ## Question:14

# ### Find the 5th and 95th percentile of an array?

# In[71]:


a = np.arange(3, 20)
print(a)
b = np.percentile(a, 5)
print("\n\n 5th Percentile of Array is: ", "\n\n", b)
c = np.percentile(a, 95)
print("\n\n 95th Percentile of Array is: ", "\n\n", c)


# ## Question:15

# ### How to find if a given array has any null values?

# In[77]:


a = np.arange(0, 20).reshape(5, 4)
print(a)
print("\n\n Looking for Null Values: \n\n", np.isnan(a))

b = np.arange(15).reshape(5, 3)
print("\n\n", b)
print("\n\n Looking for Null Values: \n\n", np.isnan(b))

