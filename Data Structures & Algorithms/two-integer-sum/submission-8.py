class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from collections import defaultdict

        hash_map = defaultdict(list)
        
        for index,num in enumerate(nums):
            diff = target - num
            if diff in hash_map:
                for j in hash_map[diff]:
                    if j!=index:
                        return [min(index, j), max(index, j)]
            else:
                hash_map[num].append(index) 