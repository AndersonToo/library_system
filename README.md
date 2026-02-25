# library_system
A Python-based library management system demonstrating object-oriented programming, magic methods, decorators, and packaging.
## Project Features

- Object-Oriented Design (Book and Library classes)
- Magic Methods (`__str__`, `__len__`, `__eq__`)
- Iterable Library container
- Logging decorator for method access tracking
- Permission control using closures
- Demonstration of duck typing

## Method Resolution Order (MRO)

If we create:

  python
class DigitalBook(Book, Software):
    pass
Python determines method lookup order using C3 Linearization.
MRO example:
DigitalBook → Book → Software → object
Order rules:
Methods in DigitalBook are checked first.
Then methods in Book.
Then methods in Software.
Finally methods in object.
This ensures predictable behavior and avoids ambiguity in multiple inheritance.
Duck Typing
Duck typing means:
If an object has the required attributes or methods, it can be used — regardless of its type.
Example:
def borrow_item(item):
    print(item.title)
This works for any object with a .title attribute.
Example:
class Newspaper:
    def __init__(self, title):
        self.title = title
n = Newspaper("Daily News")
borrow_item(n) 
If it behaves like a duck, we treat it like a duck.
