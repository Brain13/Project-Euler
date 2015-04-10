#!/usr/bin/env python3
import math

INPUT = 600851475143

##set up the sieve for all prime numbers
## 0 means prime, 1 means not prime
## 0 and 1 are special numbers, so they count as not prime
#sieve = [0] * INPUT
#sieve[0] = 1
#sieve[1] = 1
#
## go up through sqrt(INPUT)
## since range goes [start, finish), we need to go sqrt + 1 in the argument
#for i in range(2, math.ceil(math.sqrt(INPUT))):
#    if sieve[i] == 0:
#        for j in range(i + i, INPUT, i):
#            sieve[j] = 1

# find the prime factors
remainder = INPUT
sieveSpot = 2
maxPrime = 0

# divide out the prime factors
while remainder > 1:
    
    # only try to divide primes
    # anything not prime will have already been divided out
    #if sieve[sieveSpot] == 0:
        
    # it may be a repeated prime, such as during a square
    while remainder % sieveSpot == 0:
        maxPrime = sieveSpot
        remainder /= sieveSpot
        
    sieveSpot += 1
    
print(maxPrime)