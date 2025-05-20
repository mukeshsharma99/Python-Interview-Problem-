#  Write a python program to find a three minimum numbers:


def minimum(a,b,c):
    if (a <= b) and (a <= c):
        smallest = a

    elif (b<=a) and (b<=c):
        smallest = b
    else:
        smallest  = c

    return smallest


a = int(input('Enter a number: '))
b=  int(input('Enter a number: '))
c = int(input('Enter a number: '))
print(minimum(a,b,c))