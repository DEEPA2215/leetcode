class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums=[]
        for i in nums1:
            if i in nums2:
                if i not in nums:
                    nums.append(i)
        return nums
               
                
           
        