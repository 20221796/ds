#노드 클래스
class BidirectNode:
    def __init__(self, x:dict , prevNode:'BidirectNode', nextNode:'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode