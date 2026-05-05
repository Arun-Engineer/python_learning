# Drill 2
def square(n):
    return n * n

def factorial(n):
    if n < 0:
        return f"Factorial is undefined for negative numbers"
    else:
        result = 1
        for i  in range(1, n+1):
            result = result * i
        return result
    
def prime(n):
    if n < 2:
        return False
    else:
        for d in range(2, n):
            if n % d == 0:
                return False
        return True
    
if __name__ == "__main__":
    print(square(4))
    print(factorial(5))
    print(prime(9))