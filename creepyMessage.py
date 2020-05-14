#!/usr/local/bin/python3

import random

random.seed()

value = input("Please enter a message: ")
value = value.lower()

words = value.split()

newValue = ""

for w in words:
	capitalized = random.choices(population = range(1, len(w)), k = len(w)//2)

	w = list(w)
	for letter in capitalized:
		w[letter] = w[letter].upper()
	w = ''.join(w)
	print(w, end = " ")

print(newValue)
