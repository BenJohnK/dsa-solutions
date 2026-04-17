
# Node Class:
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None


class Solution:
    def dfs(self, root, result):
        if not root:
            return
        result.append(root.data)
        self.dfs(root.left, result)
        self.dfs(root.right, result)
    
    def preOrder(self, root):
        # code here
        result = []
        self.dfs(root, result)
        return result


# Now when calling the preOrder method in Solution using an object, we can obtain the list of values in preorder, instead of simply printing them.