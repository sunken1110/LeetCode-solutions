**Minimum Time to Repair Cars**
=
[Problem Link](https://leetcode.com/problems/minimum-time-to-repair-cars/description)

## Intuition
The task is to minimize the time, which is determined by the maximum reparing time of all mechanics. 
Then we can solve it with binary search with required time; we fix the total repairing time, count every 
mechanic's fixable cars, then check if the number of total fixed cars exceeds `cars`.

## Approach
**Step-by-Step Process**

1. Define `check` which returns if `cars` number of cars can be fixed in `minute`.
    - Since each mechanic with rank `r` can repair `n` cars in `r * n^2` minute, `n = int(sqrt(minute/r))`.

2. Since mechanics with same rank have exactly same ability to fix, we use `Counter` for efficiency.

3. Between the lower bound `left` and upper bound `right`, do a binary search.
    - For `right`, the worst case is that all of the mechanics are as same as the lowest rank mechanic.

## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def check(minute):
            done = 0

            for rank, mechanic in ranks.items():
                done += mechanic * int(sqrt(minute / rank))

            return done >= cars

        ranks = Counter(ranks)
        left = 0
        right = max(ranks) * ceil(cars / len(ranks))**2

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid

            else:
                left = mid + 1

        return left
```
