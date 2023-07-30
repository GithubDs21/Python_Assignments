#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().run_line_magic('pinfo', 'function')

a lambda function is a small anonymous function that can have any number of arguments but can only have one expression.
Lambda functions are often used when you need a simple, short-lived function for a specific task and
do not want to define a separate regular function using the def keyword.
Lambda functions have a few key differences when compared to regular functions (defined using def)

Syntax: As shown above, lambda functions use the lambda keyword followed by the arguments and a single expression
     Regular functions use the def keyword, a name for the function, arguments within parentheses, a colon,
        and then the function's body with one or more statements.
        
Function Name: Lambda functions are anonymous; they don't have a specific name

Number of Expressions: Lambda functions are limited to a single expression, which means they cannot contain multiple statements 
    or complex logic   

Regular functions, on the other hand, can have multiple expressions and more complex logic. 
They are generally used for defining reusable blocks of code that can be called multiple times throughout the program.    


# In[ ]:





# In[ ]:


2. Can a lambda function in Python have multiple arguments? If yes, how can you define and use
get_ipython().run_line_magic('pinfo', 'them')
yes , it takes multiple arguments.
Lambda functions are often used in conjunction with higher-order functions like map(), filter(),
and reduce() to apply the lambda function to a sequence of data.
an example using map():

lambda functions are useful for simple and short operations, for more complex and reusable functions, 
it's better to use regular functions defined with the def keyword.


# In[3]:


numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x ** 2, numbers)


# In[ ]:





# In[ ]:


3. How are lambda functions typically used in Python? Provide an example use case.

Lambda functions provide a concise way to define simple operations on the fly, 
especially when you need to use them as arguments in higher-order functions or
in situations where a full-fledged regular function might be unnecessary or less readable.



# In[4]:


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)


# In[ ]:





# In[ ]:


4. What are the advantages and limitations of lambda functions compared to regular functions in
get_ipython().run_line_magic('pinfo', 'Python')

LAMBDA Advantages: 
1) Lambda functions allow you to define simple functions in a single line of code, 
   making the code more compact and easier to read when the logic is straightforward.
2) Lambda functions are anonymous, meaning they don't require a specific name. 
    They are often used when you need a small function for a short-lived task without
    the need to define a full function using the def keyword.
3) Lambda functions are commonly used with higher-order functions like map(), filter(), and reduce(), 
   where a short function is needed as an argument.
4) When used judiciously, lambda functions can improve the readability of your code by expressing simple operations more concisely.

LAMBDA Limitations
1) single expression :  Lambda functions are limited to a single expression, 
    meaning they cannot contain multiple statements or complex logic.
    As a result, they are best suited for short, simple tasks.
2) Limited functionality:
    Due to their concise nature, lambda functions lack some features of regular functions,
    such as documentation strings (docstrings) and default argument values.
3) Reduced readability with complex logic
    Using lambda functions for complex operations might decrease code readability,
    as cramming complex logic into a single expression can be hard to understand.
4) debugging difficulties
    Since lambda functions are anonymous, debugging can be more challenging. 
    Error messages might refer to lambda functions by their memory address rather than a descriptive name.


Regular function Advantages & limitations
1)Multiple Expressions: Regular functions can contain multiple expressions,
    allowing for more complex logic and better code organization.
    
2)Named Functions: Regular functions have names, making it easier to identify them in error messages and 
    improve code readability.
3)Docstrings and Function Attributes: Regular functions can have docstrings (documentation strings)
     to provide descriptive information and 
    can also include custom attributes. 
4)Reusability: Regular functions can be reused in multiple parts of your code,
    making them more versatile for complex operations.
    
Limitations:
1)More Verbose: Regular functions often require more lines of code to define, 
   which might lead to more verbose code for simple tasks.
2) Less Suitable for Short-Lived Tasks: Creating a regular function for a one-time,
    small task can add unnecessary complexity to your code.


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'scope')
Explain with an example.

Yes, lambda functions in Python can access variables that are defined outside of their own scope. Lambda functions have access to variables from the containing scope where they are created.
This is known as "lexical scoping" or "closure.


# In[9]:


def outer_fuct(x):
    y=10
    inner_lambda=lambda a:a+y+x
    return inner_lambda


# In[14]:


closure_function = outer_fuct(5)
result=closure_function(25)
result


# In[ ]:





# In[ ]:


6. Write a lambda function to calculate the square of a given number.


# In[19]:


square= lambda x:x**2 
square(5)


# In[ ]:





# In[ ]:


7. Create a lambda function to find the maximum value in a list of integers.


# In[20]:


find_max=lambda list_:max(list_)


# In[21]:


numbers=[1,500,48,677,19,15826,4975]


# In[22]:


find_max(numbers)


# In[ ]:





# In[ ]:


8. Implement a lambda function to filter out all the even numbers from a list of integers.


# In[31]:


numbers=[1,500,48,677,19,15826,4975]
filter_even = lambda list_:list(filter(lambda x: x % 2==0,list_))
even_numbers=filter_even(numbers)
print(even_numbers)


# In[ ]:





# In[ ]:


9. Write a lambda function to sort a list of strings in ascending order based on the length of each
string.


# In[32]:


sort_by_length = lambda lst: sorted(lst, key=lambda x: len(x))


# In[33]:


words = ['apple', 'banana', 'orange', 'grape', 'kiwi', 'pear']
sorted_words = sort_by_length(words)
print(sorted_words)


# In[ ]:





# In[ ]:


10. Create a lambda function that takes two lists as input and returns a new list containing the
common elements between the two lists.


# In[34]:


find_common_elements = lambda list1, list2: list(filter(lambda x: x in list2, list1))
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = find_common_elements(list1, list2)
print(common_elements) 


# In[ ]:





# In[ ]:


11. Write a recursive function to calculate the factorial of a given positive integer.


# In[35]:


def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)


# In[37]:


factorial(5)


# In[ ]:





# In[ ]:


12. Implement a recursive function to compute the nth Fibonacci number.


# In[ ]:


def fibonacci(n):
    if n <= 0:
        raise ValueError("Fibonacci sequence is only defined for positive integers.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# In[ ]:





# In[ ]:


13. Create a recursive function to find the sum of all the elements in a given list.


# In[41]:


def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])
print(recursive_sum([]))    


# In[45]:


print(recursive_sum([1, 2, 3, 4, 5])) ,
print(recursive_sum([10, 20, 30, 40]))


# In[ ]:





# In[ ]:





# In[ ]:


14. Write a recursive function to determine whether a given string is a palindrome.


# In[47]:


def is_palindrome(s):
    # Base case: If the string is empty or has only one character, it is a palindrome.
    if len(s) <= 1:
        return True
    # Recursive case: Compare the first and last characters of the string.
    # If they are equal, check the palindrome property for the substring between them.
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


# In[48]:


print(is_palindrome("radar"))       # Output: True (Palindrome: reads the same backward)
print(is_palindrome("level"))       # Output: True (Palindrome)
print(is_palindrome("python"))      # Output: False (Not a palindrome)
print(is_palindrome("racecar"))     # Output: True (Palindrome)
print(is_palindrome("step on no pets")) # Output: True (Palindrome, considering spaces)


# 15. Implement a recursive function to find the greatest common divisor (GCD) of two positive integers

# In[50]:


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# In[51]:


gcd(12,18)


# In[53]:


mcd(12,18)

