# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


# Constant space
class Solution:
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        # Calculates how far a node is from the root
        def nodeDepth(node: "Node") -> int:
            count = 0
            while node.parent:
                node = node.parent
                count += 1
            return count

        p_depth = nodeDepth(p)
        q_depth = nodeDepth(q)

        # Make the lower node swim to the same height as the higher node
        while p_depth > q_depth:
            p = p.parent
            p_depth -= 1
        while q_depth > p_depth:
            q = q.parent
            q_depth -= 1

        # p and q are on the same level, simply swim up one by one until they match
        while p != q:
            p = p.parent
            q = q.parent

        return p  # p now equals q, they found the same parent


# Use set
class Solution:  # noqa F811
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        visited = set()
        while p or q:
            visited.add(p)
            visited.add(q)

            if p and q and p.parent == q.parent:
                return p.parent
            if p and p.parent in visited:
                return p.parent
            if q and q.parent in visited:
                return q.parent
            if p:
                p = p.parent
            if q:
                q = q.parent

        return None


# Constant space but confusing
class Solution:  # noqa F811
    def lowestCommonAncestor(self, p: "Node", q: "Node") -> "Node":
        pointer_p = p
        pointer_q = q
        while pointer_p != pointer_q:
            if pointer_p.parent:
                pointer_p = pointer_p.parent
            else:
                pointer_p = q
            if pointer_q.parent:
                pointer_q = pointer_q.parent
            else:
                pointer_q = p
        return pointer_p
