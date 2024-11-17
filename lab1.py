from math import *

x= float(input("Введите значение x--> "))
y= float(input("Введите значение y--> "))
z= float(input("Введите значение z --> "))

s= ((cbrt(9+(x-y)**2))/((pow(x, 2))+pow(y, 2)+2))-exp(x-y)*pow(tan(z),3)

print(s)
