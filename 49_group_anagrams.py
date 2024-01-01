from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            k = "".join(sorted([x for x in i]))
            res[k].append(i)
        return res.values()