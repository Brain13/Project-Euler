#!/usr/bin/env python3

MAX_NUMBER = 10

runningTotal = 0

for i in range(1, MAX_NUMBER):
    if i % 3 == 0:
        runningTotal += i
    elif i % 5 == 0:
        runningTotal += i
        
        
print(runningTotal)

