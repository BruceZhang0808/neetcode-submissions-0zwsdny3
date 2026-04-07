class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for l in s:
                counts[ord(l) - ord('a')] += 1
            output[tuple(counts)].append(s)
        return list(output.values())