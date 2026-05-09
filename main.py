def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    wrapper.cache = cache
    return wrapper

@memoize
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

@memoize
def grid_paths(m, n):
    """M x N to'rda yuqori-chapdan pastki-o'ngga necha yo'l bor?"""
    if m == 1 or n == 1:
        return 1
    return grid_paths(m-1, n) + grid_paths(m, n-1)

if __name__ == "__main__":
    print(factorial(10))        # 3628800
    print(factorial.cache)      # {(1,):1, (2,):2, ...}

    print(grid_paths(3, 3))     # 6
    print(grid_paths(10, 10))   # 48620
