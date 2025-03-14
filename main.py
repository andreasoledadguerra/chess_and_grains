def square(n):
    if not(0 <= n <= 64):
        raise ValueError("square must be between 0 and 64")
    return pow(2,n) 