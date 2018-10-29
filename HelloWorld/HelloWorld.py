# -*- coding: utf-8 -*-
print("Hello world!")

print("--------------------")

string = "1234567890"

for char in string:
    print(char)

print("--------------------")

my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))

print("--------------------")

my_list = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

for i in my_list:
    print(i)

print("--------------------")

my_iterator = iter(my_list)
for i in range(0, len(my_list)):
    next_item = next(my_iterator)
    print(next_item)
