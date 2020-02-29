class Solution(object):
    def isOK(self,queen_str,index):
        #列坐标不会重合,下标就是列坐标
        for i in range(len(queen_str)):
            if queen_str[i]==index:
                return True
            if queen_str[i]+i==index+len(queen_str):
                #主对角线
                return True
            if queen_str[i]-i==index-len(queen_str):
                #次对角线
                return True
        return False
    #queen_str中放置着皇后的行坐标
    def back(self,queen_str,res,n):
        if len(queen_str)==n:
            res.append(queen_str)
        else:
            for i in range(n):
                if self.isOK(queen_str,i) is False:
                    self.back(queen_str+[i],res,n)



    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res=[]
        self.back([],res,n)
        if len(res)==0:
            return []
        else:
            return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in res]
        


