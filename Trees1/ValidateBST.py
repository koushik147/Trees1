#Time_Complexity: O(n) 
#Space_Complexity : O(n)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.result = [] # creating the resultant array
        self.inorder(root) # calling inorder function
        
        for i in range(1,len(self.result)):
            if self.result[i-1]< self.result[i]: # if previous element is lower than present element
                pass
            else:
                return False
        return True
    
    def inorder (self,root):
        #base condition
        if root == None:
            return
        
        self.inorder(root.left) # calling inorder of left
        
        self.result.append(root.val) # appending root.val in result 
        
        self.inorder(root.right) # calling inorder of right
