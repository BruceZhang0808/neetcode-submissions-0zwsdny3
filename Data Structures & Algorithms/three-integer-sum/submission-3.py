class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n - 2):
            x = nums[i]
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue

            j, k = i + 1, n - 1
            while j < k:
                if nums[j] + nums[k] < -x:
                    j += 1
                elif nums[j] + nums[k] > -x:
                    k -= 1
                else:
                    ans.append([x, nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return ans