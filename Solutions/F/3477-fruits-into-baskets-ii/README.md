**Fruits Into Baskets II**
=
[Problem Link](https://leetcode.com/problems/fruits-into-baskets-ii/description)

## Intuition
For each fruit, scan the first basket which has a capacity to hold the quantity of that fruit. Remove that basket and 
update the number of used baskets. Repeat until every fruit is checked, then return the number of remained baskets.

## Approach
**Step-by-Step Process**

1. Initialize the number of used baskets `cnt`.

2. For each `fruit`, find the first basket `j` that `fruit` <= `baskets[j]`.
    - Nullify `baskets[j]` and update `cnt`.

3. The number of unused baskets is `len(fruits) - cnt`.

## Solutions
```python
# Time Complexity O(n*m), Space Complexity O(1)
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        cnt = 0

        for fruit in fruits:
            for j in range(n):
                if fruit <= baskets[j]:
                    cnt += 1
                    baskets[j] = 0
                    break

        return n-cnt
```
