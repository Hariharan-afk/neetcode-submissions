class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0]*len(height)
        i = 0
        j = len(height) - 1
        max_volume = 0
        while i<=j:
            volume = min(height[i], height[j])
            if volume > max_volume:
                max_volume = volume
            water[i] = max_volume - min(max_volume, height[i])
            water[j] = max_volume - min(max_volume, height[j])
            if height[i]>=height[j]:
                j-=1
            else:
                i+=1
        return sum(water)
            


        