class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        j = len(s1)
        S1 = ''.join(sorted(s1))
        while j < len(s2)+1:
            S2 = ''.join(sorted(s2[i:j]))
            if S2 == S1:
                return True
            i+=1
            j+=1
        return False

        