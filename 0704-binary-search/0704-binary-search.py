class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        mid = right//2
        
        while left <= right:
            
            if nums[mid] == target:
                return mid
            
            mid = (left + right)//2
            if target > nums[mid]:
                left = mid+1
              
            elif target < nums[mid]:
                right = mid-1
               
          
        return -1
        