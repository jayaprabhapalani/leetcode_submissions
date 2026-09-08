import heapq
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        heap=[]
        for i in arr:
            #push the (distance, val)
            heapq.heappush(heap,(-abs(i-x),-i))

            if len(heap)>k:
                heapq.heappop(heap)
        
        return sorted([-val for dist, val in heap])
        