class Solution:
    def maxArea(self, height: List[int]) -> int:
        area=0
        l=0
        r=len(height)-1
        while(l<r):
            min_height=min(height[l],height[r])
            area=max(area,(r-l)*min_height)
            if height[l]>=height[r]:
                r-=1
            else:
                l+=1    
        return area       
            
        