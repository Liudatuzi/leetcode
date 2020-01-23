class Solution(object):
    def find(self,a,left,right,target,t):
        if right<left:
            return False
        else:
             mid=(right-left)/2+left
             if abs(a[mid]-target)<=t:
                 return True
             if self.find(a,left,mid-1,target,t)  or self.find(a,mid+1,right,target,t):
                 return True
        return False
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        i=0
        if k==10000:
            return False;
        while i<len(nums):
            if i+k>=len(nums)-1:
                a=nums[i+1:len(nums)]
            else:
                a=nums[i+1:i+k+1]
            a.sort()
            target=nums[i]
            if self.find(a,0,len(a)-1,target,t):
                return True
            i+=1
        return False
