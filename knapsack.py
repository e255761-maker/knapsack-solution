# 品物のデータ（1番から18番まで）
# (容量, 値段)
items = [
    (4, 6),   # 品物 1
    (8, 12),  # 品物 2
    (3, 4),   # 品物 3
    (5, 3),   # 品物 4
    (9, 7),   # 品物 5
    (2, 1),   # 品物 6
    (3, 3),   # 品物 7
    (1, 2),   # 品物 8
    (5, 7),   # 品物 9
    (2, 3),   # 品物 10
    (4, 4),   # 品物 11
    (2, 2),   # 品物 12
    (7, 10),  # 品物 13
    (10, 13), # 品物 14
    (3, 5),   # 品物 15
    (13, 16), # 品物 16
    (11, 14), # 品物 17
    (8, 9)    # 品物 18
]

KNAPSACK_CAPACITY = 45
n = len(items)

max_value = 0
best_combination = []

# 2^18 通りの組み合わせを総当り（全探索）で調べる
for i in range(1 << n):
    current_weight = 0
    current_value = 0
    current_items = []
    
    for j in range(n):
        # i番目の組み合わせにj番目の品物が含まれているかチェック
        if (i >> j) & 1:
            current_weight += items[j][0]
            current_value += items[j][1]
            current_items.append(j + 1) # 品物番号は1からスタート
            
    # 容量を超えておらず、これまでの最大価値を更新した場合
    if current_weight <= KNAPSACK_CAPACITY:
        if current_value > max_value:
            max_value = current_value
            best_combination = current_items

# 結果の表示
print(f"最大の総値段: {max_value}")
print(f"選んだ品物の組み合わせ: {best_combination}")