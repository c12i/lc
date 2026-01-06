# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        arr = self.inorder(root, [])
        n = len(arr)
                      
        a = arr[0]      # default 1st wrong value from start
        for i in range(1, n):
            if arr[i].val < arr[i - 1].val:
                a = arr[i - 1]
                break
            
        b = arr[-1]   #default 1st wrong value from end
        for i in range(n - 2, -1, -1):
            if arr[i].val > arr[i + 1].val:
                b = arr[i + 1]
                break

        a.val, b.val = b.val, a.val   

    def inorder(self, root, arr):
        if not root:
            return 
        self.inorder(root.left, arr)
        arr.append(root)
        self.inorder(root.right, arr)
        return arr