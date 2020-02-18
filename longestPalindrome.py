import numpy as np
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        left, right,length=0,0,1
        #if si=sj, then dp[i,j]=dp[i+1,j-1]
        #dp[i,j]表示i-j是否是回文, 0为否，1为是
        number=len(s)
        if number==0:
            return ""
        dp=np.zeros((number,number))
        #一个字符一定是
        # for i in range(number):
        #     dp[i,i]=1

        #两个字符特殊考虑
        for i in range(number-1,-1,-1):
            for j in range(i+1,number):
                if s[i]==s[j] and j-i<2:
                    dp[i,j]=1
                if s[i]==s[j] and j-i>1:
                    dp[i,j]=dp[i+1,j-1]
                if dp[i,j]==1 and j-i+1>length:
                    left=i
                    right=j
                    length=j-i+1
        return s[left:right+1]
