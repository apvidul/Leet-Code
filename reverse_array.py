class Solution(object):
    def rotate(self, nums, k):
        
        if len(nums)==1:
            return
        
        k = k % len(nums)
        
        if k!=0:
        
            first = nums[:-k]
            last = nums[-k:]     

            nums[:k] = last
            nums[k:] = first
