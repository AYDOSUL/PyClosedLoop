import random as r
a = r.randint(0,9) #Randomly assigning the coefficients
b = r.randint(0,9)
c = r.randint(0,9)
d = r.randint(0,9)

def func(input):
    return d + c*(input) + b*(input)*(input) + a*(input)*(input)*(input) #Creating the function
print('Coefficients of the cubic equation')
print(a)
print(b)
print(c)
print(d)
setpoint = int(input('Setpoint for closed loop: ')) #Asking user for setpoint
cycle = int(input('Number of cycles the closed loop will optimize: ')) #Asking user for number of cycles the algorithm will run
cval = 0 #Declaring initial correction value
inval = 0
i = 0 #Setting i to 1, avoiding division by zero errors(on line 18)
print("#    Input    Output")
while i < cycle : 
    cval = 0.01
    if func(inval) < setpoint :
        inval = inval + cval #Updating the input value as per calculation
        print(i," ",inval," ",func(inval)) #Printing the updated input value
        i = i + 1
    elif func(inval) > setpoint:
        inval = inval - cval #Updating the input value as per calculation
        print(i," ",inval," ",func(inval)) #Printing the updated input value
        i = i + 1
    elif func(inval)-tol < setpoint and func(inval)+tol > setpoint:
        print(i," ",inval," ",func(inval)) #Printing the input value 
        i = cycle+1
        
print(func(inval)) #Printing final output of function
print(inval) #Printing final input value

