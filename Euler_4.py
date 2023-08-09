#A palindromic number reads the same both ways.
#The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99
#Find the largest palindrome made from the product of two 3-digit numbers.
a = 99
b = 99
while True:   
    x = list(str(a * b))
    x.reverse()
    if(x == list(str(a * b))):
        print("juu: ", a, b, x)
        break       
    else:
        if(a >= b):
            a -= 1
        elif(b > a):
            b -= 1    