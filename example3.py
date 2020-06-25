def get_zeros(n):
    i = 1
    c1 = 0
    c2 = 0
    while i < n:
        i += 1
        c1 += get_div_count(i, 2)
        c2 += get_div_count(i, 5)
    return min(c1, c2)

def get_div_count(f, n):
    r = 0
    while f % n == 0:
        r += 1
        f = f//n
    return r

print(get_zeros(5))
print(get_zeros(12))