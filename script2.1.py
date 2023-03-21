#!/usr/bin/python3

number1 = int(input('Введите первое число: '))
number2 = int(input('Введите первое число: '))

a = number1 + number2
b = number1 - number2
c = number1 * number2
d = number1 / number2
e = number1 ** number2
f = number1 % number2
g = number1 // number2

print(f'a + b = {a}\na - b = {b}\na * b = {c}\n'
     f'a / b = {d}\na**b = {e}\na % b = {f}\n'
     f'a // b = {g}')