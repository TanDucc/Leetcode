from typing import List
from collections import defaultdict

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        res[tuple(count)].append(s)
    return list(res.values())    

# Example usage:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))  

#def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
 #       mp = {}
 #       res = []
 #       for s in strs: 
 #           key = tuple(sorted(s)) 
#          if key in mp: 
#                mp[key].append(s)
#          else:               
#                mp[key] = [s]
#        for l in mp.values():
#            res.append(l)

#        return res