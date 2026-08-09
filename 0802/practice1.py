# ── 基礎練習：變數、函式、條件、迴圈 ──────────────────────────────────

# 1. 問候函式
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to Python."


# 2. 判斷奇偶
def classify_number(n: int) -> str:
    if n % 2 == 0:
        return f"{n} 是偶數"
    else:
        return f"{n} 是奇數"


# 3. 計算 1 到 n 的總和
def sum_to(n: int) -> int:
    return sum(range(1, n + 1))


# 4. 用 list comprehension 取得 1~20 中的偶數
even_numbers = [x for x in range(1, 21) if x % 2 == 0]


# ── 主程式 ──────────────────────────────────────────────────────────

if __name__ == "__main__":
    # 問候
    print(greet("Python"))

    # 奇偶判斷
    for num in [3, 8, 15, 42]:
        print(classify_number(num))

    # 總和
    n = 100
    print(f"\n1 到 {n} 的總和 = {sum_to(n)}")

    # 偶數列表
    print(f"\n1~20 的偶數：{even_numbers}")
