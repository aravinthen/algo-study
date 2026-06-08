class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_anagrams = {}
        for s in strs:
            sort_s = "".join(sorted(s))

            if sort_s not in all_anagrams:
                all_anagrams[sort_s] = [s]
            else:
                all_anagrams[sort_s].append(s)
        
        result = []
        for i in all_anagrams:
            result.append(all_anagrams[i])
        
        return result