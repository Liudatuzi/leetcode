#纪念下新学到的数据结构，单调栈
#算法课上讲过，当时觉得这是个什么玩意，谁想出来的，，还背下来了代码虽然考试没想起来。。。现在觉得好厉害
#今天好基友拿到了usc，前天ucla，我还是啥都没有，现在只剩我一个在等offer啦，哎不哭不哭，人生这么多条路呢，但还是为自己泯然众人感到很难过
#单调栈(此处举例递增),这个栈里头的元素始终是递增的，当栈空则入栈元素，栈尾元素比当前元素大则不停地弹出，这样就保证刚弹出的那个元素
#第一个比它小的就是目前栈尾，然后右边第一个比它小的就是当前遍历到的这个
'''
84.给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
'''
#头放个0为了保证里面只剩一个元素的时候不用特殊处理，尾部放个0因为这样就能把所有元素弹出来
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #用单调递增栈
        stack=[]
        heights=[0]+heights+[0]
        maxArea=0
        for i, val in enumerate(heights):
            if not stack:
                stack.append(i)
            elif stack and heights[stack[-1]]<val:
                stack.append(i)
            else:
                while heights[stack[-1]]>val:
                    temp=stack.pop()
                    maxArea=max(maxArea,heights[temp]*(i-stack[-1]-1))
                stack.append(i)
        return maxArea
