#The prime factors of 13195 are 5, 7, 13 and 29
#what is the largest prime factor of the number 600851475143
def SieveOfEratosthenes(n):
    
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
  
        if (prime[p] == True):
            
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
        
    primelst = []
    for p in range(2, n+1):
        if prime[p]:
            primelst.append(p)
    return(primelst)

n = 25
print("Following are the prime numbers smaller"),
print("than or equal to", n)
print(SieveOfEratosthenes(n))