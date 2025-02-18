#!/usr/bin/env python
# coding: utf-8

# # Mean-Variance-Standard Deviation Calculator
# 
# This is a (mini) Python project, completed as part of the requirements for the **Data Analysis with Python** certification from [freeCodeCamp.com](https://www.freecodecamp.org/learn/data-analysis-with-python/).
# 

# ## Project Instructions

# Create a function named `calculate()` in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
# 
# The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.
# 
# The returned dictionary should follow this format:
# ```
# {
#   'mean': [axis1, axis2, flattened],
#   'variance': [axis1, axis2, flattened],
#   'standard deviation': [axis1, axis2, flattened],
#   'max': [axis1, axis2, flattened],
#   'min': [axis1, axis2, flattened],
#   'sum': [axis1, axis2, flattened]
# }
# ```
# If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.
# 
# The instructions for building the project can be found at [freeCodeCamp](https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/mean-variance-standard-deviation-calculator).

# ## Code Solution

# The project is fairly simple and straightforward.
# 
# It basically requires importing the `NumPy` library and using its statistical methods (`mean`, `std`, `max`, `min`, etc.) to calculate the required values. The methods have an `axis` argument that can be used to specify calculations along the rows or columns (or `None` to flatten the array).
# 
# An `if` statement is used to check the input constraint (i.e. 9 numbers in the list), and a `ValueError` message is raised if this condition is not satisfied. Although not specified as a constraint, a `for loop` is also added to check that the list contains only float or integer types.
# 
# The code for the `calculate()` function:

# In[1]:


# Import NumPy
import numpy as np


# In[2]:


# The calculate function
def calculate(xlist):
    if not len(xlist) == 9: # Tests that input has 9 elements
        raise ValueError("List must contain nine numbers.")
    for i in xlist:
        if not isinstance(i, (float, int)):
            raise ValueError("List must contain only numbers.")

    # Convert the input list in a 3x3 NumPy array
    xarray = np.array([xlist[i:i+3] for i in range(0,len(xlist),3)])
    
    axes = [0, 1, None] # Axes along which do the statistical calculations

    # Perform the statistical caluclations as list comprehensions
    mean = [np.mean(xarray, axis=i).tolist() for i in axes]
    var = [np.var(xarray, axis=i).tolist() for i in axes]
    std = [np.std(xarray, axis=i).tolist() for i in axes]
    maxx = [np.max(xarray, axis=i).tolist() for i in axes]
    minn = [np.min(xarray, axis=i).tolist() for i in axes]
    summ = [np.sum(xarray, axis=i).tolist() for i in axes]

    # Return a dictionary of the calculations
    return {'mean': mean, 'variance': var,'standard deviation': std, 'max': maxx,'min': minn,'sum': summ}    


# ## Some code tests

# In[ ]:


# Code test 01
calculate([2,3,4,5,2,5,7,11,4])


# In[ ]:


# Code test 02
calculate([2,3,4,'r',2,5,7,11,4])


# In[ ]:


# Code test 03
calculate([2,3,4,5,2,5,7,11,])

