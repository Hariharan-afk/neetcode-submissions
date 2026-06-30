class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        hash_map = defaultdict(list)
        for i in range(len(strs)):
            print(strs[i])
            # hash_map[tuple(sorted(strs[i]))].append(strs[i])
            hash_map[''.join((sorted(strs[i])))].append(strs[i])
        return list(hash_map.values())


        