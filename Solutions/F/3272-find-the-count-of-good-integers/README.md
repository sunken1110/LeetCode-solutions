**Find the Count of Good Integers**
=
[Problem Link](https://leetcode.com/problems/find-the-count-of-good-integers/description)

## Intuition
We solve the problem step by step.

1. Find every palindrome of `n` digits.

2. Select k-palindromic integers out only.

3. Select unique k-palindromic intgers in the manner of **good** condition.

4. Now, for each unique good integer, the set of digits is also unique. Perform a permutation to count possible number.

5. Exclude the cases of leading zero.

## Approach
**Step-by-Step Process**

1. Set a range of candidates according to `n`, and then find every palindrome.
    - Since a palindrome is symmetric, we first condier the left half then the right half automatically be decided.
  
2. For each palindrome, append to the array `palindrome` if it is k-palindromic.

3. For each integer in `palindrome`, extract unique digit representations up to **good**.
    - Sorting with `set()` can guarantee the uniqueness.

4. For each unique digit represenation `pal`, compute the number of permutations.
    - Note that `len(pal)! / (f_1! * f_2! * ...)` is the answer where `f_i` is a frequency of elements in `pal`.
  
5. If 0 is in `pal`, then exclude the case of leading zero similar to 5.
  
## Solutions
```python
# Time Complexity O(n * 9**(n/2)), Space Complexity O(1)
class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        palindrome = []
        half_digit = (n+1)//2
        ans = 0
        
        for num in range(10**(half_digit-1), 10**half_digit):
            half = str(num)
            pal = half + half[::-1] if n % 2 == 0 else half + half[-2::-1]

            if int(pal) % k == 0:
                palindrome.append(pal)

        unique = set()
        
        for pal in palindrome:
            sorted_digits = ''.join(sorted(list(pal)))

            if sorted_digits in unique:
                continue

            unique.add(sorted_digits)

        for pal in unique:
            freq = Counter(pal)
            cnt = factorial(len(pal))

            for val in freq.values():
                cnt //= factorial(val)

            ans += cnt

            if '0' in freq:
                freq['0'] -= 1
                cnt_zero = factorial(len(pal)-1)
                
                for val in freq.values():
                    cnt_zero //= factorial(val)

                ans -= cnt_zero

        return ans
