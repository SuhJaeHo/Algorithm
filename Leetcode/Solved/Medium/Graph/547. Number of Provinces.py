from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        hm = {}
        parents = [i for i in range(len(isConnected))]

        def findParent(parents, x):
            if parents[x] != x:
                parents[x] = findParent(parents, parents[x])
            return parents[x]

        def unionParent(a, b):
            a = findParent(parents, a)
            b = findParent(parents, b)
            if a > b:
                parents[a] = b
            else:
                parents[b] = a

        for i in range(len(isConnected)):
            for k in range(len(isConnected)):
                if k == i or isConnected[i][k] != 1:
                    continue
                unionParent(i, k)

        for i in range(len(isConnected)):
            parents[i] = findParent(parents, i)

        for parent in parents:
            if not hm.get(parent):
                hm[parent] = 1

        return len(hm.keys())

# res = Solution().findCircleNum([[1,1,0],[1,1,0],[0,0,1]])
# res = Solution().findCircleNum([[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,1,0],[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,1,0,0,0,1,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,0,1,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,1,0,0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,0,0,0,0,0,0,1,0,0],[0,1,0,0,0,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])
res = Solution().findCircleNum([[1,0,0,0,1,0,1,0,0,0],[0,1,0,1,0,1,0,0,0,0],[0,0,1,0,0,1,0,0,0,0],[0,1,0,1,0,0,0,0,0,0],[1,0,0,0,1,0,0,0,1,0],[0,1,1,0,0,1,1,0,0,0],[1,0,0,0,0,1,1,0,1,0],[0,0,0,0,0,0,0,1,0,0],[0,0,0,0,1,0,1,0,1,0],[0,0,0,0,0,0,0,0,0,1]])
print("res", res)
