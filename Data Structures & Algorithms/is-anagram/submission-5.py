class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for i in list(s):
            if i in s_map:
                s_map[i] += 1
            else:
                s_map[i] = 1

        for i in list(t):
            if i in t_map:
                t_map[i] += 1
            else:
                t_map[i] = 1

        if s_map == t_map:
            return True
        else:
            return False