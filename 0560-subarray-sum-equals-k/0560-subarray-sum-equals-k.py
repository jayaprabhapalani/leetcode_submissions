class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ps=0
        freq={0:1} # because we are going to get this based on prefix sum - k , and if the first num is k then we need to get the cnt aswell so we are initializing with 0 sum as 1 cnt
        cnt=0
        for num in nums:
            ps+=num
            if ps-k in freq:
                cnt+=freq[ps-k]
            freq[ps]=freq.get(ps,0)+1
        return cnt
        