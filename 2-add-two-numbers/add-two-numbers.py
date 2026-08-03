class Solution:
    def addTwoNumbers(self, l1, l2):
        root = head = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            carry += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            head.next = ListNode(carry % 10)
            head = head.next
            carry //= 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return root.next
