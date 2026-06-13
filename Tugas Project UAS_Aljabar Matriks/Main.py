import Izzul033 as izy

A = [
    [4, 2,  0],
    [4,  2, -1],
    [0, 5,  2]
]

B = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

izy.tampilkan(A, "Matriks A:")
izy.tampilkan(B, "Matriks B:")

izy.tampilkan(izy.tambah(A, B),     "A + B:")
izy.tampilkan(izy.kurang(A, B),     "A - B:")
izy.tampilkan(izy.kali(A, B),       "A x B:")
izy.tampilkan(izy.transpose(A),     "Transpose A:")