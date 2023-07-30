#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'block')

    The try and except block in Python is used for exception handling. It allows you to handle errors and 
    exceptions that might occur during the execution of your code. 
    When a potential error-prone section of code is placed inside a try block, Python tries to execute it. 
    If an exception occurs during the execution of the try block, the program jumps to the corresponding except block, 
    where you can handle the exception gracefully.


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'block')


# In[3]:


try:
    num1 = int(input("Enter the numerator: "))
    num2 = int(input("Enter the denominator: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid integers.")


# In[ ]:





# In[ ]:


3. What happens if an exception occurs inside a try block and there is no matching
get_ipython().run_line_magic('pinfo', 'block')

    If an exception occurs inside a try block and there is no matching except block to handle that specific type of exception,
    the program will terminate, and an error message will be displayed. 
    The error message will include a traceback, which shows the sequence of function calls and 
    code lines that led to the unhandled exception.


# In[ ]:





# In[ ]:


4. What is the difference between using a bare except block and specifying a specific
get_ipython().run_line_magic('pinfo', 'type')


# In[4]:


# Bare
try:
    result = 10 / 0
except:
    print("An error occurred.")


# In[5]:


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")


# In[ ]:





# In[ ]:





# In[ ]:


5. Can you have nested try-except blocks in Python? If yes, then give an example.


# In[6]:


def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero!")

    except TypeError:
        print("Error: Invalid input type!")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divide_numbers(num1, num2)

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")


# In[ ]:





# In[ ]:


6. Can we use multiple exception blocks, if yes then give an example.
    Yes, you can use multiple except blocks to handle different types of exceptions in Python. 
    This allows you to provide specific error handling
    for each type of exception that might occur in the try block.


# In[10]:


def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)

    except ZeroDivisionError:
        print("Error: Division by zero!")

    except TypeError:
        print("Error: Invalid input type!")

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divide_numbers(num1, num2)

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")


# In[ ]:





# In[ ]:





# In[ ]:


7. Write the reason due to which following errors are raised:
a. EOFError
        This error is raised when an input operation reaches the end of a file unexpectedly. 
        It typically occurs when using functions like input() or raw_input() for reading input from the user,
        and the user terminates the input stream (e.g.,
        by pressing Ctrl+D or Ctrl+Z in the terminal or console)

b. FloatingPointError
        This error is raised when a floating-point arithmetic operation fails to produce a valid result. It can occur,
        for example, when dividing by zero or
        when performing invalid mathematical operations on floating-point numbers.
        
c. IndexError
        This error is raised when trying to access an invalid index in a sequence (e.g., list, tuple, string).
        It occurs when you attempt to access an element at an index that is out of range or not present in the sequence.

d. MemoryError
        This error is raised when an operation fails due to a lack of memory resources. 
        It occurs when your program tries to allocate more memory than the system can provide, 
        resulting in the inability to allocate further memory.
e. OverflowError
        This error is raised when an arithmetic operation exceeds the maximum representable value for a numeric type. 
        It occurs when a number becomes too large to be stored within the limits of the data type.
        
f. TabError
        This error is raised when inconsistent use of tabs and spaces is encountered in indentation.
        It occurs when you mix tabs and spaces to indent code, leading to indentation errors.
g. ValueError
        This error is raised when a built-in operation or function receives an argument of the correct data type
        but with an inappropriate value. For example, trying to convert a string that cannot be represented as 
        an integer using int() or providing an incorrect argument to a function that
        expects a specific range of values may raise a ValueError


# In[ ]:





# In[ ]:


8. Write code for the following given scenario and add try-exception block to it.
a. Program to divide two numbers
b. Program to convert a string to an integer
c. Program to access an element in a list
d. Program to handle a specific exception
e. Program to handle any exception


# In[11]:


# a. Program to divide two numbers:
def divide_numbers(a, b):
    try:
        result = a / b
        print("Division result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

# Test case
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")


# In[17]:


# b. Program to convert a string to an integer:
def convert_to_integer(s):
    try:
        integer_value = int(s)
        print("Converted integer:", integer_value)
    except ValueError:
        print("Error: Invalid input. The string cannot be converted to an integer.")

# Test case
input_string = input("Enter a string: ")
convert_to_integer(input_string)


# In[20]:


#c. Program to access an element in a list:
def access_list_element(lst, index):
    try:
        element = lst[index]
        print("Element at index", index, ":", element)
    except IndexError:
        print("Error: Index out of range. The list does not have an element at index", index)

# Test case
my_list = [10, 20, 30, 40, 50,60,70,80,90,100]
try:
    index = int(input("Enter an index to access the list element: "))
    access_list_element(my_list, index)
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")


# In[21]:


#d. Program to handle a specific exception:
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 / num2
    print("Division result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter valid integers.")


# In[ ]:




