import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m=len(matrix)
        max_heap=[]
        for i in range(m):
            for j in range(len(matrix[0])):
                heapq.heappush(max_heap,-matrix[i][j])

                if len(max_heap)>k:
                    heapq.heappop(max_heap)
        return -max_heap[0]
                

        
        