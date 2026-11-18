

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)     # key -> list of words with that key
        for word in strs:
            key = "".join(sorted(word))  # same letters in the same order for  anagrams
            groups[key].append(word)
        return list(groups.values())

        
            



