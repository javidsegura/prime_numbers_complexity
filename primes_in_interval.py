import numpy as np
import time
import matplotlib.pyplot as plt


def isprime3(n):
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def allprimes(n):
      primes = []
      for num in range(2, n):
            if isprime3(num):
                  primes.append(num)
      return primes
print(allprimes(100))


def testallprimes(func):
  for i in range(1,30):
    t0 = time.time()
    func(int(i*10000))
    t = time.time()-t0
    print(f"{i*10000}: {t},") #Original value was i * 10000, why?

testallprimes(allprimes)
