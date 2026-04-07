class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        need = {}
        for i, num in enumerate(numbers):
            j = i + 1
            rest = target - num
            if num in need:
                return [need[num], j]
            need[rest] = j