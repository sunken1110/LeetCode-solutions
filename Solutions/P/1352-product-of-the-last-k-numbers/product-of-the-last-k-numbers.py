#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# https://leetcode.com/problems/product-of-the-last-k-numbers/description

# Complexity O(1)
class ProductOfNumbers:

    def __init__(self):
        self.prod = 1
        self.pref_list = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prod = 1
            self.pref_list = []
        
        else:
            self.prod *= num
            self.pref_list.append(self.prod)

    def getProduct(self, k: int) -> int:
        if len(self.pref_list) < k:
            return 0

        elif len(self.pref_list) == k:
            return self.pref_list[-1]

        else:
            return self.pref_list[-1] // self.pref_list[-1-k]
