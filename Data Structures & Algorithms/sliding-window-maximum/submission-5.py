class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        j = k - 1
        ans = []
        max_value = -10000
        while j < len(nums):
            i = j - k + 1
            while i<=j:
                if nums[i] > max_value:
                    max_value = nums[i]
                i+=1
            ans.append(max_value)
            max_value = -10000
            j+=1
        return ans

        