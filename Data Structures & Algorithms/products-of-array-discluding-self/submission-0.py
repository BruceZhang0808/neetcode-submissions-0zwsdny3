class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = [1], [1]
        res = []
        for i in range(len(nums) - 1):
            prefix.append(nums[i] * prefix[i])
        for i in range(len(nums) - 1):
            j = len(nums) - 1 - i
            suffix.append(nums[j] * suffix[i])
        for i in range(len(nums)):
            j = len(nums) - 1 - i
            res.append(prefix[i] * suffix[j])
        return res