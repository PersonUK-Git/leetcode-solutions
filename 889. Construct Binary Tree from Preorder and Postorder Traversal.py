# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder, postorder):
        self.pre_idx = 0
        self.post_idx = 0
        
        def construct():
            if self.pre_idx >= len(preorder):
                return None
            
            curr = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1
            
            if curr.val != postorder[self.post_idx]:
                curr.left = construct()
            if curr.val != postorder[self.post_idx]:
                curr.right = construct()
            
            self.post_idx += 1
            return curr
        
        return construct()
    

'''
C++ SOLUTION

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int pre_idx = 0;
    int post_idx = 0;
public:
    TreeNode* constructFromPrePost(vector<int>& preorder, vector<int>& postorder) {
        TreeNode* curr = new TreeNode(preorder[pre_idx]);
        pre_idx++;

        if(curr->val != postorder[post_idx])
            curr->left = constructFromPrePost(preorder, postorder);
        if(curr->val != postorder[post_idx])
            curr->right = constructFromPrePost(preorder, postorder);

        post_idx++;
        return curr;
    }
};
'''


