#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Q.1. Create two int type variables, apply addition, subtraction, division and multiplications
and store the results in variables. Then print the data in the following format by calling the
variables:
First variable is __ & second variable is __.
Addition: __ + __ = __
Subtraction: __ - __ = __
Multiplication: __ * __ = __
Division: __ / __ = __


# In[1]:


n1=int(input("Enter number is :"))
n2=int(input("Enter number is :"))
print(f"fisrt variable is ={n1} and second variable is ={n2}")
print(f"Addition :{n1}+{n2} is=",n1+n2)
print(f"subtraction :{n1}-{n2} is=",n1-n2)
print(f"Multiplication :{n1}*{n2} is=",n1*n2)
print(f"Division :{n1}/{n2} is=",n1/n2)


# In[ ]:





# In[ ]:


Q.2. What is the difference between the following operators:
(i) ‘/’ & ‘//’
(ii) ‘**’ & ‘^’


# In[2]:


print(11/3) # Normal division
print(11//3) #  floor division.


# In[ ]:





# In[ ]:


Q.3. List the logical operators.
Python has three logical operators: and , or , and no


# In[ ]:




Q.4. Explain right shift operator and left shift operator with examples.
right-shift operator ( >> ), which moves the bits of an integer or enumeration type expression to the right
left-shift operator ( << ), which moves the bits to the left
# In[ ]:





# In[ ]:


Q.5. Create a list containing int type data of length 15. Then write a code to check if 10 is
present in the list or not.


# In[3]:


l1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

i=10
if i in l1:
    print("10: is present in the given list")
else:
    print("10: is not in the list")


# In[ ]:




