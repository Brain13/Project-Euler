#!/usr/bin/env python3

MAX_VALUE = 4000000

# iterative fibonacci
# this sequence starts with 1, 2, 3, 5...
fib1 = 1
fib2 = 2
runningTotal = 0

while fib1 < MAX_VALUE:
    if fib1 % 2 == 0:
        runningTotal += fib1
    fib3 = fib1 + fib2
    fib1 = fib2
    fib2 = fib3

print(runningTotal)