class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()  # Initialize an empty set
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)  # Add the element to the set
        return False
