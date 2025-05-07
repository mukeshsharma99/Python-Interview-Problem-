# Write a python programb to check the given number is Armstrong or Not

num  =  int(input('Enter the Number '))

sum =  0
temp = num

while temp >0:
    digit =  temp%10
    sum += digit** 3
    temp //= 10
if num == sum:
    print('Is an Armstrong number', num)
else:
    print('is not an Armstrong number', num)