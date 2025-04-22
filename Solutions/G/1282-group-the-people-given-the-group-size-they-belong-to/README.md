**Group the People Given the Group Size They Belong To**
=
[Problem Link](https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description)

## Intuition
Note that every person is belonged to one of groups, so any group of size `size` reveals exactly 
multiples of `size` times in `groupSizes`. Then we can partition by `size` while scanning `groupSizes`, by 
append corresponding indices to `defaultdict` and if the size of partition meets to `size` then pop it up.

## Approach
**Step-by-Step Process**

1. Initialize `groups` as `defaultdict`.
  
2. For each `size` in `groupSizes`, store the corresponding index to each partition `groups[size]`.

3. If the size or partition meets to `size`, then append it to `ans` and reset `groups[size]` as a new partition.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        ans = []

        for idx, size in enumerate(groupSizes):
            groups[size].append(idx)

            if len(groups[size]) == size:
                ans.append(groups[size])
                groups[size] = []

        return ans
```
