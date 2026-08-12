import math
import heapq
class Solution:
    def calulcate_distance(self, x, y):
        distance = math.sqrt((x**2)+(y**2))
        return distance

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for i in range(len(points)):
            calculated_distance = self.calulcate_distance(points[i][0], points[i][1])
            heapq.heappush(heap, (calculated_distance, points[i]))
        kclosest = []
        for i in range(k):
            popped_element = heapq.heappop(heap)
            kclosest.append(popped_element[1])
        
        return kclosest
        