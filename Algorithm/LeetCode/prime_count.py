# https://leetcode.com/problems/count-primes/

class Solution:
    def countPrimes(self, n: int) -> int:

        count_prime = 0
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p <= n):
            if prime[p] == True:

                for i in range(p * p, n + 1, p):
                    prime[i] = False

            p += 1

        for i in range(2, n):
            if prime[i] == True:
                count_prime += 1

        return count_prime
