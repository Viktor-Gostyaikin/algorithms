def eculid(m:float, n:float):
    if n > m:
        m, n = n, m
    changed = True
    while changed:
        m = m % n
        if m == 0:
            changed == False
            return n
        else:
            n = n % m
            if n == 0:
                changed == False
                return m