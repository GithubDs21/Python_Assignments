#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * : expression
# 'hello'value string
# -87.8  value float
# -      expression
# /      expression
# +      expression
# 6      value int

# 2. What is the difference between string and variable?
# Variable means in which value can be stored where as string is data type of the variable.
# 

# 3. Describe three different data types.
# String-it is a data type where we can store text
# Integer – it is a data type in which whole numbers get stored
# Float – in this data type decimal figures is considered with integer . 

# 4. What is an expression made up of? What do all expressions do?
# Expressions are mathematical operators , mathematical operations can be done with the help of these expression.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'statement')


# In[2]:


#6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[4]:


#7. What should the values of the following two terms be?
print('spam' + 'spamspam')
print('spam' * 3)


# 8. Why is eggs a valid variable name while 100 is invalid?
# 
# Ans : Because variable names cannot begin with a number

# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
# int()
# float()
# str()

# In[ ]:


get_ipython().run_line_magic('pinfo', 'it')
'I have eaten ' + 99 + ' burritos.'

in this 99 , we have to convert it into str then & then we can concatenate all these 3 elements.


we can not add two datatypes together like if i want to make an addition of [5 + "DS"] here in this example
data type of 5 is int and data type of "DS" is str so python will not allow to add them.


# In[5]:


"I have eaten"+str(99)+"burritos"


# In[ ]:




