# Write a python program to findthe factorial number  using  Recursive Approach:

def fac_recursive(n):
    if n <0:
        return 'Facorial not define for nagetive number'
    
    if n ==0 or n== 1:
        return 1
    return n* fac_recursive (n -1)

num = int(input('Enter a number: '))
print(fac_recursive(num))  ;kfiekfgmueokr8u