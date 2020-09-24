def sumatoria_cubica(n):
    r = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            for k in range(j, i + j + 1):
                r += 1     
    return(r)
    raise NotImplementedError()
    

def sumatoria_constante(n):
    i = n*(n+1)
    j = (n*(n+1)/3)
    res = int(i*j)
    return res
    raise NotImplementedError()
