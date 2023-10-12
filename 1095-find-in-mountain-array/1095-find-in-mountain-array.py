class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Find the peak element using binary search
        peak = self.findPeak(mountain_arr)

        # Search for the target in the left side of the mountain
        left_result = self.binarySearch(mountain_arr, target, 0, peak)
        if left_result != -1:
            return left_result

        # Search for the target in the right side of the mountain
        right_result = self.binarySearch(mountain_arr, target, peak, mountain_arr.length() - 1)
        return right_result

    def findPeak(self, mountain_arr: 'MountainArray') -> int:
        low, high = 0, mountain_arr.length() - 1
        while low < high:
            mid = (low + high) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                low = mid + 1
            else:
                high = mid
        return low

    def binarySearch(self, mountain_arr: 'MountainArray', target: int, low: int, high: int) -> int:
        ascending = mountain_arr.get(low) < mountain_arr.get(high)
        while low <= high:
            mid = (low + high) // 2
            mid_val = mountain_arr.get(mid)
            if mid_val == target:
                return mid
            if (mid_val < target) if ascending else (mid_val > target):
                low = mid + 1
            else:
                high = mid - 1
        return -1
