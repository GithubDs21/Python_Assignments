#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'them')

True and False


# In[ ]:


get_ipython().run_line_magic('pinfo', 'operators')
and , or, not


# In[ ]:


3. Make a list of each Boolean operator s truth tables (i.e. every possible combination of Boolean values for the operator and what it evaluate ).

AND 
True and True = True
True and False = False
False and True = False
False and False = False

OR
True or True = True
True or False = True
False or True = False
Fasle or False = False

NOT
not True = False
not False = True


# In[ ]:


get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)                : False
not (5 > 4)                         : False
(5 > 4) or (3 == 5)                 : True
not ((5 > 4) or (3 == 5))           : False
(True and True) and (True == False) : False
(not False) or (not True)           : True


# In[ ]:


get_ipython().run_line_magic('pinfo', 'operators')
=
>
<
>=
<=
!=


# In[ ]:


6. How do you tell the difference between the equal to and assignment operators?Describe a condition and when you would use one.
equal to == is compare two values 
assignment operator is =  in this value can be asigned to a particular variable


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

in every print statement there is indentation required.


# In[12]:


spam = 0
if spam == 10:
    print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
    print('spam')


# In[ ]:


8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.

spam=input()
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")


# In[17]:


spam=int(input("Entered number is :"))
if spam==1:
    print("Hello")
elif spam==2:
    print("Howdy")
else:
    print("Greetings!")


# In[ ]:


get_ipython().run_line_magic('pinfo', 'press')
control + C


# In[ ]:


get_ipython().run_line_magic('pinfo', 'continue')
break statement will move the execution outside and just after a loop.
continue statement will move the execution to the start of the loop.


# In[ ]:


11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?

range(10) : [i for i in range(10)] => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
range(0, 10) : [i for i in range(0,10)] => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
and range(0, 10, 1) :[i for i in range(0,10,1)] => [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    iteration start from 0 & end point is 10 means will execute till 9


# In[ ]:


12. Write a short program that prints the numbers 1 to 10 using a for loop. 
Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for loop >>> [i for i in range(11)]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
 
While Loop >>> 


# In[29]:


i=1
while i<=10:
    print(i)
    i=i+1


# In[ ]:


get_ipython().run_line_magic('pinfo', 'spam')

spam.bacon()

