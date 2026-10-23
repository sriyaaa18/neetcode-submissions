class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen=set()
        for num in nums:
            seen.add(num)
        nums[:]=seen
        nums.sort()
        return len(nums)
        