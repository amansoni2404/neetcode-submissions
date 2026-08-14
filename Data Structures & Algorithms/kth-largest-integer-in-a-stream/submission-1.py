import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # make a min heap of size k
        self.k = k
        self.heap = []
        heapq.heapify(self.heap)
        for i in range(len(nums)):
            if len(self.heap) < k:
                heapq.heappush(self.heap, nums[i])
            else:
                if nums[i] <= self.heap[0]:
                    # a no. samller than heap[0] wouldd never be k largest, so it is not important to add it in the heap
                    pass
                else:
                    # if the no. if greater than the heap[0] it could possibly replace the kth largest element, so we pop the current root and add this new no. in the heap
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, nums[i])
        # print("Final Heap Initial:", self.heap)


    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
                heapq.heappush(self.heap, val)
        else:
            if val <= self.heap[0]:
                # a no. samller than heap[0] wouldd never be k largest, so it is not important to add it in the heap
                pass
            else:
                # if the no. if greater than the heap[0] it could possibly replace the kth largest element, so we pop the current root and add this new no. in the heap
                heapq.heappop(self.heap)
                heapq.heappush(self.heap, val)
        return self.heap[0]

        
