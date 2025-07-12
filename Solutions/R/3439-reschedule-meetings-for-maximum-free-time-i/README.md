**Reschedule Meetings for Maximum Free Time I**
=
[Problem Link](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/description)

## Intuition
The crucial constraint is that the relative order of all meetings should be conserved. Our approach is to compute
the information of gaps between each consecutive meetings, and then apply sliding window technique to get the 
maximum free time by sum consecutive `k+1` gaps.

## Approach
**Step-by-Step Process**

1. Initialize `gaps` and compute the gaps between each two consecutive meetings.

2. Start from the first `k+1` sum of gaps, apply sliding window to get the maximum free time.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        gaps = []
        prev = 0

        for i in range(n):
            gaps.append(startTime[i] - prev)
            prev = endTime[i]

        gaps.append(eventTime - prev)
        free = sum(gaps[:k+1])
        max_free = free

        for i in range(n-k):
            free += gaps[i+k+1] - gaps[i]
            max_free = max(max_free, free)

        return max_free
```
