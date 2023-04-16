
def can_break_chocolate(n, m, k):
    if k == 1:
        return True
    if k > n * m:
        return False
    if k % n == 0 or k % m == 0:
        return True
    return False