class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.flag = True # setting flag to true
        self.prev = float('-inf') # creating the prev 
        self.inorder(root) # calling inorder function
        return self.flag # returning flag
        
    def inorder (self,root):
        #base condition
        if root == None:
            return
        
        self.inorder(root.left) # calling inorder of left
        
        if not (self.prev<root.val): # if root value is lesser than prev then return false
            self.flag = False
        self.prev = root.val # setting root value to prev
            
        self.inorder(root.right) # calling inorder of right