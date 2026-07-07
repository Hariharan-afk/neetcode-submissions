class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left<=right:
            i = right-left//2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                right = i-1
            else:
                left = i+1
        return -1
