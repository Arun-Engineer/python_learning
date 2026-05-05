# greetings.py as a simple module with reusable functions

def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"

GREETING_LANGUAGAE = "English"

# Test code that should onle run when this file is run directly
if __name__ == "__main__":
    print(hello("Arun"))
    print(goodbye("Arun"))
