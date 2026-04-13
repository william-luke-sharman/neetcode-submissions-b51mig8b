class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            counts = [0] * 26
            for c in s:
                counts[ord(c) - ord('a')] += 1
            counts = tuple(counts)
            res[counts] = res.get(counts,[]) + [s]
        
        return list(res.values())