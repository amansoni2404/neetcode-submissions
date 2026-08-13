import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        res = []
        heapq.heapify(heap)
        for key,freq in counter.items():
            heapq.heappush(heap, (-freq, key))
        for i in range(k):
            popped_tuple = heapq.heappop(heap)
            res.append(popped_tuple[1])
    
        return res



        
        