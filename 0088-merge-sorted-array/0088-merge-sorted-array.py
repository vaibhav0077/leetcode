class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for x in nums2:
            nums1[m] = x
            m+=1
        
        nums1.sort()
        