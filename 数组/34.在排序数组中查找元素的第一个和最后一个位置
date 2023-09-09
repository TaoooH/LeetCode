class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        else:
            left = self.leftMargin(nums, target)
            right = self.rightMargin(nums, target)
            return [left, right]

    def leftMargin(self, nums: List[int], target: int):
        # 确定左边界
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            # 一直寻找到第一个target左边值的index，防止重复的target
            if nums[mid] == target:
                right = mid - 1 
            elif nums[mid] > target:
                right = mid - 1
            # 最后一个循环中mid在第一个target左边，通过mid + 1找到左边界
            else:
                left = mid + 1
        if nums[left] == target:
            return left
        else:
            return -1
    
    def rightMargin(self, nums: List[int], target: int):
        # 确定右边界，原理同左边界
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        if nums[right] == target:
            return right
        else:
            return -1 
