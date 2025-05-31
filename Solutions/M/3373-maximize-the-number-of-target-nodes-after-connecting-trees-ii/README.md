**Maximize the Number of Target Nodes After Connecting Trees II**
=
[Problem Link](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description)

## Intuition
The main approach is similar to the following problem:
[Problem Link](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-i/description)

We use array `parity` to mark each node either even or odd. Note that two adjacent nodes have exactly reverse `parity` value. 
Then the maximum target value can be obtained by `max(sum(parity), number of nodes - sum(parity)`. We start from constructing 
a DFS which traverse every node and mark `parity`.


## Approach
**Step-by-Step Process**

1. Construct a DFS algorithm.
    - Without loss of generality, start from the node `0`.
  
2. Find the maximum parity sum of second tree.

3. For each node in the first tree, compute the sum of same parity nodes.
    - Conclude by adding the maximum value of second tree.
  
## Solutions
```python
# Time Complexity O(m+n), Space Complexity O(m+n)
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def dfs(graph, n):
            queue = deque([(0, -1, True)])
            parity = [-1] * n

            while queue:
                node, parent, even = queue.popleft()
                parity[node] = even

                for child in graph[node]:
                    if child == parent:
                        continue
                    
                    queue.append((child, node, not even))

            return parity


        graph1 = defaultdict(list)
        graph2 = defaultdict(list)

        for u, v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u, v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        m = len(edges1) + 1
        n = len(edges2) + 1
        even1 = dfs(graph1, m)
        even2 = dfs(graph2, n)
        sum1 = sum(even1)
        sum2 = sum(even2)

        max2 = max(sum2, n-sum2)

        return [max2 + (sum1 if even else m-sum1) for even in even1]
```
