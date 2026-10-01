from collections import Counter # counter counts hashable objects
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # if the length of the strings arent the same there's no point of checking
            return False

        s_dict = Counter(s)
        t_dict = Counter(t)
        
        return s_dict == t_dict

    
        
        

        
        