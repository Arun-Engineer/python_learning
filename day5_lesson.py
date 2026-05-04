# section 1: Your first class

class Greeter:
    def __init__(self, name):
        self.name = name
    
    def hello(self):
        return f"Hello, {self.name}!"

g = Greeter("Arun")
print(g.hello())
print(g.name)

# Section 2: Multiple instances
g1 = Greeter("Arun")
g2 = Greeter("Mumbai")

print(g1.hello())
print(g2.hello())
# Each instatnce has its OWN name. They are independent objects.

# Section 3: A class with state that changes

class Counter:
    def __init__(self):
        self.count = 0
    
    def increment(self):
        self.count = self.count + 1

    def get(self):
        return self.count
    
c = Counter()
print(c.get())
c.increment()
c.increment()
c.increment()
print(c.get())

# Section 4: A class with collection state

class TodoList:
    def __init__(self):
        self.items = []
    
    def add(self, item):
        self.items.append(item)

    def show(self):
        print("Todo List: ")
        for i, item in enumerate(self.items, start=1):
            print(f" {i}. {item}")

todo = TodoList()
todo.add("Finish Day 5")
todo.add("Push to GitHub")
todo.add("sleep")
todo.show()

# Section 5: Methods calling other methods on self

class BugCounter:
    def __init__(self):
        self.bugs = []
    
    def add(self, title, severity):
        self.bugs.append({"title": title, "severity": severity})
    
    def is_critical(self, bug):
        return bug["severity"] >=4
    
    def count_critical(self):
        #self .is_critical is a method on this same object
        return sum(1 for bug in self.bugs if self.is_critical(bug))

bc = BugCounter()
bc.add("Login Broken", 5)
bc.add("Typo", 1)
bc.add("Payment fail", 4)
print(f"Critical: {bc.count_critical()}")