class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        my_dict = defaultdict(int)
        max_count = 0
        i = 0
        j = 0
        while j < len(s):
            my_dict[s[j]]+=1 
            if (j - i + 1) - max(my_dict.values()) > k:
                while i < j:
                    my_dict[s[i]]-=1
                    i+=1
                    if (j - i + 1) - max(my_dict.values()) <= k:
                        break
            window_size = j - i + 1
            if window_size > max_count:
                max_count = window_size
            j+=1
        return max_count


            
        