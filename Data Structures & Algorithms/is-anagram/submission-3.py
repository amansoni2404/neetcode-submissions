class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            freq_count = {}
            for i in range(0, len(s)):
                if s[i] in freq_count:
                    freq_count[s[i]] += 1
                else:
                    freq_count[s[i]] = 1
            for i in range(0, len(t)):
                if t[i] in freq_count:
                    freq_count[t[i]] -= 1
                else:
                    return False
        return (all(value == 0 for value in freq_count.values()))
