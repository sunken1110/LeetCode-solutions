**Vowel Spellchecker**
=
[Problem Link](https://leetcode.com/problems/vowel-spellchecker/description)

## Intuition
First, we make two dictionaries based on the original(base) word; one is a conversion of capitalization and the 
other is a conversion of vowel errors. Then check whether each `word` of `queries` is either a case of capitalization, 
vowel errors, or nothing.

## Approach
**Step-by-Step Process**

1. Initialize `capital` and `vowel`, refer the dictionaries of capitalization and vowel errors, respectively.

2. For each `word` in `queries`, check if `word` is one of the target of spellchecker.
    - For an effective search of exact match in `wordlist`, initialize `wordset` as a set first.
    - If `word` is the target of capitalization, append the first base word of `capital`.
    - Next, if `word` is the target of vowel errors, append the first base word of `vowel`.
  
## Solutions
```python
# Time Complexity O((m+n)*l), Space Complexity O(n*l)
# where m is the size of queries, n is the size of wordlist, and l is the max length of words
class Solution:
    def spellchecker(self, wordlist, queries):
        wordset = set(wordlist)
        capital = defaultdict(list)
        vowel = defaultdict(list)
        ans = []

        for word in wordlist:
            original = word.lower()
            capital[original].append(word)

            for char in 'aeiou':
                original = original.replace(char, '*')

            vowel[original].append(word)

        for word in queries:
            if word in wordset:
                ans.append(word)

            else:
                original = word.lower()

                if original in capital:
                    ans.append(capital[original][0])

                else:
                    for char in 'aeiou':
                        original = original.replace(char, '*')

                    if original in vowel:
                        ans.append(vowel[original][0])

                    else:
                        ans.append('')

        return ans
```
