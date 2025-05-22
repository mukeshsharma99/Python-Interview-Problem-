# Write a python progrm to find the fabonacci  of  a numeber

nterms  = int(input('How many terms'))

n1, n2 =  0,1 
count = 0

if nterms <=0:
    print('please enter the postive number')

elif nterms == 1:
    print('fabonacci sequence upto ', nterms)
    print(n1)

else:
    print('fabnacci sequence')
    while count< nterms:
        print(n1)
        nth = n1 +n2
        n1 = n2
        n2 = nth
        count +=1
        