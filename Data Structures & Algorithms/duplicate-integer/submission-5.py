from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums) # create counter hashmap
        for key , value in count.items():
            if value > 1:
                return True
        return False