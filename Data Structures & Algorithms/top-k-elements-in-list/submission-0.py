import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums) # dictionary of each 
        heap = []

        for num , freq in counter.items():
        
            heapq.heappush(heap,(freq,num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [t[1] for t in heap]


        
       