# Python3
# 完成以下函数
# 参数：整数n，整数m，二维数组gophers，二维数组plants
# 返回一个包含两个整数的list，表示答案
# example:
# gophers = [[1, 2], [2, 2], [1, 2]]
# plants = [[1, 2]]

"""
你有一片菜地, 种着 M 株植物, 每株植物位置可以用一个二维坐标来表示。
你的地理闯进了一只超级地鼠, 这只地鼠使出了瞬移绝技在地里到处乱窜。
幸运的是, 你统计出了在之前一段时间内, 地鼠在乱窜过程中出现过的 N 个位置 (N个二维坐标, 位置可能重复)。你希望统计一下地鼠在哪里出现的次数最多,
然后拿起锤子向那个地方砸去。
但前提是, 你不能砸到植物所在位置。

注意:
如果答案不唯一, 输出其中横纵坐标之和 (x+y) 最小的; 若还不唯一, 输出其中横坐标 (x) 最小的

数据范围:
1 <= N, M <= 1000, 坐标范围在 0~10,000,000 之间
"""

from collections import defaultdict
from heapq import heappush


def solve(n, m, gophers, plants):
    plant_set = set()
    for plant in plants:
        plant_set.add(tuple(plant))
    
    go_map = defaultdict(int)
    for gopher in gophers:
        if tuple(gopher) in plant_set:
            continue
        go_map[tuple(gopher)] += 1
    
    ans_list = []
    max_cnt = max(go_map.values())
    for gopher, cnt in go_map.items():
        if cnt == max_cnt:
            x, y = gopher
            heappush(ans_list, [x + y, x, gopher])

    
    ans = ans_list[0][2]

    return ans


if __name__ == "__main__":
    first_line = list(map(int, input().split()))
    n = first_line[0]
    m = first_line[1]
    gophers = []
    plants = []
    for i in range(n):
        gophers.append(list(map(int, input().split())))
    for i in range(m):
        plants.append(list(map(int, input().split())))
    ans = solve(n, m, gophers, plants)
    print(ans[0], ans[1])