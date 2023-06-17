#!/usr/bin/env python
# coding: utf-8
1. Why are functions advantageous to have in your programs?

Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update
2. When does the code in a function run: when it's specified or when it's called?
The code in a function executes when the function is called, not when the function is defined.
# In[ ]:


get_ipython().run_line_magic('pinfo', 'function')
The def statement defines (that is, creates) a function.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'call')
A function call is what moves the program execution into the function, 
and the function call evaluates to the function’s return value.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'scopes')
There is one global scope, and a local scope is created whenever a function is called.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'returns')
When a function returns, the local scope is destroyed, and all the variables in it are forgotten.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'expression')
A return value is the value that a function call evaluates to. Like any value,
a return value can be used as part of an expression.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'function')
If there is no return statement for a function, its return value is None.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'variable')
A global statement will force a variable in a function to refer to the global variable.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'None')
The data type of None is NoneType.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'do')
That import statement imports a module named areallyourpetsnamederic. (This isn’t a real Python module, by the way.)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'spam')
This function can be called with spam.bacon().


# In[ ]:


get_ipython().run_line_magic('pinfo', 'error')
Place the line of code that might cause an error in a try clause.


# In[ ]:


get_ipython().run_line_magic('pinfo', 'clause')
The code that could potentially cause an error goes in the try clause.

The code that executes if an error happens goes in the except clause.

