class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=sorted(list(set(nums)))
        print(s)
        max_count=0
        for i in range(len(s)):
            if i==0 and s[i]!='':
                count = 1
                if count>max_count:
                    max_count=count
            elif not s:
                return 0
            if i>0 and s[i] == s[i-1] + 1:
                count+=1
                if count>max_count:
                    max_count=count
            elif i>0 and s[i] != s[i-1] + 1:
                count = 1
        return max_count
 
            