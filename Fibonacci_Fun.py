# The first few terms of the Fibonacci sequence is 1, 1, 2 ...
# Write a function that returns the sum of the first n terms in the Fibonacci sequence

def fib(n):
    return 1/(5**0.5)*(((1+(5**0.5))/2)**n-((1-(5**0.5))/2)**n)

def fib_sum(n):
    total = 0
    for i in range(n+1):
        total += fib(i)
