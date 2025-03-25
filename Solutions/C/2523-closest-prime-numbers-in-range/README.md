**Closest Prime Numbers in Range**
=
[Problem Link](https://leetcode.com/problems/closest-prime-numbers-in-range/description)

## Intuition
To efficiently check whether the number is a prime or not, we apply the sieve of Eratosthenes. 
Suppose a number `num = a * b` is a composite number. Since `b` is automatically be decided if `a`
is fixed, only numbers less than or equal to `sqrt(num)` need to be considered as candidates for factors. 
We first define this sieve method `is_prime`, and then store every primes between `left` and `right`.

## Approach
**Step-by-Step Process**

1. Define the sieve of Eratosthenes `is_prime`.

2. Looping `is_prime` starts from `left` to `right`.

3. Store **2 primes**, since our target is to find the closest primes pair.
    - Store the previous prime to `prev`.
    - If current `num` is also a prime, then compute `diff = num - prev`.
    - Mathematically the closest distance is 1 or 2, if `diff <= 2` then return `[prev, num]` immediately.
    - Keep tracking minimal `diff` with `ans = [prev, num]`.
  
## Solutions
```python
# Complexity O((right-left) * sqrt(right))
class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(num):
            if num == 1:
                return False

            for div in range(2, int(sqrt(num)) + 1):
                if num % div == 0:
                    return False

            return True
        
        ans = []
        prev = None

        for num in range(left, right + 1):
            if not is_prime(num):
                continue

            if not prev:
                prev = num
                continue

            diff = num - prev

            if diff <= 2:
                return [prev, num]

            if not ans or diff < ans[1] - ans[0]:
                ans = [prev, num]

            prev = num

        return [-1, -1] if not ans else ans
