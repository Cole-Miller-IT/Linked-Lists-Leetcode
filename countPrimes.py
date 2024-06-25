class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 1:
            return 0
        
        elif n == 2:
            return 0
        
        else:
            #using https://www.geeksforgeeks.org/sieve-of-eratosthenes/
            #see diagrams for how this works but basically you start at 2 (or p) flag all multiples of p as false,
            #then move on until you find the next number (the next prime) that is marked true (repeat above step).

            # Create a boolean array
            # "prime[0..n]" and initialize
            #  all entries it as true.
            # A value in prime[i] will
            # finally be false if i is
            # Not a prime, else true.
            prime = [True for i in range(n+1)]

            p = 2 #start at p = 2
            while (p * p <= n):

                # If prime[p] is not
                # changed, then it is a prime
                if (prime[p] == True):

                    # Update all multiples of p
                    for i in range(p * p, n+1, p):
                        prime[i] = False
                p += 1

            # Print all prime numbers
            primeCount = 0
            for p in range(2, n):
                if prime[p]:
                    primeCount += 1
                    #print(p)


            return primeCount