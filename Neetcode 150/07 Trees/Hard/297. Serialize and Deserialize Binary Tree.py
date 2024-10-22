# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        def dfs(node):
            if not node:
                result.append("None")
                return
            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        values = data.split(",")

        def dfs(i):
            if values[i] == "None":
                return None, i + 1
            node = TreeNode(int(values[i]))
            i += 1
            node.left, i = dfs(i)
            node.right, i = dfs(i)
            return node, i

        return dfs(0)[0]


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
