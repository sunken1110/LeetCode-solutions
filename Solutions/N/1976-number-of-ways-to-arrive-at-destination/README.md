**Number of Ways to Arrive at Destination**
=
[Problem Link](https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/description)

## Intuition
To find the shortest path, we use Dijkstra's algorithm with min heap. The goal is not just
the shortest path but the number of it, we also store count `cnt` while processing queues.

## Approach
**Step-by-Step Process**

1. Define `graph` to connect every intersection.
    - Append both city and time to `defaultdict`.
  
2. Construct the Dijkstra's algorithm with counter `cnt`.
    - Use heap data type structure `queue = (time, node)`.

3. For `next_node` in `graph[node]`, if the current path is faster then replace `cnt[next_node]` to `cnt[node]`.
    - Elif the current path is as fast as previous path, then accumulate `cnt[node]` to `cnt[next_node]`.

4. Return `cnt[n-1]` with modulus `10**9 + 7`.

## Solutions
```python
# Complexity O(m*log(n))
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        times = [inf] * n
        mod = 10**9 + 7
        cnt = [0] * n

        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))

        times[0] = 0
        cnt[0] = 1
        queue = [(0, 0)] # time, node for min_heap

        while queue:
            time, node = heappop(queue)

            if times[node] < time:
                continue

            for next_node, t in graph[node]:
                if times[node] + t < times[next_node]:
                    times[next_node] = times[node] + t
                    cnt[next_node] = cnt[node]

                    heappush(queue, (times[next_node], next_node))

                elif times[node] + t == times[next_node]:
                    cnt[next_node] = (cnt[next_node] + cnt[node]) % mod

        return cnt[n-1]
```
