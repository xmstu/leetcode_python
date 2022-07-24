# -*- coding:utf-8 -*-


class DisjointSet:
    """
    并查集

    find 将 x 和 x 的所有祖先连在根节点上, 因此树的高度只有2层
    unionSet 把两棵树进行合并, 只有当两个节点的最高层级的祖先不一致时, 才合并
    """

    def __init__(self, n) -> None:
        self.fa = [i for i in range(n)]
    
    def find(self, x):
        if x != self.fa[x]:
            self.fa[x] = self.find(self.fa[x])
        return self.fa[x]
    
    def unionSetV1(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.fa[x] = y
    
    def unionSet(self, x, y):
        self.fa[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)