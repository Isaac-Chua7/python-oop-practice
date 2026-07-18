#magic methods or Dunder methods are methods that without explicit calling. The occur when classes are instantiated, compared, printed or otherwise operated on. They can be used to tailor common operations to perform task specific actions. 

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __eq__(self, other):
        if self.pages == other.pages:
            return True
        else:
            return False
        
    def __gt__(self, other):
        if self.pages > other.pages:
            return True
        else:
            return False
    
    def __lt__(self, other):
        return (self.pages < other.pages)
    
    def __str__(self):
        return f"{self.title} written by {self.author}"
    
    def __add__(self, other):
        return f"Number of combined pages is {self.pages + other.pages}"
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"Key '{key}' was not found"


b1 = Book("Harry Potter and the Prisioner of Azkaban", "J.K. Rowling", 317)
b2 = Book("The Hunger Games", "Suzanne Collins", 374)
b3 = Book("Percy Jackson and the Battle of the Labyrinth", "Rick Riordan", 317)

print(b2 == b1) #implicitly calls __eq__

print(b2 > b1) #implicitly calls __gt__

print(b2 < b3) #implictly calls less than

print(b1) #implicitly calls __str__

print(b1+b2) #implicitly calls __add__

print("Games" in b2) #implicitly calls __contains__

print(b1["title"])