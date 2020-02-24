'''
给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#用的回溯法，时间比较慢，感觉用动态规划比较迅速
class Solution(object):
    def check(self,current):
        temp1=[]
        for i in range(len(current)):
            if current[i]==')' and temp1[-1]=='(':
                temp1.pop(-1)
            else:
                temp1.append(current[i])

        if len(temp1)==0:
            return True
        return False

    def generate(self,current,n,res):

        if len(current)==2*n and self.check(current)==True:
            res.append(current)
        elif len(current)<2*n:

            if self.check(current):
                self.generate(current+'(',n,res)
            else:
                self.generate(current+')',n,res)
                self.generate(current+'(',n,res)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        res=[]
        self.generate("",n,res)
        return res
Solution().generateParenthesis(3)
