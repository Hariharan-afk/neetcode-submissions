class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        hash_map = defaultdict(list)

        for index,num in enumerate(nums):
            hash_map[num].append(index)

        for i in range(len(nums)):
            diff = target - nums[i]
            
            if diff in hash_map:
                for j in hash_map[diff]:
                    if j!=i:
                        return [min(i, j), max(i, j)]

            
            
