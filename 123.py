n = int(input())             # 輸入要產生的數字數量
arr = []


def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""

    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
