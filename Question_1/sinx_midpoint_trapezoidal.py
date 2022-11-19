import numpy as np

#input_section
a=0
b=(3*np.pi)/4
n=1000

#Defining the function
def f(x):
    return np.sin(x)

#midpoint_rule
def midpoint(a,b,n,f):
    h=(b-a)/n  #the_value of the step size
    g=0       
    for i in range (0,n):
        x_i=a+(((2*i)+1)*h)/2 #midpoints
        g=g+f(x_i) #calculating_sum
    area=h*g #finding_area
    return area

#Trapezoidal_rule
def trapezoidal(a,b,n,f):
    h=(b-a)/n #the value of step size
    g=(f(a)+f(b))/2
    for i in range(1,n):
        g=g+f(a+(i*h))  #calculating the total value of the sum
    area=h*g  #calculating the area
    return area

#Difference between Trapezoidal and midpoint rule
diff=(trapezoidal(a,b,n,f)-midpoint(a,b,n,f))
      
print("The difference between trapezoidal and midpoint rule here is:",diff)