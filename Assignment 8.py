#!/usr/bin/env python
# coding: utf-8
1. In Python, what is the difference between a built-in function and a user-defined function? Provide an
example of each.
# If you define any function yourself, it is a user-defined function. Wherein, the Python function that come along with Python are known as in-built functions
# 
# Python inbuilt  function = print() , range() etc..
# python user defined function like addition of any two or more numbers using def keyword.

# 
2. How can you pass arguments to a function in Python? Explain the difference between positional
arguments and keyword arguments.


# Positional arguments must be included in the correct order. 
# Keyword arguments are included with a keyword and equals sign.

# In[ ]:




3. What is the purpose of the return statement in a function? Can a function have multiple return
statements? Explain with an example.


# A return statement is used to end the execution of the function call and “returns” the result (value of the expression following the return keyword) to the caller. The statements after the return statements are not executed.
# Multiple return statements may exist in a function, but only the one that fulfils the specified condition first is executed.

# In[ ]:




4. What are lambda functions in Python? How are they different from regular functions? Provide an
example where a lambda function can be useful.

# A lambda function is an anonymous function  that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression.For example, you can use Lambda for: File processing:  Use Amazon Simple Storage Service (Amazon S3) to trigger Lambda data processing in real time after an upload.
5. How does the concept of "scope" apply to functions in Python? Explain the difference between local
scope and global scope.

# There are two types of variables: global variables and local variables. The scope of global variables is the entire program whereas the scope of local variable is limited to the function where it is defined

# In[ ]:




6. How can you use the "return" statement in a Python function to return multiple values?

# To do that, you just need to supply several return values separated by commas.

# In[ ]:




7. What is the difference between the "pass by value" and "pass by reference" concepts when it
comes to function arguments in Python?

# When you give function parameters via reference, you're just passing references to values that already exist. When you pass arguments by value, on the other hand, the arguments become independent copies of the original values

# In[ ]:




8. Create a function that can intake integer or decimal value and do following operations:
a. Logarithmic function (log x)
b. Exponential function (exp(x))
c. Power function with base 2 (2x)
d. Square root

# In[39]:


def logarithmic(X):
    import math as m
    return (f"logrithm of {X} is:",m.log(X))


# In[47]:


def exponential(X):
    import math as m
    return (f"exponential of {X} is:",m.exp(X))


# In[48]:


def power(X,Y):
    import math as m
    return (f"base {X} power {Y} and square is :",m.pow(X,Y))


# In[49]:


def sqare_root(X):
    import math as m
    return (f"square root of {X} is",m.sqrt(X))


# In[51]:


logarithmic(2),exponential(1),power(4,2),sqare_root(4)

9. Create a function that takes a full name as an argument and returns first name and last name
# In[23]:


def full_name(x):
    A=x.split()
    f_n=A[0]
    l_n=A[2]
    return f_n,l_n


# In[24]:


full_name("suryakant Aaram Mhaske")


# In[ ]:




