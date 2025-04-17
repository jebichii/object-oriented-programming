# Assignment: Object-Oriented Programming with Python

## Project Description
This project demonstrates the principles of object-oriented programming (OOP) in Python by designing and implementing classes. The assignment focuses on creating a `Book` class and its inherited class `Ebook`, while also exploring polymorphism through shared methods that behave differently across related classes.

---

## Features

### Assignment 1: Design Your Own Class
- **Class Creation**: A `Book` class with attributes such as `title`, `author`, `genre`, and `price`.
- **Inheritance**: An `Ebook` class inherits from `Book` and includes additional attributes like `file_size`.
- **Encapsulation**: Attributes are initialized using a constructor to ensure controlled access.
- **Methods**:
  - `display_details()`: Displays the details of the book.
  - `read()`: Demonstrates a behavior specific to the type of book (paperback or ebook).

### Activity 2: Polymorphism Challenge
- **Polymorphism**: Implements the same method, `read()`, differently in `Book` and `Ebook` classes.
- **Shared Interface**: Both physical books and ebooks share the same method name but execute unique behaviors.

---

## Code Highlights
- **Encapsulation**: Use of constructors (`__init__`) to initialize attributes of each object.
- **Inheritance**: Demonstrating how `Ebook` extends the `Book` class.
- **Polymorphism**: Overriding methods in subclasses to define unique behavior.
- **Iterative Implementation**: Creating objects dynamically and calling shared methods in a loop.

---