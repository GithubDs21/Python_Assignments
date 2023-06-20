#!/usr/bin/env python
# coding: utf-8

# # Q1

# In[ ]:


get_ipython().run_line_magic('pinfo', 'like')

{}


# # Q2

# In[ ]:


What is the value of a dictionary value with the key 'foo' and the value 42?

{"foo":42}


# # Q3

# In[ ]:


get_ipython().run_line_magic('pinfo', 'list')

Dictionary has key & pair whereas list has collection of elements which may be with different data types


# # Q4

# In[ ]:


4.What happens if you try to access spam['foo'] if spam is {'bar': 100}?

Error


# # Q5

# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?


There is no difference. The in operator checks whether a value exists as a key in the dictionary


# # Q6

# In[ ]:


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() 
checks whether there is a value 'cat' for one of the keys in spam


# # Q7

# In[ ]:


get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'


spam.setdefault('color', 'black')


# # Q8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'function')


pprint.pprint()

