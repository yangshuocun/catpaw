"""
LeetCode Hot100 第25题：K 个一组翻转链表
题目描述：
    给你链表的头节点 head，每 k 个节点一组进行翻转，请你返回修改后的链表。
    k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，
    那么请将最后剩余的节点保持原有顺序。
    你不能只是单纯地改变节点内部的值，而是需要实际进行节点交换。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 先检查剩余节点是否够 k 个，不够则不翻转
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        if count < k:
            return head

        # 翻转前 k 个节点
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # head 现在是翻转后的尾节点，递归处理剩余部分
        head.next = self.reverseKGroup(curr, k)
        return prev

    def reverseKGroup_iterative(self, head: ListNode, k: int) -> ListNode:
        """迭代法：K 个一组翻转链表"""
        dummy = ListNode(0, head)
        prev_group = dummy

        while True:
            # 检查剩余节点是否够 k 个
            curr = prev_group.next
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            if count < k:
                break

            # 翻转当前组的 k 个节点
            group_start = prev_group.next
            prev = None
            curr = group_start
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # 连接前一组的尾和当前组的头
            prev_group.next = prev
            group_start.next = curr  # 连接当前组的尾和下一组的头
            prev_group = group_start  # 移动到当前组的尾

        return dummy.next


# ========== 辅助函数 ==========

def list_to_linkedlist(lst):
    """将 Python 列表转换为链表"""
    dummy = ListNode(0)
    curr = dummy
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(node):
    """将链表转换为 Python 列表"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


# ========== 测试样例 ==========

def test():
    solution = Solution()

    # 测试样例 1：常规情况，恰好整除
    # 输入: head = [1,2,3,4,5], k = 2
    # 输出: [2,1,4,3,5]
    head1 = list_to_linkedlist([1, 2, 3, 4, 5])
    result1 = linkedlist_to_list(solution.reverseKGroup(head1, 2))
    print(f"测试1: 输入 [1,2,3,4,5], k=2")
    print(f"       输出: {result1}")
    assert result1 == [2, 1, 4, 3, 5], f"期望 [2,1,4,3,5], 得到 {result1}"
    print("       ✅ 通过\n")

    # 测试样例 2：有余数，最后一组不翻转
    # 输入: head = [1,2,3,4,5], k = 3
    # 输出: [3,2,1,4,5]
    head2 = list_to_linkedlist([1, 2, 3, 4, 5])
    result2 = linkedlist_to_list(solution.reverseKGroup(head2, 3))
    print(f"测试2: 输入 [1,2,3,4,5], k=3")
    print(f"       输出: {result2}")
    assert result2 == [3, 2, 1, 4, 5], f"期望 [3,2,1,4,5], 得到 {result2}"
    print("       ✅ 通过\n")

    # 测试样例 3：k=1，相当于不翻转
    # 输入: head = [1,2,3], k = 1
    # 输出: [1,2,3]
    head3 = list_to_linkedlist([1, 2, 3])
    result3 = linkedlist_to_list(solution.reverseKGroup(head3, 1))
    print(f"测试3: 输入 [1,2,3], k=1")
    print(f"       输出: {result3}")
    assert result3 == [1, 2, 3], f"期望 [1,2,3], 得到 {result3}"
    print("       ✅ 通过\n")

    # 测试样例 4：链表长度等于 k，整体翻转
    # 输入: head = [1,2,3,4], k = 4
    # 输出: [4,3,2,1]
    head4 = list_to_linkedlist([1, 2, 3, 4])
    result4 = linkedlist_to_list(solution.reverseKGroup(head4, 4))
    print(f"测试4: 输入 [1,2,3,4], k=4")
    print(f"       输出: {result4}")
    assert result4 == [4, 3, 2, 1], f"期望 [4,3,2,1], 得到 {result4}"
    print("       ✅ 通过\n")

    # 测试样例 5：单节点链表
    # 输入: head = [1], k = 1
    # 输出: [1]
    head5 = list_to_linkedlist([1])
    result5 = linkedlist_to_list(solution.reverseKGroup(head5, 1))
    print(f"测试5: 输入 [1], k=1")
    print(f"       输出: {result5}")
    assert result5 == [1], f"期望 [1], 得到 {result5}"
    print("       ✅ 通过\n")

    print("🎉 所有测试样例通过！")

    # ===== 迭代法测试 =====
    print("\n===== 迭代法测试 =====\n")

    # 迭代法测试 1
    head6 = list_to_linkedlist([1, 2, 3, 4, 5])
    result6 = linkedlist_to_list(solution.reverseKGroup_iterative(head6, 2))
    print(f"迭代测试1: 输入 [1,2,3,4,5], k=2")
    print(f"          输出: {result6}")
    assert result6 == [2, 1, 4, 3, 5], f"期望 [2,1,4,3,5], 得到 {result6}"
    print("          ✅ 通过\n")

    # 迭代法测试 2
    head7 = list_to_linkedlist([1, 2, 3, 4, 5])
    result7 = linkedlist_to_list(solution.reverseKGroup_iterative(head7, 3))
    print(f"迭代测试2: 输入 [1,2,3,4,5], k=3")
    print(f"          输出: {result7}")
    assert result7 == [3, 2, 1, 4, 5], f"期望 [3,2,1,4,5], 得到 {result7}"
    print("          ✅ 通过\n")

    print("🎉 迭代法测试全部通过！")


if __name__ == "__main__":
    test()
