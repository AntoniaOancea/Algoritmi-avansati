import math

def codificare(numar, a, b, p):
    l = int(math.log((b-a)*(10**p),2)) + 1
    interval_size = (b - a) / (2 ** l)
    index = int((numar - a) // interval_size)
    binar = format(index,f'0{l}b' )
    return binar

def decodificare(binar, a, b):
    p = len(binar)
    interval_size = (b - a) / (2 ** p)
    index = int(binar, 2)
    numar = a + index * interval_size
    return "{:.4f}".format(numar)

# Citirea datelor de intrare
a, b = map(float, input().split())
p = int(input())
m = int(input())

# Procesarea testelor
for _ in range(m):
    test_type = input().strip()
    if test_type == 'TO':
        numar = float(input())
        binar = codificare(numar, a, b, p)
        print(binar)
    elif test_type == 'FROM':
        binar = input().strip()
        numar = decodificare(binar, a, b)
        print(numar)
