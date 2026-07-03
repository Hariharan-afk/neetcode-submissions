class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answers = set()
        for i in range(len(nums)):
            target = -(nums[i])
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j] + nums[k] == target:
                    answer = [nums[i], nums[j], nums[k]]
                    answers.add(tuple(answer))
                if nums[j] + nums[k] > target:
                    k-=1
                else:
                    j+=1
        return list(answers)


        

        