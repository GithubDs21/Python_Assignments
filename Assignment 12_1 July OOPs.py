#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What is the primary goal of Object-Oriented Programming (OOP)?


# In[ ]:


The primary goal of Object-Oriented Programming (OOP) is to model the real-world entities and their interactions in a software application. OOP is a programming paradigm that revolves around the concept of "objects," which are instances of classes representing entities with attributes (data) and behaviors (methods).

The goals of Object-Oriented Programming are:

Abstraction: OOP allows developers to create abstract representations of real-world entities in the form of classes. These classes define the common properties and behaviors shared by objects of the same type.

Encapsulation: OOP encapsulates the data and methods that operate on that data within a class. This concept of data hiding helps in protecting the internal state of an object, allowing controlled access to its properties and behaviors.

Inheritance: Inheritance allows classes (called subclasses or derived classes) to inherit the properties and behaviors of other classes (called base classes or superclasses). This promotes code reuse and the creation of hierarchical relationships between classes.

Polymorphism: Polymorphism enables objects of different classes to be treated as objects of a common superclass. This allows for more generic and flexible programming, as the same method can behave differently depending on the specific object it is called on.

Modularity: OOP encourages modular design, where complex systems can be broken down into smaller, more manageable units (classes). Each class represents a specific module with well-defined responsibilities, making the code easier to understand, maintain, and scale.

Flexibility and Maintainability: OOP supports the open-closed principle, which means classes should be open for extension but closed for modification. This makes it easier to add new features without modifying existing code, leading to more maintainable and extensible software.

Overall, the primary goal of Object-Oriented Programming is to create software that is organized, reusable, and easy to understand and maintain. By representing entities and their interactions using objects and classes, OOP provides a powerful paradigm for building complex systems and large-scale applications in a structured and efficient manner.


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


In Python, everything is an object. This means that all data types
(such as integers, strings, lists, dictionaries, etc.) and even functions and 
classes are objects. Every object in Python has three key characteristics

Identity: An object's identity is a unique identifier that distinguishes it from other objects. 
The identity is guaranteed to be unique during the object's lifetime and can be obtained using the built-in id() function

Attributes: Attributes are the data associated with an object. In Python, attributes can be accessed and modified using dot notation
(e.g., object.attribute). For example, for a class Person, the object may have attributes like name, age, etc.

Methods: Methods are functions that are associated with an object and operate on its attributes.
    They define the behavior of the object.
    Methods can be called using dot notation as well (e.g., object.method()).
    
To create an object, you need to define a class first. A class serves as a blueprint or a template for creating objects. 
It specifies what attributes and methods an object of that class will have. 
Once the class is defined, you can create instances (objects) of that class using the class constructor.
The process of creating an object from a class is called instantiation.    


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


In Python, a class is a blueprint or a template for creating objects.
It is a fundamental concept in object-oriented programming (OOP) that 
allows you to define a new data type with its own attributes (data) and methods (functions). 
A class defines the structure and behavior of the objects that will be created based on it.


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'class')


# In[ ]:


In a class, attributes and methods are the two main components that define the structure and 
behavior of objects created from that class. They are essential concepts in object-oriented programming (OOP) and
play a fundamental role in encapsulating data and functionality within a class.


Attributes:
Attributes are variables that store data specific to each object created from the class.
They represent the characteristics or properties of the objects. In Python, attributes can be of various data types, 
such as integers, strings, lists, etc. Each object of the class has its own set of attribute values,
allowing different objects to have different data.

Attributes can be of two types:

Instance Attributes: These attributes are specific to each instance (object) of the class. They are defined inside the class's methods using the self keyword and are accessed using the dot notation (object.attribute_name) outside the class.
Class Attributes: These attributes are shared by all instances of the class. They are defined directly within the class but outside any method and are accessed using the class name (ClassName.attribute_name).


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'Python')


# In[ ]:


Class Variables:

    Class variables are shared among all instances of a class. They are defined within the class but outside of any instance methods.
They are typically used to store data that is common to all instances of the class.
Class variables are created when the class is defined and are not tied to any specific instance. Any modification to a class variable will affect all instances of the class.
They are accessed using the class name itself or through any instance of the class.
Class variables can be useful for constants, default values, or data that should be consistent across all instances.

Instance Variables:

    Instance variables are unique to each instance of a class. They are defined within the class's methods, particularly within the constructor method (__init__).
They hold data specific to an individual instance and can have different values for different instances.
Instance variables are accessed using the self keyword within instance methods, where self refers to the instance itself.
Any modification to an instance variable affects only that particular instance.


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('pinfo', 'methods')


# In[ ]:


In Python, the self parameter in class methods refers to the instance of the class on which the method is being called. It is a convention, not a keyword, and you can technically name it something else, although it's highly recommended to stick with the convention of using self.

The purpose of the self parameter is to allow you to access and manipulate the instance variables and other attributes of the object within the method. It essentially provides a reference to the instance itself, so you can perform actions and retrieve information specific to that instance.


# In[ ]:





# In[ ]:


7. For a library management system, you have to design the "Book" class with OOP
principles in mind. The “Book” class will have following attributes:
a. title: Represents the title of the book.
b. author: Represents the author(s) of the book.
c. isbn: Represents the ISBN (International Standard Book Number) of the book.
d. publication_year: Represents the year of publication of the book.
e. available_copies: Represents the number of copies available for checkout.
The class will also include the following methods:
a. check_out(self): Decrements the available copies by one if there are copies
available for checkout.
b. return_book(self): Increments the available copies by one when a book is
returned.
c. display_book_info(self): Displays the information about the book, including its
attributes and the number of available copies.


# In[ ]:


class Book:
    def __init__(self, title, author, isbn, publication_year, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.available_copies = available_copies

    def check_out(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print(f"Checked out '{self.title}'. {self.available_copies} copies available.")
        else:
            print(f"No copies of '{self.title}' available for checkout.")

    def return_book(self):
        self.available_copies += 1
        print(f"Returned '{self.title}'. {self.available_copies} copies available.")

    def display_book_info(self):
        print("Book Information:")
        print(f"Title: {self.title}")
        print(f"Author(s): {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Publication Year: {self.publication_year}")
        print(f"Available Copies: {self.available_copies}")

# Creating an instance of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0", 1925, 5)

# Performing operations on the book
book1.display_book_info()
book1.check_out()
book1.return_book()
book1.check_out()


# In[ ]:





# In[ ]:


8. For a ticket booking system, you have to design the "Ticket" class with OOP
principles in mind. The “Ticket” class should have the following attributes:
a. ticket_id: Represents the unique identifier for the ticket.
b. event_name: Represents the name of the event.
c. event_date: Represents the date of the event.
d. venue: Represents the venue of the event.
e. seat_number: Represents the seat number associated with the ticket.
f. price: Represents the price of the ticket.
g. is_reserved: Represents the reservation status of the ticket.
The class also includes the following methods:
a. reserve_ticket(self): Marks the ticket as reserved if it is not already reserved.
b. cancel_reservation(self): Cancels the reservation of the ticket if it is already
reserved.
c. display_ticket_info(self): Displays the information about the ticket, including its
attributes and reservation status.


# In[ ]:


class Ticket:
    def __init__(self, ticket_id, event_name, event_date, venue, seat_number, price):
        self.ticket_id = ticket_id
        self.event_name = event_name
        self.event_date = event_date
        self.venue = venue
        self.seat_number = seat_number
        self.price = price
        self.is_reserved = False

    def reserve_ticket(self):
        if not self.is_reserved:
            self.is_reserved = True
            print(f"Ticket {self.ticket_id} reserved for {self.event_name}.")
        else:
            print(f"Ticket {self.ticket_id} is already reserved.")

    def cancel_reservation(self):
        if self.is_reserved:
            self.is_reserved = False
            print(f"Reservation for ticket {self.ticket_id} canceled.")
        else:
            print(f"Ticket {self.ticket_id} is not currently reserved.")

    def display_ticket_info(self):
        print("Ticket Information:")
        print(f"Ticket ID: {self.ticket_id}")
        print(f"Event Name: {self.event_name}")
        print(f"Event Date: {self.event_date}")
        print(f"Venue: {self.venue}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Price: ${self.price}")
        print(f"Reservation Status: {'Reserved' if self.is_reserved else 'Not Reserved'}")

# Creating an instance of the Ticket class
ticket1 = Ticket(1, "Concert", "2023-09-15", "Arena Hall", "A12", 50.00)

# Performing operations on the ticket
ticket1.display_ticket_info()
ticket1.reserve_ticket()
ticket1.cancel_reservation()
ticket1.reserve_ticket()
ticket1.display_ticket_info()


# In[ ]:





# In[ ]:


9. You are creating a shopping cart for an e-commerce website. Using OOP to model
the "ShoppingCart" functionality the class should contain following attributes and
methods:
a. items: Represents the list of items in the shopping cart.
The class also includes the following methods:
a. add_item(self, item): Adds an item to the shopping cart by appending it to the
list of items.
b. remove_item(self, item): Removes an item from the shopping cart if it exists in
the list.
c. view_cart(self): Displays the items currently present in the shopping cart.
d. clear_cart(self): Clears all items from the shopping cart by reassigning an
empty list to the items attribute.


# In[ ]:


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"Added '{item}' to the shopping cart.")

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            print(f"Removed '{item}' from the shopping cart.")
        else:
            print(f"'{item}' not found in the shopping cart.")

    def view_cart(self):
        if self.items:
            print("Items in the shopping cart:")
            for item in self.items:
                print(item)
        else:
            print("The shopping cart is empty.")

    def clear_cart(self):
        self.items = []
        print("Shopping cart has been cleared.")

# Creating an instance of the ShoppingCart class
cart = ShoppingCart()

# Performing operations on the shopping cart
cart.add_item("Shirt")
cart.add_item("Shoes")
cart.add_item("Hat")
cart.view_cart()
cart.remove_item("Shoes")
cart.view_cart()
cart.clear_cart()
cart.view_cart()


# In[ ]:





# In[ ]:


10. Imagine a school management system. You have to design the "Student" class using
OOP concepts.The “Student” class has the following attributes:
a. name: Represents the name of the student.
b. age: Represents the age of the student.
c. grade: Represents the grade or class of the student.
d. student_id: Represents the unique identifier for the student.
e. attendance: Represents the attendance record of the student.
The class should also include the following methods:
a. update_attendance(self, date, status): Updates the attendance record of the
student for a given date with the provided status (e.g., present or absent).
b. get_attendance(self): Returns the attendance record of the student.
c. get_average_attendance(self): Calculates and returns the average
attendance percentage of the student based on their attendance record.


# In[ ]:


class Student:
    def __init__(self, name, age, grade, student_id):
        self.name = name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.attendance = {}  # Using a dictionary to store attendance records

    def update_attendance(self, date, status):
        self.attendance[date] = status
        print(f"Attendance for {self.name} on {date} updated: {status}")

    def get_attendance(self):
        return self.attendance

    def get_average_attendance(self):
        if not self.attendance:
            return 0.0

        total_days = len(self.attendance)
        present_days = sum(1 for status in self.attendance.values() if status == "present")
        average = (present_days / total_days) * 100
        return average

# Creating an instance of the Student class
student1 = Student("Alice", 15, "10th", "S123")

# Performing operations on the student
student1.update_attendance("2023-08-15", "present")
student1.update_attendance("2023-08-16", "absent")
student1.update_attendance("2023-08-17", "present")

attendance_record = student1.get_attendance()
print("Attendance Record:")
for date, status in attendance_record.items():
    print(f"{date}: {status}")

average_attendance = student1.get_average_attendance()
print(f"Average Attendance: {average_attendance:.2f}%")


# In[ ]:





# In[ ]:




