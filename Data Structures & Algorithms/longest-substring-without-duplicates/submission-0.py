class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        encountered = set()
        result = []
        i,j, max_len = 0,0,0
        while j < len(s):
            if s[j] not in encountered:
                encountered.add(s[j])
                result.append(s[j])
                j += 1
            else:
                removed_char = result[0]
                result.remove(removed_char)
                encountered.remove(removed_char)
                i += 1
            max_len = max(max_len, len(result))
        return max_len
        
        