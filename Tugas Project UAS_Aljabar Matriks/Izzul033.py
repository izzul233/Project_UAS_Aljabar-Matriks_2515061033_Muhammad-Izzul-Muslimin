def tampilkan(A, label=""):
    if label:
        print(label)
    for baris in A:
        print(baris)
    print()

def tambah(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def kurang(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def kali(A, B):
    n = len(A)
    hasil = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                hasil[i][j] += A[i][k] * B[k][j]
    return hasil

def transpose(A):
    n = len(A)
    return [[A[j][i] for j in range(n)] for i in range(n)]