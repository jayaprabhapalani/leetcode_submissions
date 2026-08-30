"""
Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.
Each student is assigned a contiguous sequence of books.
No book is assigned to more than one student.
All books must be allocated.
The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum. If it is not possible to allocate books to all students, return -1;

Note: Test cases are generated such that the answer always fits in a 32-bit integer.

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
=> [12] and [34, 67, 90] Maximum Pages = 191
=> [12, 34] and [67, 90] Maximum Pages = 157
=> [12, 34, 67] and [90] Maximum Pages = 113.
The third combination has the minimum pages assigned to a student which is 113.
Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.
"""
class Solution:
    def findPages(self, arr, k):
        if len(arr)<k:
            return -1
        # code here
        l=max(arr)
        h=sum(arr)
        ans=-1
        while(l<=h):
            limit=l+(h-l)//2 #mid calculation
            
            if self.valid_book_allocation(arr,k,limit):
                ans=limit
                h=limit-1
            else:
                l=limit+1
        return ans
                
    def valid_book_allocation(self,arr,k,limit):  
        #book allocation calculation
        std_cnt=1
        pages=0
        for book in arr:
            if pages+book>limit :
                std_cnt+=1
                pages=book
            else:
                pages+=book
        
        return std_cnt<=k

                
                    
                
                
            
