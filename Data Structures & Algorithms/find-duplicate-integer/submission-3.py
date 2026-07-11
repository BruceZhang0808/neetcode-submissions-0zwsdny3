class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                head = nums[0]
                while slow != head:
                    head = nums[head]
                    slow = nums[slow]
                return slow