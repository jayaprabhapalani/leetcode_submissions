import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in range(len(nums)):
            freq[nums[i]]=freq.get(nums[i],0)+1
        
        heap=[]
        for num, cnt in freq.items():
            heapq.heappush(heap,(cnt,num))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return [num for cnt ,num in heap]
       
        