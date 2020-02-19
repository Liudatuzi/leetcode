# 将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。

# 比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：

# L   C   I   R
# E T O E S I I G
# E   D   H   N

# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/zigzag-conversion
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
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
