from collections import  defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for words in strs:
            counter = [0]*26
            for character in words:
                counter[ord(character)- ord('a')] += 1

            anagram_map[tuple(counter)].append(words)

        return list(anagram_map.values())
        