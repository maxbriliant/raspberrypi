#!/usr/bin/python3
import sys

J = 11
Q = 12 
K = 13
A = 14

h = 'h'
d = 'd'
s = 's'
c = 'c'

broadCards = { 'J' : 11, 'Q' : 12, 'K' : 13, 'A' : 14}
valueList   = [ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
colorList  = ['h','d','s','c'] 


class Card():

	
	def __init__(self, value, color):
		self.value = value
		self.color = color

	def bigger(c1, c2):
		if c1.value > c2.value: 
			print("True")
			return True 
		else: 					
			print("False")
			return False 

	def __str__(self):
		if self.value 	== 	11:
			return str('J' + self.color)
		elif self.value == 	12:
			return str('Q' + self.color)
		elif self.value == 	13:
			return str('K' + self.color)
		elif self.value == 	14:
			return str('A' + self.color)
		else:
			return str(self.value) + self.color



deck = []


def fill_deck(deck):
	return deck

print(valueList)
print(colorList)