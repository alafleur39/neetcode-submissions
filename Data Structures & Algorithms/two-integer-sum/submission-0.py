class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} # initlize hash_map
        for i in range(len(nums)): #iterate nums array
            difference = target - nums[i] # what number do i need to complete the pair
            if difference in hash_map: # if we find the difference in our hashmap
                return [hash_map[difference],i] # return that pair in a set
            hash_map[nums[i]]=i #store each element in our hashmap 
       