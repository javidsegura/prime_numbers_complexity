import numpy as np
import time

def bestisprime(n,primelist): # Named after isprime3
  limit = int(np.sqrt(n))+1
  for prime in primelist:
    if limit < prime:
      return True
    if n%prime == 0:
      return False
  return True

def bestallprimes(n): #Named after allprimes
    primes = []
    for num in range(2, n):
        if bestisprime(num,primes):
            primes.append(num)
    return primes
print(bestallprimes(100))

def testallprimes(func): 
  for i in range(1,30):
    t0 = time.time()
    func(int(i))
    t = time.time()-t0
    print(f"{i}: {t},") #Original value was i * 10000, why?

testallprimes(bestallprimes)