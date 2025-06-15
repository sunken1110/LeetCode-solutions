**Zero Array Transformation III**
=
[Problem Link](https://leetcode.com/problems/zero-array-transformation-iii/description)

## Intuition
This is an application of [Problem Link](https://leetcode.com/problems/zero-array-transformation-i/description). 

Since we want to remove as many as possible, chosen queries must cover wider range than non-chosen queries. The idea 
is that for each `(idx, num)` in `nums`, take every queries that starts with `idx` in `max_heap`. Pop wider queries 
first until the number of queries matches `num`, and store the prefix sum to `pref[idx]`. Next, move to `idx+1` 
and set the current prefix sum `curr`. Repeat the above process. If the process successfully finished for every index, 
then the remained queries in `max_heap` are unnecessary to make a zero array transformation. 

## Approach
**Step-by-Step Process**

1. Initialize a max-heap `max_heap`, prefix sum `pref`, and current sum `curr`.

2. Sort `queries` by the starting index.

3. For each `(idx, num)` in `nums`, push queries which starting index match `idx` into `max_heap`.

4. Adjust the prefix sum of `idx-1` to `curr`.

5. Until `curr` matches `num`, heappop the widest query from `max_heap`.
    - Adjust `curr` and the future `pref`.
  
6. Return the number of remaining queries of `max_heap`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        max_heap = []
        curr = 0
        pref = [0] * (n+1)
        
        queries.sort(key=lambda x: -x[0])

        for idx, num in enumerate(nums):
            while queries and idx == queries[-1][0]:
                heappush(max_heap, -queries.pop()[1])
                
            curr += pref[idx]

            while max_heap and idx <= -max_heap[0] and num > curr:
                curr += 1
                pref[-heappop(max_heap) + 1] -= 1
            
            if num > curr:
                return -1

        return len(max_heap)
```
