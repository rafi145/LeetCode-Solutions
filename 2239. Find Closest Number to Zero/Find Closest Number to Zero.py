class Solution(object):
    def findClosestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=nums[0]
        for num in nums:
            if (abs(num)<abs(mini)):
                mini = num
            elif abs(num)==abs(mini):
                mini = max(mini,num)
        return mini
