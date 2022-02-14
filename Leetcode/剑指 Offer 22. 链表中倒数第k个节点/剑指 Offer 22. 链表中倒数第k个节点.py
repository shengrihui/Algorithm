# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 21:27:07 2021

@author: 11200
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        node, n = head, 0
        while node:
            node = node.next
            n += 1

        node = head
        for _ in range(n - k):
            node = node.next

        return node

    # 作者：LeetCode-Solution


# 链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/lian-biao-zhong-dao-shu-di-kge-jie-dian-1pz9l/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""
剑指 Offer 22. 链表中倒数第k个节点
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。

例如，一个链表有 6 个节点，从头节点开始，它们的值依次是 1、2、3、4、5、6。这个链表的倒数第 3 个节点是值为 4 的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.
"""
