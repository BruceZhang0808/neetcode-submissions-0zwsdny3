class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for num in store:
            if (num - 1) not in store:
                streak, cur = 1, num + 1
                while cur in store:
                    streak += 1
                    cur += 1
                res = max(res, streak)
        return res