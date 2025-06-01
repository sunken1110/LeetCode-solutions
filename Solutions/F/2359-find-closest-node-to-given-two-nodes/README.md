**Find Closest Node to Given Two Nodes**
=
[Problem Link](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description)

## Intuition

Suppose two nodes start to move simultaneously. Since each node has at most one outgoing edge, the targets are the first 
nodes that both nodes finish to visit. We start from both `node1` and `node2`, and traverse along each edge. For each 
move, we mark the minimum distance of both starting nodes `dist1`, `dist2`. Keep moving until both traverse visit same node, 
and then get that node with maximum distance of it. Since we want to minimize the index of the answer, we use min heap 
to return the correct index.

## Approach
**Step-by-Step Process**

1. Initialize the queue with `node1`,`node2` and the distance arrays `dist1`, `dist2`.
    - To compute the maximum distance, store both node and distance.
  
2. Construct a DFS which traverse along the edge.

3. If two paths intersect, store the index of the intersection and the maximum distance in min heap `ans`.
    - No extra traverse is needed.
    - Multiple intersections can be returned.

4. Return the minimum index among target nodes.
  
## Solutions
```python
# Time Complexity O(n), Space Complexity O(n)
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        dist1 = [-1] * n
        dist2 = [-1] * n
        queue = deque([(node1, 0, 1), (node2, 0, 2)])
        ans = []
        
        while queue:
            node, depth, i = queue.popleft()

            if i == 1:
                if dist1[node] >= 0:
                    continue

                dist1[node] = depth

            else:
                if dist2[node] >= 0:
                    continue

                dist2[node] = depth

            if dist1[node] != -1 and dist2[node] != -1:
                heapq.heappush(ans, (max(dist1[node], dist2[node]), node))

            elif edges[node] != -1:
                queue.append([edges[node], depth+1, i])

        return ans[0][1] if ans else -1
```
