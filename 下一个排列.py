# 下一个排列
# 倒叙遍历，寻找第一个升序
# 调换升序，将调换后左边数字的右边按升序排列
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1:
            return
        else: 
            # 遍历倒序，找第一个升序序列，即找到:nums[i] < nums[i + 1]
            i = n - 2
            while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
            
            if i >= 0:
                j = n - 1
                while j >= 0 and nums[i] >= nums[j]:
                    j -= 1
                # 交换i, j
                nums[i], nums[j] = nums[j], nums[i]
            
            # 将nums[i + 1: ]按升序排列
            left, right = i + 1, n - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
            return
