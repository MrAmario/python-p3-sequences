#!/usr/bin/env python3

def print_fibonacci(n):
    fib = [0,1]
    for index in range(n):
        add = fib[-1] + fib[-2]
        fib.append(add)
        print(fib[0:n])

print_fibonacci(7)