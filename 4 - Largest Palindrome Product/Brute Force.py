#!/usr/bin/env python3
import math

# takes a number and determines if it is a palindrome
def isPalindrome(number):
    return str(number) == reversedString(number)
    
# reverses a string
# [::-1] => [a:b:c] => takes a slice of the string
# a => start position of string
# b => end position of string
# c => step amount (negative to go backwards)
def reversedString(stringValue):
    return str(stringValue)[::-1]

NUMBER_OF_DIGITS = 3

largestPalindrome = 0
for i in range(10 ** (NUMBER_OF_DIGITS - 1), 10 ** NUMBER_OF_DIGITS):
    for j in range(10 ** (NUMBER_OF_DIGITS - 1), 10 ** NUMBER_OF_DIGITS):
        product = i * j
        if (isPalindrome(product)):
            largestPalindrome = max(product, largestPalindrome)
            
print(largestPalindrome)