#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/vowel-spellchecker/description

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
