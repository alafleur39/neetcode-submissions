from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # create 2 hash tables
        freqS = Counter(s)
        freqT = Counter(t)

        if freqS == freqT:
            return True
        else: 
            return False



