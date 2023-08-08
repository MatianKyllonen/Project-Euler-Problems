#The prime factors of 13195 are 5, 7, 13 and 29
#what is the largest prime factor of the number 600851475143
prime = [2, 3]

def findnewprime(prime):
    print(prime)
    z = prime[-1] - 1
    x = 0
    y = 1
    while True:
        while y < len(prime): 
            while x < prime[-y]:
                if(x * prime[-y] == z):
                    x = 0
                    y = 0
                    z += 1
                print(x * prime[-y])
                x += 1
            y += 1
            if(x * prime[-y] == z and z not in prime):
                return(z)         
        if(x * prime[-y] == z and z not in prime):
                return(z)
        z += 1
        x = 0
        y = 1
print(findnewprime(prime))
          

            
    