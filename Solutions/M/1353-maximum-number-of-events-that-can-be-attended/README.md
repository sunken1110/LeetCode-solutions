**Maximum Number of Events That Can Be Attanded**
=
[Problem Link](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/description)

## Intuition
First we sort `events` to align multiple events with same start day. Then push them to the min-heap, and pop each 
event in order while updating already attended event day. If an event is attendable then count it, if not then just 
pop it up. Repeat this process until we check every event schedule.

## Approach
**Step-by-Step Process**

1. Initialize `min_heap` and sort `events`.

2. Starts from the first event, push all the other events with same start day.

3. Pop `min_heap` in order of end date.
    - If the day is attendable, then `cnt += 1`.
    - If not, just pop it up.

4. Repeat the process.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        cnt = 0
        start = -1
        idx = 0
        min_heap = []

        while idx < n or min_heap:
            if not min_heap:
                start = events[idx][0]

            while idx < n and events[idx][0] == start:
                heappush(min_heap, events[idx][1])
                idx += 1

            heappop(min_heap)
            cnt += 1
            start += 1

            while min_heap and min_heap[0] < start:
                heappop(min_heap)

        return cnt
```
