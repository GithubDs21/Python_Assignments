#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Explain what inheritance is in object-oriented programming and why it is used.


# In[ ]:


In object-oriented programming (OOP), inheritance is a fundamental concept that allows a class (known as a subclass or derived class) to inherit properties and behavior (attributes and methods) from another class (known as a superclass or base class). The subclass can extend or customize the functionality of the superclass by adding its own unique attributes and methods or by modifying the inherited ones.

Here's a more detailed explanation of inheritance and its purpose:

1. **Inheritance Relationship:**
   Inheritance establishes an "is-a" relationship between classes. It implies that a subclass is a specialized version of the superclass, sharing its characteristics but with additional features or modifications.

2. **Code Reusability:**
   One of the primary benefits of inheritance is code reusability. By defining common attributes and methods in a superclass, multiple subclasses can inherit and use them without duplicating code. This promotes a more efficient and maintainable codebase.

3. **Extending and Specialization:**
   Subclasses can extend the functionality of the superclass by adding new attributes and methods. They can also override the behavior of inherited methods to suit their specific requirements. This enables customization and specialization of behavior while maintaining a common foundation.

4. **Hierarchy and Organization:**
   Inheritance allows for the creation of class hierarchies, where more specialized classes (subclasses) can be organized under more general, abstract classes (superclasses). This hierarchy facilitates conceptual organization and helps developers understand the relationships between different types of objects in the system.

5. **Polymorphism:**
   Inheritance is closely related to polymorphism, another important OOP concept. Polymorphism allows objects of different classes (including subclasses and superclasses) to be treated as objects of a common parent class, enabling more flexible and generic programming.

6. **Modularity and Maintenance:**
   Inheritance promotes a modular approach to software development. Changes or updates made in a superclass are automatically inherited by its subclasses, reducing the need for redundant modifications and improving maintainability.

7. **Abstraction and Encapsulation:**
   Inheritance contributes to achieving the principles of abstraction and encapsulation in OOP. Abstraction allows for defining a common interface and behavior for subclasses, while encapsulation ensures that the internal implementation details of the superclass are hidden from the subclasses.

In summary, inheritance in OOP helps in code reuse, extending functionality, organizing classes in a hierarchy, achieving polymorphism, and adhering to the principles of modularity, abstraction, and encapsulation. It's a powerful tool for creating efficient, flexible, and maintainable software systems.


# In[ ]:





# In[ ]:


2. Discuss the concept of single inheritance and multiple inheritance, highlighting their
differences and advantages.


# In[ ]:


In object-oriented programming (OOP), inheritance is broadly categorized into two main types: single inheritance and multiple inheritance. Let's delve into each of these concepts, outlining their differences and advantages:

### Single Inheritance:

**Definition:**
Single inheritance refers to a scenario where a derived class (subclass) inherits properties and behavior from only one base class (superclass). The subclass extends the functionality of the base class by adding new attributes and methods or by overriding existing ones.

**Example:**

```python
class Animal:
    def sound(self):
        return "Making a sound"

class Dog(Animal):
    def sound(self):
        return "Barking"
```

In this example, `Dog` is a subclass of `Animal`, demonstrating single inheritance.

**Advantages:**

1. **Simplicity:**
   Single inheritance is straightforward and easier to implement, understand, and manage. The relationship between classes is simpler to visualize and conceptualize.

2. **Reduced Complexity:**
   With only one parent class, the complexity of the inheritance hierarchy is limited, making the codebase more manageable and less prone to conflicts.

3. **Avoiding Diamond Problem:**
   The diamond problem is a complication related to multiple inheritance (discussed later). Single inheritance completely avoids this problem, as there's only one direct parent class.

### Multiple Inheritance:

**Definition:**
Multiple inheritance occurs when a derived class (subclass) inherits properties and behavior from more than one base class (superclass). The subclass combines and extends the functionality of multiple base classes.

**Example:**

```python
class Animal:
    def sound(self):
        return "Making a sound"

class Dog(Animal):
    def sound(self):
        return "Barking"

class Bird(Animal):
    def sound(self):
        return "Chirping"

class DogBird(Dog, Bird):
    pass
```

In this example, `DogBird` is a subclass of both `Dog` and `Bird`, illustrating multiple inheritance.

**Advantages:**

1. **Code Reusability:**
   Multiple inheritance facilitates the reuse of code from multiple parent classes. The subclass can inherit attributes and methods from different sources, promoting code reuse and reducing redundancy.

2. **Flexibility and Extensibility:**
   Subclasses can combine features and behaviors from different parent classes, allowing for a more flexible and extensible design. This enables the creation of specialized classes with a diverse set of functionalities.

3. **Modeling Real-World Relationships:**
   Multiple inheritance is useful when real-world entities have multiple types of relationships. For example, a `FlyingDog` class might inherit from both `Dog` and `Bird`, representing an entity that shares characteristics of both.

**Differences:**

1. **Number of Parents:**
   The fundamental difference is that single inheritance involves inheriting from only one parent class, while multiple inheritance involves inheriting from more than one parent class.

2. **Complexity:**
   Multiple inheritance is inherently more complex due to the potential for conflicts (like the diamond problem) and the need to manage interactions and dependencies between multiple parent classes.

In summary, single inheritance offers simplicity and ease of understanding, while multiple inheritance provides code reusability, flexibility, and the ability to model complex relationships. The choice between them depends on the specific requirements of the application and the design goals. It's important to carefully consider the trade-offs and choose the appropriate inheritance model accordingly.


# In[ ]:





# In[ ]:


3. Explain the terms "base class" and "derived class" in the context of inheritance.


# In[ ]:


In the context of inheritance in object-oriented programming (OOP), "base class" and "derived class" are fundamental concepts that define the parent-child relationship between classes.

### Base Class:

A base class, also known as a parent class or superclass, is a class that provides a common set of attributes (data members) and methods (functions) to be inherited by one or more subclasses. It serves as a blueprint or template for creating more specialized types of classes.

**Characteristics of a Base Class:**

1. **Provides a Foundation:** The base class defines the common behavior, attributes, and methods that are shared by its subclasses.

2. **May Have Abstract or Concrete Methods:** Base classes can contain abstract methods (methods without an implementation) that must be implemented by subclasses, or they can have concrete implementations that can be inherited as-is or overridden.

3. **Can Be Instantiated:** In many cases, a base class can be instantiated to create objects. However, it's also common for base classes to be abstract, meaning they cannot be instantiated on their own but are intended to be subclassed.

### Derived Class:

A derived class, also known as a child class or subclass, is a class that inherits attributes and methods from a base class. The derived class extends or specializes the behavior of the base class by adding new attributes, methods, or by modifying the existing inherited members.

**Characteristics of a Derived Class:**

1. **Inherits from a Base Class:** The derived class explicitly declares its inheritance from a specific base class, indicating that it is extending the functionality provided by that base class.

2. **Can Add New Functionality:** The derived class can have additional attributes and methods that are unique to it, providing specialized behavior beyond what's inherited from the base class.

3. **Can Override Inherited Behavior:** The derived class can override (redefine) inherited methods from the base class, allowing it to customize the behavior to suit its specific needs.

**Example:**

```python
class Animal:  # Base class
    def make_sound(self):
        print("Animal sound")

class Dog(Animal):  # Derived class inheriting from Animal
    def make_sound(self):
        print("Bark")

# Creating instances of the derived class
animal_instance = Animal()
dog_instance = Dog()

dog_instance.make_sound()  # Output: Bark
```

In this example, `Animal` is the base class, and `Dog` is the derived class inheriting from `Animal`.

In summary, a base class is a generic class that provides a common set of attributes and methods, serving as a foundation for one or more specialized derived classes. A derived class is a class that inherits attributes and methods from a base class, extending and customizing the behavior to create specialized types of objects.


# In[ ]:





# In[ ]:


4. What is the significance of the "protected" access modifier in inheritance? How does
get_ipython().run_line_magic('pinfo', 'modifiers')


# In[ ]:


In object-oriented programming (OOP), access modifiers (or access specifiers) determine the visibility and accessibility of attributes and methods within a class hierarchy. These modifiers control how members of a class can be accessed from within the same class, derived classes, and outside the class. There are typically three main access modifiers: public, private, and protected.

Let's explore each access modifier and their significance in the context of inheritance:

### 1. Public Access Modifier:

- **Significance:**
  - Public members (attributes and methods) are accessible from anywhere, both within the class, derived classes, and external code.
  - They form the interface of the class, allowing other parts of the program to interact with the class.
  
- **Example:**

  ```python
  class MyClass:
      def __init__(self):
          self.public_attribute = 10

      def public_method(self):
          print("This is a public method.")

  obj = MyClass()
  print(obj.public_attribute)  # Accessible
  obj.public_method()  # Accessible
  ```

### 2. Private Access Modifier:

- **Significance:**
  - Private members are accessible only within the class where they are defined. They are not accessible in derived classes or external code.
  - They encapsulate the internal implementation details and prevent direct modification from outside the class.

- **Example:**

  ```python
  class MyClass:
      def __init__(self):
          self.__private_attribute = 20

      def __private_method(self):
          print("This is a private method.")

  obj = MyClass()
  # Attempting to access private members directly will result in an error.
  # print(obj.__private_attribute)  # Error
  # obj.__private_method()  # Error
  ```

### 3. Protected Access Modifier:

- **Significance:**
  - Protected members are accessible within the class and its derived classes, but not accessible from outside the class hierarchy.
  - They strike a balance between the openness of public members and the encapsulation of private members.
  
- **Example:**

  ```python
  class MyClass:
      def __init__(self):
          self._protected_attribute = 30

      def _protected_method(self):
          print("This is a protected method.")

  class DerivedClass(MyClass):
      def access_protected(self):
          print(self._protected_attribute)  # Accessible
          self._protected_method()  # Accessible

  obj = DerivedClass()
  obj.access_protected()  # Accessible within DerivedClass

In the example above, `_protected_attribute` and `_protected_method` are marked as protected using the single underscore prefix. This indicates that they are intended for internal use within the class and its derived classes, discouraging external use but allowing it if needed.

### Differences Between Private, Protected, and Public Access Modifiers:

1. **Visibility:**
   - Public members are visible and accessible everywhere.
   - Private members are visible only within the defining class.
   - Protected members are visible within the defining class and its derived classes.

2. **Access Outside the Class Hierarchy:**
   - Public members are accessible from anywhere, including outside the class hierarchy.
   - Private members are not accessible from outside the defining class.
   - Protected members are not accessible from outside the class hierarchy but can be accessed by derived classes.

3. **Inheritance:**
   - Derived classes can inherit public and protected members from the base class.
   - Private members are not inherited by derived classes.

In summary, the choice of access modifier (public, private, or protected) in inheritance is crucial for defining the appropriate level of encapsulation, visibility, and accessibility for class members, ensuring effective interaction and code maintainability within the class hierarchy.


# In[ ]:





# In[ ]:


5. What is the purpose of the "super" keyword in inheritance? Provide an example.


# In[ ]:


The `super` keyword in object-oriented programming (OOP) is used to refer to the base class (superclass) from a derived class (subclass). It allows the subclass to access and call methods or constructors from the superclass. This is particularly useful when the subclass wants to extend the functionality of the superclass while maintaining and invoking the behavior defined in the superclass.

The `super` keyword is often used in the constructor (`__init__` method) of the subclass to invoke the constructor of the superclass and initialize the inherited attributes.

Here's an example to illustrate the use of the `super` keyword:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls the base class constructor to initialize 'name'
        self.breed = breed

    def sound(self):
        super().sound()  # Calls the 'sound' method from the base class
        print("Barking")

# Creating an instance of the derived class 'Dog'
dog_instance = Dog("Buddy", "Labrador")

# Accessing attributes from the base class
print("Dog's name:", dog_instance.name)
print("Dog's breed:", dog_instance.breed)

# Calling the overridden method which also invokes the base class method
dog_instance.sound()
```

In this example:
- The `Animal` class is the base class with an `__init__` method (constructor) and a `sound` method.
- The `Dog` class is the derived class that inherits from `Animal`.
- In the `__init__` method of `Dog`, `super().__init__(name)` calls the constructor of the base class (`Animal`), allowing it to initialize the `name` attribute.
- In the `sound` method of `Dog`, `super().sound()` calls the `sound` method of the base class (`Animal`), and additional behavior (barking) is added.

The `super` keyword helps in maintaining a clear and predictable behavior when dealing with inheritance, ensuring that both the functionality from the superclass and the customization in the subclass are appropriately utilized.


# In[ ]:





# In[ ]:


6. Create a base class called "Vehicle" with attributes like "make", "model", and "year".
Then, create a derived class called "Car" that inherits from "Vehicle" and adds an
attribute called "fuel_type". Implement appropriate methods in both classes.


# In[1]:


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Vehicle Information:")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")


# Creating an instance of Car
car1 = Car("Toyota", "Corolla", 2020, "Gasoline")

# Displaying vehicle information for the car
car1.display_info()


# In[ ]:





# In[ ]:


7. Create a base class called "Employee" with attributes like "name" and "salary."
Derive two classes, "Manager" and "Developer," from "Employee." Add an additional
attribute called "department" for the "Manager" class and "programming_language"
for the "Developer" class.


# In[2]:


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"Employee Information:")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary}")


class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Programming Language: {self.programming_language}")


# Creating instances of Manager and Developer
manager1 = Manager("John Doe", 80000, "IT")
developer1 = Developer("Jane Smith", 70000, "Python")

# Displaying employee information for the manager and developer
manager1.display_info()
print("\n")
developer1.display_info()


# In[ ]:





# In[ ]:


8. Design a base class called "Shape" with attributes like "colour" and "border_width."
Create derived classes, "Rectangle" and "Circle," that inherit from "Shape" and add
specific attributes like "length" and "width" for the "Rectangle" class and "radius" for
the "Circle" class.


# In[3]:


class Shape:
    def __init__(self, colour, border_width):
        self.colour = colour
        self.border_width = border_width

    def display_info(self):
        print(f"Shape Information:")
        print(f"Colour: {self.colour}")
        print(f"Border Width: {self.border_width}")


class Rectangle(Shape):
    def __init__(self, colour, border_width, length, width):
        super().__init__(colour, border_width)
        self.length = length
        self.width = width

    def display_info(self):
        super().display_info()
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")


class Circle(Shape):
    def __init__(self, colour, border_width, radius):
        super().__init__(colour, border_width)
        self.radius = radius

    def display_info(self):
        super().display_info()
        print(f"Radius: {self.radius}")


# Creating instances of Rectangle and Circle
rectangle1 = Rectangle("Blue", 2, 10, 5)
circle1 = Circle("Red", 1, 7)

# Displaying shape information for the rectangle and circle
rectangle1.display_info()
print("\n")
circle1.display_info()


# In[ ]:





# In[ ]:


9. Create a base class called "Device" with attributes like "brand" and "model." Derive
two classes, "Phone" and "Tablet," from "Device." Add specific attributes like
"screen_size" for the "Phone" class and "battery_capacity" for the "Tablet" class.


# In[4]:


class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Device Information:")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")


class Phone(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def display_info(self):
        super().display_info()
        print(f"Screen Size: {self.screen_size}")


class Tablet(Device):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} mAh")


# Creating instances of Phone and Tablet
phone1 = Phone("Apple", "iPhone 12", "6.1 inches")
tablet1 = Tablet("Samsung", "Galaxy Tab S6", 7040)

# Displaying device information for the phone and tablet
phone1.display_info()
print("\n")
tablet1.display_info()


# In[ ]:





# In[ ]:


10. Create a base class called "BankAccount" with attributes like "account_number" and
"balance." Derive two classes, "SavingsAccount" and "CheckingAccount," from
"BankAccount." Add specific methods like "calculate_interest" for the
"SavingsAccount" class and "deduct_fees" for the "CheckingAccount" class


# In[5]:


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def display_info(self):
        print("Account Information:")
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def calculate_interest(self, interest_rate):
        interest = (interest_rate / 100) * self.balance
        self.balance += interest
        print(f"Interest calculated and added to the account: ${interest}")
        print("Updated Balance:", self.balance)


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance):
        super().__init__(account_number, balance)

    def deduct_fees(self, fee_amount):
        self.balance -= fee_amount
        print(f"Fees deducted from the account: ${fee_amount}")
        print("Updated Balance:", self.balance)


# Creating instances of SavingsAccount and CheckingAccount
savings_account = SavingsAccount("SAV123456", 1000.0)
checking_account = CheckingAccount("CHK789012", 2000.0)

# Displaying account information and performing operations
print("Savings Account:")
savings_account.display_info()
savings_account.calculate_interest(5)  # 5% interest rate
print("\nChecking Account:")
checking_account.display_info()
checking_account.deduct_fees(20)  # $20 fee


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




