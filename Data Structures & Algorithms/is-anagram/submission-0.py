class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_map = {}
        s = s.lower()
        t = t.lower()
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            if s[i] in char_map:
                char_map[s[i]] += 1
            else:
                char_map[s[i]] = 1
        
        for i in range(0, len(t)):
            if t[i] in char_map:
                char_map[t[i]] -= 1
            else:
                return False
        # print("Char Map:", char_map)
        if all(value == 0 for value in char_map.values()):
            return True
        else:
            return False
        