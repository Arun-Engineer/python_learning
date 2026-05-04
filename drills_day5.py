# Drill 1 - Person class
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

p1 = Person("Arun", 30)
p2 = Person("Priya", 29)
print(p1.introduce())
print(p2.introduce())

# Drill 2 - BankAccount
class BankAccount():
    def __init__(self, owner_name, balance = 0):
        self.owner_name = owner_name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance = self.balance + amount
    
    def withdraw(self, amount):
        if self.balance > 0 and self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False

    def get_balance(self):
        return self.balance
    
ac = BankAccount("Arun", 0)
ac.deposit(30000)
withdraw_result = ac.withdraw(10000)
print(f"Balance: {ac.get_balance()} Withdrawn Success: {withdraw_result}")
withdraw_result = ac.withdraw(25000)
print(f"Balance: {ac.get_balance()} Withdrawn Success: {withdraw_result}")

# Drill 3 - Stack
class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items != None:
            self.items.pop()
            return (item for item in self.items)
        else:
            return False
    
    def peek(self):
        if self.items != None:
            return self.items[-1]
        else:
            return False
    
    def size(self):
        return len(self.items)
    
st = Stack()
st.push("Apple")
print(st.size())
st.push("Papaya")
print(st.size())
st.pop()
print(st.size())
print(st.peek())

# Drill 4 - Restaurant Order
class RestaurantOrder():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    
    def total(self):
        return sum(item["price"] for item in self.items)
           
    def print_receipt(self):
        print(f"Customer Name: {self.customer_name}")
        print("-"*30)
        for i , item in enumerate(self.items, start = 1):
            print(f"{i}. {item['name']} - Rs.{item['price']}")

        print("-" * 30)
        print(f"Total: Rs.{self.total()}")

order = RestaurantOrder("Arun")
order.add_item("Dosa", 60)
order.add_item("Coffee", 25)
order.add_item("Poori", 50)

order.print_receipt()

# Drill 5 - Compositional method
class RestaurantOrder():
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
    
    def total(self):
        return sum(item["price"] for item in self.items)
    
    def is_big_order(self):
        if self.total() > 1000:
            return True
        else:
            return False
           
    def print_receipt(self):
        print(f"Customer Name: {self.customer_name}")
        print("-"*30)
        for i , item in enumerate(self.items, start = 1):
            print(f"{i}. {item['name']} - Rs.{item['price']}")

        print("-" * 30)
        print(f"Total: Rs.{self.total()}")

order = RestaurantOrder("Arun")
order.add_item("Dosa", 60)
order.add_item("Coffee", 25)
order.add_item("Poori", 50)

order.print_receipt()

