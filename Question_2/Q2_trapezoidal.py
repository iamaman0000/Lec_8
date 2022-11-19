import numpy as np

#input_section
a=-2 #initial_value
b=2 #final_value
n=1000 #number of step size

#definingfunction
def f(x):
    return (10-(x**2))

#Trapezoidal_rule
def trapezoidal(a,b,n,f):
    h=(b-a)/n #the value of step size
    g=(f(a)+f(b))/2
    for i in range(1,n):
        g=g+f(a+(i*h))  #calculating the total value of the sum
    area=h*g  #calculating the area
    return area

print("The value of integration is:", trapezoidal(a,b,n,f))