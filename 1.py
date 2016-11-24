def fib(n):
    try:
        n >= 1
    except:
        return None
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
print(fib(7))