# Write a python program to findthe factorial number  using  itterative apporach 

def fact_iterative(n):
    if n < 0:
        return 'Factorial is not defined for negative numbers.'
    result = 1 
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input('Enter a number: '))
print(fact_iterative(num))
