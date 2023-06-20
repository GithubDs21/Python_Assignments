#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q.1. What are keywords in python? Using the keyword library, print all the python keywords.

Keywords are reserve words in python & user can not use them as a variable.


# In[25]:


#!pip install keywords
import keyword
a=keyword.kwlist
b=len(a)
print("these number of key words are in python",{b}, a)


# In[ ]:




Q.2. What are the rules to create variables in python?

A variable name must start with a letter or the underscore character.
A variable name cannot start with a number.
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (City, CITY and city are three different variables)

# In[ ]:





# In[ ]:


Q.3. What are the standards and conventions followed for the nomenclature of variables in
get_ipython().run_line_magic('pinfo', 'maintainability')


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'name')
We cannot use a keyword as a variable name, function name, or any other identifier


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'used')
for creation of functions


# In[ ]:





# In[ ]:


Q.6. What is the operation of this special character ‘\’?

Backslash: Separates locations in a file or network path


# In[ ]:





# In[ ]:


Q.7. Give an example of the following conditions:
(i) Homogeneous list  : it only contains a single type of data. [1,2,3,4,5]
(ii) Heterogeneous set :Heterogeneous Data Structure – Data elements may not be of same data type (ex -List, Tuples, Sets etc)
(iii) Homogeneous tuple : contains a single type of data (3.14,6.15,2.5)


# In[ ]:





# In[ ]:


Q.8. Explain the mutable and immutable data types with proper explanation & examples.
   
Immutable datatypes are objects that cannot be modified or altered after they have been created 
(for example, by adding new elements, removing elements, or replacing elements). 
Python's immutable data types are: Int. Float. Tuple    


# In[ ]:





# In[ ]:


Q.9. Write a code to create the given structure using only for loop.
*
***
*****
*******
*********


# In[42]:


rows=6
for i in range(rows): 
   
    for j in range(i):
       
        print("*", end='')
    
    print('')


# In[ ]:





# In[ ]:


Q.10. Write a code to create the given structure using while loop.
|||||||||
|||||||
|||||
|||
|


# In[45]:


n = int(input('Enter number of rows : '))
 
i = 1
while i <= n :
    j = n
    while j >= i:
        print("|", end = "")
        j -= 1
    print()
    i += 1


# In[ ]:




