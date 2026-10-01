class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        sequence_length = 0
        arraytoset = set(nums) # first we convert nums to a hash set
        for num in nums:
            if num -1 not in arraytoset: # we start building the sequence
                curr_length = 0
                while (num + curr_length) in arraytoset:
                    curr_length += 1
                sequence_length = max(sequence_length,curr_length)
        return sequence_length