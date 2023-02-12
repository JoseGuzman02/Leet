class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def display(self):
        temp = self.head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next
        print()

    def push(self, value):
        self.count += 1
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node

    def append(self, value):
        self.count += 1
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def addArr(self, arr):
        for num in arr:
            self.push(num)

    def checkList(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            if temp.val > 9:
                if temp.next is None:
                    temp.val = temp.val - 10
                    self.append(1)
                else:
                    temp.val = temp.val - 10
                    next_node = temp.next
                    next_node.val = next_node.val + 1
            temp = temp.next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        list1 = LinkedList()
        list2 = LinkedList()
        list1.addArr(l1)
        list2.addArr(l2)

        min_num = min(list1.count, list2.count)
        temp1 = list1.head
        temp2 = list2.head
        for i in range(min_num):
            temp1.val += temp2.val
            temp1 = temp1.next
            temp2 = temp2.next

        if min_num == list1.count:
            while(temp2):
                list1.append(temp2.val)
                temp2 = temp2.next
            list1.checkList()
            return list1


arr1 = [3,0]
arr2 = [1,9]

sol = Solution()
sum_list = sol.addTwoNumbers(arr1, arr2)
sum_list.display()