import random as r #Importing required library
a = r.randint(0,9) #Creating cubic coefficients
b = r.randint(0,9)
c = r.randint(0,9)
d = r.randint(0,9)

def func(input):
    return a + b*(input) + c*(input)*(input) + d*(input)*(input)*(input) #Creating the function
print('Coefficients of cubic equation') #Printing the function coefficients
print(a)
print(b)
print(c)
print(d)
setpoint = int(input('Setpoint for closed loop: ')) #Asking user for setpoint
cycle = int(input('Number of cycles the closed loop will optimize: ')) #Asking user for number of cycles the algorithm will run
cval = 0 #Declaring initial correction value
inval = 0 #Declaring initial input value
tuneval = 0.0001 #Declaring the tuning value for the loop
i = 1 #Setting i to 1, avoiding division by zero errors(on line 23)

while i < cycle+1 : 
    x = setpoint/i #Creating x variable to make rate of change smoother
    cval = (func(setpoint-x) - func(1))/(setpoint-1) #Creating calculation of the correction value
    if func(inval) < setpoint :
        inval = inval + tuneval*cval #Updating the input value as per calculation
        print(inval) #Printing the updated input value
    elif func(inval) > setpoint:
        inval = inval - tuneval*cval #Updating the input value as per calculation
        print(inval) #Printing the updated input value
    elif func(inval) == setpoint :
        print(inval) #Printing the input value 
    i = i + 1
print(func(inval)) #Printing final output of function
print(inval) #Printing final input value
