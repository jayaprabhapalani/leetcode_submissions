class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        next_greater={}
        # here finding the next element using stack and storing it in a hash as elements:greater_elements key-val pair to map to it to the given subset list
        for i in range(len(nums2)-1,-1,-1):
            while stack and stack[-1]<nums2[i]:
                stack.pop()

            next_greater[nums2[i]] = stack[-1] if stack else -1 

            stack.append(nums2[i]) 

        return [next_greater[num] for num in nums1]

        