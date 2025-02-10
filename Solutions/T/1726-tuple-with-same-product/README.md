**Tuple with Same Product**
=
[Problem Link](https://leetcode.com/problems/tuple-with-same-product/description)

## Intuition
Since all integers in `nums` are distinct, every tuple uniquely generates one product. That is, 
if we can count every possibility of generating a specific product, the remained work is 
to calculate permutations of it.

## Approach
**Step-by-Step Process**

1. Construct a frequency dictionary `count` of each product. The order of product is not our interest.

2. For each product, calculate every permutation of generating method.
    - If a tuple `(a, b, c, d)` is fixed with `a * b = c * d`, then there are totally 8 permutations.
    - > 2 from changing order of `(a, b)`, 2 from changing order of `(c, d)`, and 2 from swapping `(a, b)` and `(c, d)`.
    - If there are `freq` pairs of generating the product, then `freq` choose 2 is total permutations.
    - > `freq * (freq - 1) / 2` cases occurred.

3. Multiply every permutation for each product, then sum them up.
  
## Solutions
```python
# Complexity O(n)
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        count = {}
        ans = 0

        for i in range(n):
            for j in range(i+1, n):
                prod = nums[i] * nums[j]

                if prod in count:
                    count[prod] += 1
                else:   
                    count[prod] = 1

        for prod, freq in count.items():
            ans += freq * (freq - 1) * 4

        return ans
```
