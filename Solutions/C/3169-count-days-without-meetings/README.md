**Count Days Without Meetings**
=
[Problem Link](https://leetcode.com/problems/count-days-without-meetings/description)

## Intuition
We first sort `meetings`, then check if any overwrap exists between each meeting. 
If overwrap occurred, merge two meetings as one meeting and then move to next meeting. 
If not, check the previous end day of meeting and count the gap between two meetings.

## Approach
**Step-by-Step Process**

1. Sort `meetings` to easily check the overwrapping.

2. Initialize the end date of previous meeting `prev_end`.

3. For each meeting, check if `start` is later than `prev_end`.
    - If so, then count the gap between two meetings.
    - If not, merge two meeting and renew `prev_end`.

4. After the iteration, count the remained days of `days`.
  
## Solutions
```python
# Complexity O(n*log(n))
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        prev_end = 0
        cnt = 0

        meetings.sort()

        for start, end in meetings:
            if start > prev_end + 1:
                cnt += start - prev_end - 1

            prev_end = max(prev_end, end)

        cnt += days - prev_end

        return cnt
