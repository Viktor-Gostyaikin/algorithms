def eculid(m:int, n:int):
    if n > m:
        m, n = n, m
    r=m%n
    while r:
        m=n
        n=r
        r=m%n
    return n