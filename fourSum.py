'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。
这道题和三数之和有点区别，会出现负数，所以三数里的跳出语句不成立


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res=[]
        for i in range(len(nums)):
            # if nums[i]>target:
            #     return res
            newtarget=target-nums[i]
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1,len(nums)-1):
                left=j+1
                right=len(nums)-1
                # if nums[j]>newtarget:
                #     break
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                while left< right:
                    if nums[j]+nums[left]+nums[right]==newtarget:
                        res.append([nums[i],nums[j],nums[left],nums[right]])
                        while left<right and nums[left]==nums[left+1]:
                            left+=1
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        left+=1
                        right-=1
                    elif nums[j]+nums[left]+nums[right]<newtarget:
                            left+=1
                    elif nums[j]+nums[left]+nums[right]>newtarget:
                            right-=1
        return res
                        


