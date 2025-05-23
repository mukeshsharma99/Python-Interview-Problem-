# Write the python program to find the gcd

def gcd(a,b):


    if a == 0:
        return b
    if b == 0:
        return a
    if (a==b):
        return a
    if (a>b):
        return gcd(a-b,b)
a = 98
    
