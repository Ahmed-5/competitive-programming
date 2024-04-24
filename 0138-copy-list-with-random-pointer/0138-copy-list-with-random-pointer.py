"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import _ctypes

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        l = []
        d = dict()
        d2 = dict()
        current = head
        prev_node = None
        
        while current:
            node = Node(current.val)
            rand = id(current.random)
            d[id(current)] = id(node)
            d2[id(node)] = id(current.random)
            l.append(node)
            if prev_node:
                prev_node.next = node
            current = current.next
            prev_node = node
            
            
        if len(l)>0:
            current = l[0]
            while current:
                id_ = id(current)
                cc = d2[id_]
                # print(id_, cc)
                if cc in d:
                    obj_id = d[cc]
                    # print(obj_id)
                    obj = _ctypes.PyObj_FromPtr(obj_id)
                    current.random = obj
                current = current.next
            return l[0]
        else:
            return None
        