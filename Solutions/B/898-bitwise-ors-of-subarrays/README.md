**Bitwise ORs of Subarrays**
=
[Problem Link](https://leetcode.com/problems/bitwise-ors-of-subarrays/description)

## Intuition
Naive approach is enough.

## Approach
**Step-by-Step Process**

1. Initialize the previous bitwise ORs `prev`.

2. For each `num` in `arr`, add `num` OR all `i`s in `prev`.

3. Update the possible bitwise OR values and `prev`.
  
## Solutions
```python
# Time Complexity O(n^2), Space Complexity O(n)
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev = set()

        for num in arr:
            curr = {num}

            for i in prev:
                curr.add(i|num)

            ans.update(curr)
            prev = curr

        return len(ans)
```
