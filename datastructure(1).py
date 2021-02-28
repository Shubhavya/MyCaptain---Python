import math

x = float(input("Input the radius of the circle: "))
print("The area of the circle with radius ", x, " is: ", math.pi*x*x)

y = input("Input the Filename: ")
k = y.index('.')
print("The extension of the file is :", y[k+1:])