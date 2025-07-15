**Meeting Rooms III**
=
[Problem Link](https://leetcode.com/problems/meeting-rooms-iii/description)

## Intuition
We use 2 min-heaps to trace 1. currently booked rooms to find a room where the meeting ends the fastest and 
2. available rooms to allocate in ascending order. To proceed meetings from the fast one, sort `meetings` and 
trace the current time. If there is no available room then wait until the fastest meeting ends, else book a new room. 
Count the number of meetings when new room is booked, and then return the maximal counted room number.

## Approach
**Step-by-Step Process**

1. Sort `meetings` and initialize 2 min-heaps `rooms` and `booked`.

2. If `booked` is not empty and the end time of the fastest meeting is already passed, pop it up.

3. Start from the fastest meeting, allocate available rooms.
    - To trace the current time, `booked` store current time and room number.
    - Compute the end time of current meeting, and then push it with room number to `booked`.

4. Count the number of meeting while a new room is booked.

5. Return the smallest indexed room that held the most meetings.
   
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(n)
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = list(range(n))
        cnt = [0] * n
        booked = []

        for start, end in meetings:
            while booked and booked[0][0] <= start:
                heappush(rooms, heappop(booked)[1])

            gap = end - start

            if rooms:
                room = heappop(rooms)
                curr = start

            else:
                curr, room = heappop(booked)

            heappush(booked, (curr + gap, room))
            cnt[room] += 1

        return max(range(n), key=lambda x: cnt[x])
```
