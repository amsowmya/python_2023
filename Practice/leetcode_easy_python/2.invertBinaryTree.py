# Recursive approach
class Solution:
    def invertTree(self, root):
        def reverseNodes(node):
            if node == None:
                return
            reverseNodes(node.left)
            reverseNodes(node.right)

            hold = node.left
            node.left = node.right
            node.right = hold

        reverseNodes(root)
        return root

if __name__ == "__main__":
    sol = Solution()
    root = [4,2,7,1,3,6,9]
    sol.invertTree(root)

# Iterative approach
class Solution1:
    def invertTree(self, root):
        st = [root]
        while len(st) > 0:
            node = st.pop()
            if node != None:
                hold = node.left
                node.left = node.right
                node.right=hold

                st.append(node.left)
                st.append(node.right)

        return root
