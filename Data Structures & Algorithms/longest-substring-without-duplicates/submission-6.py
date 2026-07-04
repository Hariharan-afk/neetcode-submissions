class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        my_dict = defaultdict(int)
        i = 0
        j = 0
        max_count = 0
        count = 0
        while j < len(s):
            if my_dict[s[j]]==0:
                my_dict[s[j]]+=1
                count+=1
                if count > max_count:
                    max_count = count
            elif my_dict[s[j]]>0:
                while i < j:
                    if s[i] == s[j]:
                        my_dict[s[i]] -= 1
                        count -= 1
                        i+=1
                        break
                    my_dict[s[i]] -= 1
                    count -= 1 
                    i+=1
                my_dict[s[j]]+=1
                count+=1
                if count > max_count:
                    max_count = count 
            j+=1
        return max_count