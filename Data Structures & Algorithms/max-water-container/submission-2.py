class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        left = 0
        right = len(heights) - 1
        while left<right:
            current_volume = min(heights[left], heights[right])*(right-left)
            if current_volume>max_volume:
                max_volume = current_volume
            if heights[left]>=heights[right]:
                right-=1
            else:
                left+=1
        return max_volume 

        