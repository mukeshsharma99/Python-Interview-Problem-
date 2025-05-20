# Write a program to find a maximum of two numbers.
def maximum(a, b):
    if a>=b:
        return a
    else:
        return b
    

a =  int(input('enter the number :'))
b  = int(input('Enter the number:'))

print(maximum(a,b))


