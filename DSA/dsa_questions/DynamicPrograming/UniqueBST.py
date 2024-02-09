from DSA.dsa_questions import TreeParsing

class Tree:
    def __init__(self, val: int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTree(self, n: int):
        if n <= 1: return 1
        return sum(self.generateTree(i-1)*self.generateTree(n-i) for i in range(1, n+1))

    def generateBTS(self, n):
        def bts(start, end):
            if start > end: return [None]
            all_tree = []
            for i in range(start, end+1):
                left_trees = bts(start, i-1)
                right_trees = bts(i+1, end)

                for left_tree in left_trees:
                    for right_tree in right_trees:
                        t = Tree(i, left_tree, right_tree)
                        all_tree.append(t)
            return all_tree
        return bts(1, n)

if __name__ == "__main__":
    s = Solution()
    print(s.generateTree(4))
    print(list(TreeParsing.preOrderParsing(i) for i in s.generateBTS(4)))