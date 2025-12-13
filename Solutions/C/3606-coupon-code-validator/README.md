**Coupon Code Validator**
=
[Problem Link](https://leetcode.com/problems/coupon-code-validator/description)

## Intuition
We first construct a method `is_valid` to check if a code is valid string. Also construct `order` to give an order 
of `businessLine`. Filter coupons which satisfy 3 validation test, and append to temporary array `val` in the 
order of `order`. Return the code in the order of sorted `val`.

## Approach
**Step-by-Step Process**

1. Declare `is_valid`.
    - Replace `'_'` to `''`.
    - Check if a string `s` contains only alphanumeric characters or an empty string (an edge case of `s` = `'_'`).

2. Construct a dictionary `order` in the order of `businessLine`.

3. For each coupon, do a validity check and append to `val` in the order of `order`.

4. Sort `val`, and return the corresponding codes.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        def is_valid(s):
            if len(s) == 0:
                return False

            s = s.replace('_', '')

            return s.isalnum() or s == ''


        order = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        val = []

        for c, b, i in zip(code, businessLine, isActive):
            if is_valid(c) and (b in order) and i:
                val.append((order[b], c))

        val.sort()

        return [c for _, c in val]
