class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 第一步：先排序，方便去重和使用双指针
        res = []
        
        for i in range(len(nums)):
            # 如果当前数字大于0，后面两个数也一定大于0，和不可能为0
            if nums[i] > 0:
                break
            
            # 去重：如果这个数字和前一个数字一样，跳过，避免结果重复
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # 使用双指针寻找剩余的两个数
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1  # 和太小，左指针右移
                elif total > 0:
                    right -= 1 # 和太大，右指针左移
                else:
                    # 找到了一组解
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # 找到解后，左右指针内部也要去重
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    # 移动到下一个可能的值
                    left += 1
                    right -= 1
                    
        return res