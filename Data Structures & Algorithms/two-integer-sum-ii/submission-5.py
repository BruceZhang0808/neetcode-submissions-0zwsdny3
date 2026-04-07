class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        have = {}
        for i, num in enumerate(numbers):
            j = i + 1
            rest = target - num
            if rest in have:
                return [have[rest], j]
            have[num] = j