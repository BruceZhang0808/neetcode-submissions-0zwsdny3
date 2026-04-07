class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDup = []
        for num in nums:
            if num in noDup:
                return True
            noDup.append(num)
        return False