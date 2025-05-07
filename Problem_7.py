# Write a program to find if the given number is prime or not.

num = int(input('Enetr  a number: '))
flag =   False

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            flag  = True
            break


if flag :
    print('Number is prome ', num)
else:
    print(' Number is not  prime  ',  num)