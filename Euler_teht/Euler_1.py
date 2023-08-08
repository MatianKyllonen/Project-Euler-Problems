#If we list all the natural numbers below 10 that are multiples of 3 or 5 , we get 3,5,6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.
num = input("Give number to check: ")
num = int(num)
lst = []
x = 0

while x < num - 1:
    x = x + 1 
    if((num - x) % 3 == 0 or (num - x) % 5 == 0 ):
        lst.append(num - x)     
print(sum(lst))
    


