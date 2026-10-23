class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        clean=[]
        zeros=[]
        for i in range(len(nums)):
            if nums[i]==0:
                zeros.append(nums[i])
            else:
                clean.append(nums[i])
        nums[:]=clean+zeros
        print(nums)