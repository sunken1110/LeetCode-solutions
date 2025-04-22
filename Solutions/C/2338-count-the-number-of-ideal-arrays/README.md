**Count the Number of Ideal Arrays**
=
[Problem Link](https://leetcode.com/problems/count-the-number-of-ideal-arrays/description)

## Intuition
Since each ideal is a chain of divisibility, we need to focus on the prime factorization of numbers under `maxValue`. 
Also each ideal array can contain more than two same values, the possibility is a combination with repetition 
in the manner of degrees of primes. Suppose `x = p^e * r` where `p` is a prime, `e` is a degree of `p`, and `r` is 
a remainder which is not divisible by `p`. Then `e` can be distributed to each element of ideal array, and it is 
independent to other primes. That is, `p^e` itself makes `n-1+e` choose `e` cases. The answer is multiples of such 
cases among whole primes of prime factorization.

## Approach
**Step-by-Step Process**

1. Construct `getPrimes` of the prime factorization.
    - Since we need each prime factor's degree, store the information in `defaultdict`.

2. For each integer from 1 to  `maxValue`, process prime factorizations.
    - The number of prime factor cases are `math.comb(n-1+deg, deg)`.
    - Multiply among whole primes.

3. Sum up.
  
## Solutions
```python
# Time Complexity O(maxValue*sqrt(maxValue)), Space Complexity O(log(maxValue))
class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        mod = 10**9 + 7
        ans = 0

        
        def getPrimes(num):
            primes = defaultdict(int)
            p = 2

            while num > 1:
                while num % p == 0:
                    primes[p] += 1
                    num //= p

                p += 1

            return primes


        for i in range(1, maxValue + 1):
            primes = getPrimes(i)
            cnt = 1

            for deg in primes.values():
                cnt *= comb(n-1 + deg, deg)

            ans += cnt

        return ans % mod
```
