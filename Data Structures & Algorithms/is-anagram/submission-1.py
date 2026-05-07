class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_in_list = list(s)
        t_in_list = list(t)

        sorted_s = sorted(s_in_list , key = str.lower)
        sorted_t = sorted(t_in_list ,  key = str.lower)

        joined_s = "".join(sorted_s)
        joined_t = "".join(sorted_t)

        if joined_s == joined_t:
            return True
        
        return False