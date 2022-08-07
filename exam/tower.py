# Python3
# 完成以下函数
# 参数：整数n，数组h
# 返回一个整数，表示答案
"""
你准备在一座山脚下盖房子定居。盖房子需要钢材, 幸运的是, 这里有排成一行的 n 座废弃的铁塔, 从左到右编号为 1~n,
其中第 i 座铁塔可以提供 h[i] 单位的钢材。
你需要把这些铁塔从左至右分成若干组, 每组内的铁塔编号必须是连续的, 并且从左至右每一组铁塔的能提供的钢材总量单调不减。
最后, 你可以用每组铁塔所提供的刚才构成一层上面小下面大的城堡。
负责处理钢材和建造城堡的公司对每一座铁塔收取 1 金币的费用, 但会给每一层城堡(即每一组钢材)优惠 1 金币。
这样一来, 你要交的费用就是 n - 组数 枚金币。因此你需要把这些铁塔分成尽量多组。

输入
第一行一个整数 n
第二行 n 个用空格隔开的整数, 第 i 个整数表示 h[i]

输出
输出一个整数, 表示最少付出的金币数, 即(n - 最多分成的组数)

数据范围
0 < n <= 5000, 0 < h[i] <= 2147483647
"""

def solve1(n, h):
    h = [0] + h
    dp = [0] * 5010
    g_len = [0] * 5010
    preSum = [0] * 5010

    for i in range(1, n+1):
        preSum[i] = preSum[i-1] + h[i]
    
    for i in range(1, n+1):
        for j in range(i):
            if preSum[i] - preSum[j] >= g_len[j]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    g_len[i] = preSum[i] - preSum[j]
                elif dp[j] + 1 == dp[i]:
                    g_len[i] = min(g_len[i], preSum[i] - preSum[j])

    return n - dp[n]


def solve(n, h):
    h = [0] + h
    dp = [0] * 5010
    g_len = [0] * 5010
    preSum = [0] * 5010

    for i in range(1, n+1):
        preSum[i] = preSum[i-1] + h[i]
    
    g_len[1] = preSum[1]
    dp[1] = 1
    for i in range(2, n+1):
        for j in range(i - 1, -1, -1):
            if preSum[i] - preSum[j] >= g_len[j]:
                dp[i] = dp[j] + 1
                g_len[i] = preSum[i] - preSum[j]
                break

    return n - dp[n]


if __name__ == "__main__":
    n = int(input())
    h = list(map(int, input().split()))
    print(solve(n, h))
