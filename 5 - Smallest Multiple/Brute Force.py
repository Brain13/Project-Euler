#!/usr/bin/env python3
import math

HIGHEST_MULTIPLE = 20

#set up the sieve for all prime numbers
# 0 means prime, 1 means not prime
# 0 and 1 are special numbers, so they count as not prime
sieve = [0] * HIGHEST_MULTIPLE
sieve[0] = 1
sieve[1] = 1

# go up through sqrt(INPUT)
# since range goes [start, finish), we need to go sqrt + 1 in the argument
for i in range(2, math.ceil(math.sqrt(HIGHEST_MULTIPLE))):
    if sieve[i] == 0:
        for j in range(i + i, HIGHEST_MULTIPLE, i):
            sieve[j] = 1

productCounts = [0] * HIGHEST_MULTIPLE
for i in range(1, HIGHEST_MULTIPLE):
    target = i
    sieveSpot = 2
    while target > 1:
        sieveCount = 0
        if sieve[sieveSpot] == 0:
            while target % sieveSpot == 0:
                sieveCount += 1
                target /= sieveSpot
        productCounts[sieveSpot] = max(productCounts[sieveSpot], sieveCount)
        sieveSpot += 1
        
totalProduct = 1
for i in range(1, HIGHEST_MULTIPLE):
    totalProduct *= i ** productCounts[i]
    
print(totalProduct)