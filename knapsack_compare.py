import time

# 品物のデータ（容量, 値段）
items = [
    (4, 6), (8, 12), (3, 4), (5, 3), (9, 7), (2, 1),
    (3, 3), (1, 2), (5, 7), (2, 3), (4, 4), (2, 2),
    (7, 10), (10, 13), (3, 5), (13, 16), (11, 14), (8, 9)
]
KNAPSACK_CAPACITY = 45
n = len(items)

# ==========================================
# 1. 総当り法（前回の方法）
# ==========================================
def solve_brute_force():
    max_value = 0
    best_combination = []
    for i in range(1 << n):
        current_weight = 0
        current_value = 0
        current_items = []
        for j in range(n):
            if (i >> j) & 1:
                current_weight += items[j][0]
                current_value += items[j][1]
                current_items.append(j + 1)
        if current_weight <= KNAPSACK_CAPACITY:
            if current_value > max_value:
                max_value = current_value
                best_combination = current_items
    return max_value, best_combination

# ==========================================
# 2. 動的計画法（DP）（今回の工夫した方法）
# ==========================================
def solve_dynamic_programming():
    # DPテーブルの初期化
    dp = [[0] * (KNAPSACK_CAPACITY + 1) for _ in range(n + 1)]
    
    # DPテーブルの更新
    for i in range(1, n + 1):
        w, v = items[i - 1]
        for j in range(KNAPSACK_CAPACITY + 1):
            if j >= w:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
            else:
                dp[i][j] = dp[i - 1][j]
                
    # 選んだ品物の復元
    max_value = dp[n][KNAPSACK_CAPACITY]
    best_combination = []
    w = KNAPSACK_CAPACITY
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            best_combination.append(i)
            w -= items[i - 1][0]
    best_combination.reverse()
    
    return max_value, best_combination

# ==========================================
# 時間測定と実行
# ==========================================
print("--- 総当り法を実行中... ---")
start_time = time.time()
bf_val, bf_items = solve_brute_force()
bf_time = time.time() - start_time
print(f"総当り法の結果: 値段={bf_val}, 品物={bf_items}")
print(f"処理時間: {bf_time:.6f} 秒\n")

print("--- 動的計画法（DP）を実行中... ---")
start_time = time.time()
dp_val, dp_items = solve_dynamic_programming()
dp_time = time.time() - start_time
print(f"動的計画法の結果: 値段={dp_val}, 品物={dp_items}")
print(f"処理時間: {dp_time:.6f} 秒\n")

print(f"【結果】動的計画法は総当り法より 約 {bf_time / dp_time:.1f} 倍速くなりました！")