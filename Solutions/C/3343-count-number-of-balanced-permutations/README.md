**Count Number of Balanced Permutations**
=
[Problem Link](https://leetcode.com/problems/count-number-of-balanced-permutations/description)

## Intuition
First we count the frequency of digits. The main idea is to distribute each digit to even and odd indices which can be 
efficiently implemented with DFS. Start from the digit `9` and distribute to even and odd indices. 
Accumulate the combinations of it and pass to the next `dp` of digit `8`. The termination occurs when 

1. Already distributed every digit from 1 to 9, but still the sum of even or odd indices don't reach to a half-sum.

2. Even or odd indices are fulled before distributing every digit.

3. One of sum of even or odd indices exceeds a half-sum.

## Approach
**Step-by-Step Process**

1. Measure the number of odd and even indices.

2. Set a target half-sum `half_sum`.
    - If `half_sum` is not even, then return 0.
  
3. Count the number of each digit.

4. Construct a dfs with above conditions.
    - A combination of distributing each digit to even or odd indices can be computed by `comb`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n^2)
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        total_sum = sum(int(i) for i in num)

        if total_sum % 2 == 1:
            return 0

        odd = len(num) // 2
        even = (len(num) + 1) // 2
        half_sum = total_sum // 2
        mod = 10**9 + 7
        freq = Counter(int(i) for i in num)


        @cache
        def dfs(digit, num_odd, num_even, balance):
            if num_odd == 0 and num_even == 0 and balance == 0:
                return 1

            if digit < 0 or num_odd < 0 or num_even < 0 or balance < 0:
                return 0

            cnt = 0

            # counter of digit -> distribute to odd/even indices
            for i in range(freq[digit] + 1):
                cnt += comb(num_odd, i) * comb(num_even, freq[digit]-i) * dfs(digit-1, num_odd-i, num_even-freq[digit]+i, balance-i*digit)

            return cnt % mod

        
        return dfs(9, odd, even, half_sum)
