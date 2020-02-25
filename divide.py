'''
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#不断地把除数×2直到大于被除数，然后递归一波儿
#很焦虑，ucsd开始发offer了，貌似offer就看学积分，没法子三年学积分就是很难看，要真看学积分那就直说啊搞什么幺蛾子，我连申都不申，要cv要ps要推荐信到头来就看学积分。还我两万块申请费啊如果要开始就想拒绝老子
class Solution(object):
    def div(self,a,b):#a/b
        if  (a<b):
            return 0
        else:
            count=1
            newb=b
            while(a>=newb+newb):
                count+=count
                newb+=newb
            return count+self.div(a-newb,b)


    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor==0:
            return 0
        if divisor==1:
            return dividend
        if divisor==-1:
            if dividend>-2**31:
                return -dividend
            else:
                return 2**31-1
        sign=(dividend>0)^(divisor>0)
        res=self.div(abs(dividend),abs(divisor))
        if sign:
            return -res
        else:
            return res

            

