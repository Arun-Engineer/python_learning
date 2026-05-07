# Drill 1 - Type - hinted functions

def multiply(a: int, b: int) -> int:
    return a * b

def is_palindrome(text: str) -> bool:
    cleaned_text = text.lower()
    return cleaned_text == cleaned_text[::-1]

def get_word_count(text: str) -> int:
    words = text.split()
    return len(words)

print(multiply(3, 2))
print(is_palindrome("Madam"))
print(get_word_count("aeroplane, hat, rat, mat, rabbit, levaes"))

# Drill 2- optional return
from typing import Optional

def find_book(title: str, library: list[dict]) -> Optional[dict]:
    for book in library:
        if title == book["title"]:
            return book
    return None

library =[
    {"id": 1, "title": "Thor"},
    {"id": 2, "title": 'Money Heist'},
    {"id": 3, "title": "encyclopedia"},
]        


print(find_book("encyclopedia", library))
        
# drill 3- First dataclass
from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int
    is_read: bool = False

b1 = Book(title= "Story", author= "ravi", pages= 234, is_read= True)
b2 = Book(title= "Poem", author= "tagore", pages= 284)
b3 = Book(title= "story", author= "dev", pages= 800, is_read= True)

print(b1 == b2)
print(b1)
print(b2)
print(b3)

# Drill 4- Dataclass with method
@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def is_square(self) -> bool:
        if self.width == self.height:
            return True
        return False
    
rect = Rectangle(3.0 , 8.2)
print(rect.area())
print(rect.perimeter())
print(rect.is_square())

# Drill 5- the big one: refactor your bug dict
@dataclass
class Bug:
    id: int
    title: str
    severity: int
    status: str
    team: str

# skipped drill 5 alone