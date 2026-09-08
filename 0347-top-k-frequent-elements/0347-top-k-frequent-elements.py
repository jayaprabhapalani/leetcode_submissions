import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        heap=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        print(freq)

        for num , cnt in freq.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [cnt for num, cnt in heap]
           
       
       
        