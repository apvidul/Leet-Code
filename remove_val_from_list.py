class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i]==val:
                for j in range(i, len(nums)):
                    if nums[j]!=val:
                        nums[i]= nums[j]
                        nums[j]= val
                        break
                    if j== len(nums)-1:
                        return i
                        
