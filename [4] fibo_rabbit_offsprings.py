#Fibonacci sequence
def fibonacci(n):
    first = 1
    second = 1
    for i in range(n-2):
        next = first + second
        first = second
        second = next
    return next

print(fibonacci(5))


#Fibonacci sequence with rabbit reproductions

def fibonacci_rabbit_reproduction(months, babies):
    first = 1
    second = 1
    for i in range(months - 2):
        next = second + (first * babies)
        first = second
        second = next
    return next

print(fibonacci_rabbit_reproduction(5,3))
