**Maximum Candies You Can Get from Boxes**
=
[Problem Link](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description)

## Intuition
BFS is a good approach here. Check the opened boxes from `initialBoxes` and collect candies in it. If there exists 
any key, then update corresponding `status` to be opened. As a BFS step, add boxes inside `containedBoxes` to the 
queue. Repeat until we visit every avaiable boxes. To avoid multiple visits, we use `visited`.

## Approach
**Step-by-Step Process**

1. Initialize `queue` and `visited`.

2. For `box` in `initialBoxes`, append opened boxes first to `queue`.
    - To do this process easier, we use `appendleft` of `deque` structure.
  
3. Since `box` is now visited, update `visited` and collect candies.

4. If there exists any `key` inside `box`, then update `status[key]` to be opened.

5. If there exists any `new_box` inside `box`, then again append opened boxes first to `queue`.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        cnt = 0
        visited = set()
        queue = deque()

        for box in initialBoxes:
            if status[box]:
                queue.appendleft(box)
            
            else:
                queue.append(box)
                
        while queue:
            box = queue.popleft()
            
            if box in visited or status[box] == 0:
                continue

            visited.add(box)
            cnt += candies[box]

            for key in keys[box]:
                status[key] = 1

            for new_box in containedBoxes[box]:
                if status[new_box]:
                    queue.appendleft(new_box)

                else:
                    queue.append(new_box)

        return cnt
```
