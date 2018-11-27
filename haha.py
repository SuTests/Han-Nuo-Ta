def hano(n, a, b, c):
    if n == 1:
        print(a, "-->", c)
        return None

    # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n - 1, a, c, b)
    print(a, "-->", c)
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hano(n - 1, b, a, c)


a = "A"
b = "B"
c = "C"

n = 4
hano(n, a, b, c)