'''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
#k个入栈然后弹出，就变成了k个数翻转
#单链表什么的学的真的很烂。。。
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        cur=dummy
        while True:
            stack=[]
            count=0
            temp=head#head记录当前k个节点的头结点
            for i in range(k):
                if not temp:
                    break
                stack.append(temp)
                count+=1
                temp=temp.next#结束的时候，temp指的是下面k个节点的头节点
            if count<k:#剩下的不够k个节点了
                cur.next=head
                return dummy.next
            else:
                while stack:
                    cur.next=stack.pop(-1)
                    cur=cur.next
                head=temp
                cur.next=temp
        return dummy.next
                
