class Solution(object):
    def countPrimes(self, n):

        def prime(n):
            if n < 2:
                return False
            if n == 2:
                return True
            div = 2
            while div * div <= n:
                if n % div == 0:
                    return False
                div += 1
            return True
        
        if n < 2:
            return 0
        
        is_prime = [True, False] * ((n + 1) // 2 )
        is_prime[0], is_prime[1]  = False, True  
        div = 3
        while div * div <= n :
            if prime(div):
                for i in range(2*div, n + 1, div):
                    is_prime[i-1] = False
            div += 2
        
        return sum(is_prime)
    
    def factorial(self, n):
        if n == 0:
            return 1
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res

    def numPrimeArrangements(self, n):

        primes_count = self.countPrimes(n)
        return self.factorial(primes_count) * self.factorial(n - primes_count) % (10**9 +7)
