class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() # implement a hash table
        for num in nums: # for each number in nums
            if num in seen: # if it shows up in hash table
                return True # return true
            else:
                seen.add(num) # otherwise add to hash table
        return False 
                

        