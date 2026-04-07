class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDup = set()
        for num in nums:
            if num in noDup:
                return True
            noDup.add(num)
        return False