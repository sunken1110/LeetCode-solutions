**Maximum Number of Events That Can Be Attended II**
=
[Problem Link](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/description)

## Intuition
We use 2-D DP to track the maximum sum of values. Since two chosen events can not be overwrapped, we first sort 
`events` by the end time of event. Also we use `bisect_right` to find the closest attendable event.
A DP table `dp[i][j]` denotes that the maximum value of `j` chosen events among first `i` events. 
For each event `i` we consider 2 cases, one is `i` is chosen and the other is `i` is not chosen. From the already 
computed DP table, compute the maximum value of accepted and not accepted, and then update it to `dp[i+1][j+1]`.

## Approach
**Step-by-Step Process**

1. Sort `events` with respect to the end time of events.

2. Initialize DP table `dp`.

3. For each event `i`, find the closest attendable event with binary search `bisect_right`.

4. For the number of considered events `j`, compute the value of chosen and not chosen cases of `i`th event.
    - Update the larger value to `dp[i+1][j+1]`.
  
## Solutions
```python
# Time Complexity O(nk + n*log(n)), Space Complexity O(nk)
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort(key=lambda x: x[1])
        dp = [[0] * (k+1) for _ in range(len(events)+1)]

        for i, (start, end, val) in enumerate(events):
            prev = bisect_right(events, start-1, key=lambda x: x[1])

            for j in range(k):
                accept = dp[prev][j] + val
                skip = dp[i][j+1]
                dp[i+1][j+1] = accept if accept > skip else skip

        return dp[-1][-1]
```
