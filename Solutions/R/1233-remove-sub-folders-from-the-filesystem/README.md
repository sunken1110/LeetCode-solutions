**Remove Sub-Folders from the Filesystem**
=
[Problem Link](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description)

## Intuition
Note that the main-folder is always lexicographically faster than its sub-folder. Then if we sort `folder`, every 
main-folder always appear first. Thus, we only need to scan a sorted `folder`, detect main-folder and skip its sub-folder 
by comparing patterns. A sub-folder has a pattern of main-folder + `/` + sub-directory name, we first check this pattern 
occurrs. Also a sub-folder must starts with the name of main-folder. If these two conditions hold, then we can pass this 
folder until we find a new main-folder.

## Approach
**Step-by-Step Process**

1. Sort `folder`, which results a lexicographically ordered filesystem.

2. Scan folders to detect main-folders and sub-folders.
    - Start from the 'parent' main-folder.
    - If next folder `f` is a sub-folder of `parent`, then pass.
    - Else, replace `parent` to `f` and add to `ans`.
  
## Solutions
```python
# Time Complexity O(n*log(n)), Space Complexity O(1)
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        parent = '-'
        ans = []

        for f in folder:
            if parent + '/' in f and f.startswith(parent):
                continue

            else:
                parent = f
                ans.append(parent)

        return ans
```
