import numpy as np
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1:
            return s
        list=[]
        
        for i in range(numRows):
            list.append("")
        postion=0#标记当前在哪个数组
        down=1#初始往下走
        for i in range(len(s)):
            if postion==0:
                down=1
            if postion==numRows-1:
                #该往上走了
                down=-1
            list[postion]+=s[i]
            i+=1
            postion+=down
        return "".join(list)
