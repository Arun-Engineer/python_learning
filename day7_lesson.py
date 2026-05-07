# section 1: Basic type hints

def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello!, {name}"

def is_adult(age: int) -> bool:
    return age >= 18

print(add(2, 3))
print(greet("Arun"))
print(is_adult(25))

# Section 2: Collections
def sum_list(numbers: list[int]) -> int:
    return sum(numbers)

def get_first_word(text: str) -> str:
    return text.split()[0]

print(sum_list([1, 2, 3, 4]))
print(get_first_word("the quick brown fox"))

# Section 3: Optional

from typing import Optional

def find_user(user_id: int, users: list[dict]) -> Optional[dict]:
    for user in users:
        if user["id"] == user_id:
            return user
    return None

users = [
    {"id": 1, "name": "Arun"},
    {"id": 2, "name": "Priya"},
]

result = find_user(1, users)
print(result)
result = find_user(99, users)
print(result)

# Section 4: Your first dataclass

from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

p1 = Person(name = "Arun", age = 30)
p2 = Person(name =  "Priya", age = 29)

print(p1)
print(p2)
print(p1 == p2)
print(p1 == Person(name = "Arun", age = 30))

# Section 5: Dataclass with defaults

@dataclass

class Bug:
    id: int
    title: str
    severity: int = 1
    status: str = "open"
    team: str = "unassigned"

bug1 = Bug(id = 1, title= "Login Broken", severity= 5, status= "open", team= "mobile")
bug2 = Bug(id = 2, title= "Typo")

print(bug1)
print(bug2)

# Section 6: Methods on dataclasses

@dataclass

class BugWithMethods:
    id: int
    title: str
    severity: int
    status: str

    def is_critical(self) -> bool:
        return self.status == "open" and self.severity >= 4
    
    def display(self) -> str:
        marker = "fire" if self.is_critical() else " "
        return f"{marker} # {self.id} [{self.severity} {self.title}]"
    
b = BugWithMethods(id=1, title="Payment Broken", severity=5, status="open")
print(b.is_critical())
print(b.display())