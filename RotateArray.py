class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k > len(nums):
            k = k % len(nums)
        
        # Slice the list and rearrange it in place
        nums[:] = nums[-k:] + nums[:-k]     #nums[:] modifies the list inplace so the value changes outside the function
