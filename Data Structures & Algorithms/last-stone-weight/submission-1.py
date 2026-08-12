import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = -heapq.heappop(stones)
            second_largest = -heapq.heappop(stones)
            if largest != second_largest:
                diff = abs(largest - second_largest)
                heapq.heappush(stones, -diff)
        if len(stones) == 1:
            return -stones[0]
        else:
            return 0

        