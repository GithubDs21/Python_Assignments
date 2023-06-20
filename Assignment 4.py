#!/usr/bin/env python
# coding: utf-8

# # Q1

# 1. What exactly is []?
# empty List
# example of elements in the list 
# List_1=[1,2,3,4,5]
# 

# # Q2

# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? (Assume [2, 4, 6, 8, 10] are in spam.)
Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.


# In[4]:


spam=[2, 4, 6, 8, 10]
spam[2]="Hello"
spam


# # Q 3

# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?


# In[5]:


[int(int('3' * 2) / 11)]


# In[7]:


a=int('3' * 2)


# In[8]:


a/11


# # Q 4. 

# In[16]:


get_ipython().run_line_magic('pinfo', 'spam[-1]')
spam=['a', 'b', 'c', 'd']


# In[17]:


spam[-1]


# # Q5

# In[ ]:


5. What is the value of spam[:2]?
Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.


# In[15]:


spam=[3.14, 'cat', 11, 'cat', True]
spam[:2]


# # Q6

# In[24]:


#6. What is the value of bacon.index('cat')?
bacon=[3.14, 'cat', 11, 'cat', True]
bacon.index('cat')
    


# 
# # Q7

# In[25]:


#7. How does bacon.append(99) change the look of the list value in bacon?

bacon.append(99)
bacon


# # Q8

# In[30]:


#8. How does bacon.remove('cat') change the look of the list in bacon?

try:
    bacon=[3.14, 'cat', 11, 'cat', True,99]
    bacon.remove('cat')
    print(bacon)
except:
    print("the element is not in the list")


# In[34]:


set(bacon)


# # Q9

# In[39]:


#9. What are the list concatenation and list replication operators?

# Concatination
list_1=[1,2,3]
list_2=[4,5,6]
list_3=list_1+list_2
print(list_3)

#Replication
list_1*3


# # Q10

# In[47]:


#10. What is difference between the list methods append() and insert()?

l1=[1,2,3]
l1.append(4)

print("this element is appended :",l1)

l1.insert(4,"surya")
print("this element is inserted:",l1)
(in insert we can specify the position where to place the element)


# # Q11

# In[58]:


#11. What are the two methods for removing items from a list?
l1=[1,2,"a","h"]
l1.pop()
print(l1)



# In[56]:


try:
    l1=[1,2,3]
    l1.remove(1)
    print(l1)
except:
    print("the element is not there in the list")


# # Q12

# In[ ]:


12. Describe how list values and string values are identical.
Both lists and strings can be passed to len(), have indexes and slices, 
be used in for loops, be concatenated or replicated, and be used with the in and not in operators


# # Q13

# In[ ]:


get_ipython().run_line_magic('pinfo', 'lists')
Lists are mutable; they can have values added, removed, or changed. 
Tuples are immutable; they cannot be changed at all.
Also, tuples are written using parentheses, ( and ),
while lists use the square brackets, [ and ].


# # Q14

# In[60]:


#14. How do you type a tuple value that only contains the integer 42?
x=(42) 
print(x)


# # Q15

# In[ ]:


get_ipython().run_line_magic('pinfo', 'form')
The tuple() and list() functions, respectively

l1=[1,2,3,4,5]
l1.tuple()


# In[62]:


l1=[1,2,3,4,5]
tuple(l1)


# In[63]:


t1=(1, 2, 3, 4, 5)
list(t1)


# # Q16

# In[ ]:


get_ipython().run_line_magic('pinfo', 'contain')
They contain references to list values.


# # Q17

# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?
The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() 
function will do a deep copy of a list. That is, only copy.deepcopy() will duplicate any lists inside the list.


# In[ ]:





# In[ ]:





# In[ ]:




