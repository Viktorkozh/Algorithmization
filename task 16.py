def f(n):
    if n == 1 or n == 2:
        return 3
    else:
        return 5 * f(n-1) - 4 * f(n-2)
ans = f(15)
print(ans)
