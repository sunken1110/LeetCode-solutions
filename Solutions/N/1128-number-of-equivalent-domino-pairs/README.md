**Number of Equivalent Domino Pairs**
=
[Problem Link](https://leetcode.com/problems/number-of-equivalent-domino-pairs/description)

## Intuition
We scan every domino and store in `unique = defaultdict(int)` with ascending order. If the counter of each domino pair 
`(i, j)` increases, the number of equivalent pair increases as `unique[(i,j)]`. 

## Approach
**Step-by-Step Process**

1. For each domino, sort it by ascending order `(i, j)`.

2. Store each domino to `unique`.

3. In each step, add the counter by amount of `unique[(i, j)]`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        unique = defaultdict(int)
        cnt = 0

        for i, j in dominoes:
            if i > j:
                i, j = j, i

            cnt += unique[(i, j)]
            unique[(i, j)] += 1

        return cnt
```
