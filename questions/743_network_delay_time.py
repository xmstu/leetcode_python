# -*- coding:utf-8 -*-
from typing import List
from heapq import heappush, heappop


class Solution:

    """
    有 n 个网络节点，标记为 1 到 n。
    给你一个列表 times，表示信号经过 有向 边的传递时间。 times[i] = (ui, vi, wi)，其中 ui 是源节点, vi 是目标节点， wi 是一个信号从源节点传递到目标节点的时间。
    现在，从某个节点 K 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 -1 。

    使用 Bellman-Ford 算法求解
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [1e9] * (n+1)
        dist[k] = 0
        # round 是更新轮数, bellman-ford 算法最多需要 n - 1 轮就可以单源最短路
        for round in range(1, n):
            # flag 代表是否有更新 dist 数组
            flag = False
            for edge in times:
                x = edge[0]
                y = edge[1]
                z = edge[2]
                if dist[x] + z < dist[y]:
                    dist[y] = dist[x] + z
                    flag = True
            # 当前这轮没有更新 dist 数组, 提前结束循环
            if not flag:
                break
        
        ans = max(dist[1:])
        return ans if ans != 1e9 else -1


class Solution2:

    """
    Dijkstra 算法是基于贪心思想的, 只适用于所有边的长度都是非负数的图
    1. 初始化 dist[1] = 0, 其余节点的 dist 值为正无穷大
    2. 找出一个未被标记的, dist[x] 最小的节点 x, 然后标记节点 x
    3. 扫描节点 x 的所有出边 (x,y,z), 若 dist[y] > dist[x] + z, 则使用 dist[x] + z 更新 dist[y]
    4. 重复上述 2-3 步骤

    时间复杂度 O(n ^ 2)

    优化，用二叉堆维护最小 dist 值可以做到 O(M * logN) 时间复杂度
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 出边数组
        ver = [[] for _ in range(n+1)]
        # 记录出边的边权
        edge = [[] for _ in range(n+1)]
        for t in times:
            x = t[0]
            y = t[1]
            z = t[2]
            ver[x].append(y)
            edge[x].append(z)
        dist = [1e9] * (n+1)
        dist[k] = 0
        expand = [False] * (n+1)
        for round in range(1, n+1):
            temp, x = 1e9, 0
            for i in range(1, n+1):
                if not expand[i] and dist[i] < temp:
                    temp = dist[i]
                    x = i
            expand[x] = True
            for i in range(0, len(ver[x])):
                y = ver[x][i]
                z = edge[x][i]
                if dist[y] > dist[x] + z:
                    dist[y] = dist[x] + z
        ans = max(dist[1:])
        return ans if ans != 1e9 else -1


class Solution3:

    """
    Dijkstra 算法是基于贪心思想的, 只适用于所有边的长度都是非负数的图
    1. 初始化 dist[1] = 0, 其余节点的 dist 值为正无穷大
    2. 找出一个未被标记的, dist[x] 最小的节点 x, 然后标记节点 x
    3. 扫描节点 x 的所有出边 (x,y,z), 若 dist[y] > dist[x] + z, 则使用 dist[x] + z 更新 dist[y]
    4. 重复上述 2-3 步骤

    时间复杂度 O(n ^ 2)

    优化，用二叉堆维护最小 dist 值可以做到 O(M * logN) 时间复杂度
    """
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 出边数组
        ver = [[] for _ in range(n+1)]
        # 记录出边的边权
        edge = [[] for _ in range(n+1)]
        for t in times:
            x = t[0]
            y = t[1]
            z = t[2]
            ver[x].append(y)
            edge[x].append(z)
        dist = [1e9] * (n+1)
        dist[k] = 0
        expand = [False] * (n+1)
        # 放一个二元组, 第一位是边权, 第二位是节点编号
        q = [(0, k)]
        while q:
            x = q[0][1]
            heappop(q)
            if expand[x]:
                continue
            expand[x] = True
            for i in range(0, len(ver[x])):
                y = ver[x][i]
                z = edge[x][i]
                if dist[y] > dist[x] + z:
                    dist[y] = dist[x] + z
                    heappush(q, (dist[y], y))
        ans = max(dist[1:])
        return ans if ans != 1e9 else -1



class TestNetworkDelayTime:

    """
    pytest -s 743_network_delay_time.py::TestNetworkDelayTime
    """

    def test(self):
        solution = Solution3()

        times = [[2,1,1],[2,3,1],[3,4,1]]; n = 4; k = 2
        assert 2 == solution.networkDelayTime(times, n, k)

        times = [[1,2,1]]; n = 2; k = 1
        assert 1 == solution.networkDelayTime(times, n, k)

        times = [[1,2,1]]; n = 2; k = 2
        assert -1 == solution.networkDelayTime(times, n, k)
