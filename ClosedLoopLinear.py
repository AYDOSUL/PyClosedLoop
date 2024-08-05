#Linear increase/decrease closed loop
import random as r
a = r.randint(-9,9) #Randomly assigning the coefficients
b = r.randint(-9,9)
c = r.randint(-9,9)
d = r.randint(-9,9)

def func(input):
    return d + c*(input) + b*(input)*(input) + a*(input)*(input)*(input) #Creating the function
print('Coefficients of the cubic equation')
print(a)
print(b)
print(c)
print(d)
kP = 0.01 #Constant of proportion
setpoint = int(input('Setpoint for closed loop: ')) #Asking user for setpoint
cycle = int(input('Number of cycles the closed loop will optimize: ')) #Asking user for number of cycles the algorithm will run
inval = 0 
i = 0
print("#    Input    Output")
while i < cycle : 
    if func(inval) < func(inval + 1):
            cval = kP
    else:
        cval = -kP
    if func(inval) < setpoint :
        inval = inval + kP #Updating the input value as per calculation
        print(i," ",inval," ",func(inval)) #Printing the updated input value
        i = i + 1
    elif func(inval) > setpoint:
        inval = inval - kP #Updating the input value as per calculation
        print(i," ",inval," ",func(inval)) #Printing the updated input value
        i = i + 1
    elif func(inval) == setpoint:
        print(i," ",inval," ",func(inval)) #Printing the input value 
        i = cycle+1
        
print(func(inval)) #Printing final output of function
print(inval) #Printing final input value