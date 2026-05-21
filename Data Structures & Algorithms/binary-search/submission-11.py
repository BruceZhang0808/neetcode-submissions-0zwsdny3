import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pos = bisect.bisect_left(nums, target)
        return pos if pos < len(nums) and nums[pos] == target else -1