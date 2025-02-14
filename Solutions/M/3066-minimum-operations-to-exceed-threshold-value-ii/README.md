**Minimum Operations to Exceed Threshold Value II**
=
[Problem Link](https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description)

## Intuition
To easily find the two smallest integers in `nums`, we use heap structure. Since every operations replace 
2 elements to 1 element, the total number of operations is at most `len(nums)`.

## Approach
**Step-by-Step Process**

1. Heapify `nums` to extract the smallest integer.

2. Within `len(nums)` iterations, process operations.

3. With `sum_set = defaultdict(list)`, push numbers in each digit sum.
    - If the smallest integer exceed the threshold `k`, break.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        ans = 0

        for i in range(len(nums)):
            x = heappop(nums)
   
            if x < k:
                y = heappop(nums)
                z = x*2 + y if x < y else y*2 + x
                heappush(nums, z)
                ans += 1

            else:
                break

        return ans
