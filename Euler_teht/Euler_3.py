#The prime factors of 13195 are 5, 7, 13 and 29
#what is the largest prime factor of the number 600851475143
prime = [2, 3]

def findnewprime(prime):
    print(prime)
    z = prime[-1] - 1
    x = 0
    y = 1
    while 1 == 1:          
        while y < len(prime): 
            while x < prime[-y]:
                if(x * prime[-y] == z):                   
                    x += 1
                elif(z not in prime):               
                    return(z)
            y += 1
            x = 0
        z += 1
        x = 0
        y = 1
print(findnewprime(prime))
          

            
    