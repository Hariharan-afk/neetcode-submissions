class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        dictionary = {}
        
        for index,num in enumerate(nums):
            diff = target - num
            if diff in dictionary:
                j = dictionary[diff]
                return [min(index, j), max(index, j)]
            else:
                dictionary[num] = index
        