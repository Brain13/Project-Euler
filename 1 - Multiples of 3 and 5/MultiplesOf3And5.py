#!/usr/bin/env python3

MAX_NUMBER = 1000

runningTotal = 0

# brute force to loop through
for i in range(1, MAX_NUMBER):
    if i % 3 == 0:
        runningTotal += i
    elif i % 5 == 0:
        runningTotal += i
        
# print the result for reporting
print(runningTotal)

