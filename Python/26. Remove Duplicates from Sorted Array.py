class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        for j in range(len(nums)-1):
            if nums[j] != nums[j+1]:
                nums[i] = nums[j+1]
                i += 1
        return i
        # 最後一次迴圈會i會多加一次，所以應該要扣1，但i是從1開始，所以return i
         
            
        