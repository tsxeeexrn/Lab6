#1  Write a Python program with builtin function to multiply all the numbers in a list
import math

size_list = input("list: ")
my_list = list(map(int, size_list.split()))
print(math.prod(my_list))

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

def count_letters(sentence):
    upper = sum(map(str.isupper, sentence))
    lower = sum(map(str.islower, sentence))

    print("sum upper:", upper)
    print("sum lower:", lower)

count_letters(input("enter sentence: "))

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def is_palindrome(sentence):
    return all(map(str.__eq__, sentence, reversed(sentence)))

print(is_palindrome(input("Enter: ")))

#4 Write a Python program that invoke square root function after specific milliseconds.
import math
import time

time_miliseconds=int(input("Enter  miliseconds:"))
time2_miliseconds=int(input("Enter 2nd miliseconds:"))

print(f"Square root of {time_miliseconds} after {time2_miliseconds} miliseconds is {math.sqrt(time_miliseconds)}")

#5 Write a Python program with builtin function that returns True if all elements of the tuple are true.
mylist=input("mylist:")
mylist=list(map(int,mylist.split()))
print("mylist:",all(mylist))

