class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        #it is just simple as max area of histogram -just convert the 2d array into 1d at each row lvl ----histogram then find the max for it ---> finally find the max area among the histogram
        """
        MAH approach- #intution---> height[i]*width
        #width=right_bound-left_bound-1
        #right boundary=next smallest element index
        #left boundary=previous smallest element index
        #needed things- stack,max_area var,left and right arr boundary( left with -1 and right with n(len)) , the one loop to calculate the max
        
        """
        #so t.c is O(3n*m)+ 2d to 1 d for that O(nm)
        if not matrix:
            return 0
        
        max_area=0
        n=len(matrix)
        m=len(matrix[0])
        hist=[0]*m # the no of elements based of the column and the no of hist is based on row
        for i in range(n):
            for j in range(m):
                if matrix[i][j]=="1":
                    hist[j]+=1
                else:
                    hist[j]=0
            #calculate max area at row level

            max_area=max(max_area,self.max_area_hist(hist))
        return max_area

    def max_area_hist(self,hist:List[int])->int:
        stack=[]
        n=len(hist)
        left=[-1]*n
        right=[n]*n
        max_area=0
        #nsl
        for i in range(n):
            while stack and hist[stack[-1]]>=hist[i]:
                stack.pop()
            left[i]=stack[-1] if stack else -1
            stack.append(i)
        #nsr
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and hist[stack[-1]]>=hist[i]:
                stack.pop()
            right[i]=stack[-1] if stack else n 
            stack.append(i)
        #max_area cal
        for i in range(n):
            area=hist[i]*(right[i]-left[i]-1)
            max_area=max(max_area,area)
        return max_area