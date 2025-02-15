**Product of the Last K Numbers**
=
[Problem Link](https://leetcode.com/problems/product-of-the-last-k-numbers/description)

## Intuition
Note that the product of the last `k` integers of length `n` list is equal to the product of every integer 
of the list divide by the product of every integer except last `k` integers.
That is, every output of `getProduct` can be calculated by cumulative products.

## Approach
**Step-by-Step Process**

1. Initialize a current cumulative product `prod` and the container list `pref_list`.

2. Define `add` by cumulative product. Initialize current product if `num` meets 0.

3. Calculate the return of `getProduct`.
    - If `len(self.pref_list) < k`, target integers eventually meets 0, so return 0.
    - If `len(self.pref_list) > k`, the return value is  `self.pref_list[-1]` divide by `self.pref_list[-1-k]`.

## Solutions
```python
# Complexity O(1)
class ProductOfNumbers:

    def __init__(self):
        self.prod = 1
        self.pref_list = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = 1
            self.pref_list = []
        
        else:
            self.prod *= num
            self.pref_list.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.pref_list) < k:
            return 0

        elif len(self.pref_list) == k:
            return self.pref_list[-1]

        else:
            return self.pref_list[-1] // self.pref_list[-1-k]
