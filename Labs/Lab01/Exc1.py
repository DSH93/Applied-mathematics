import numpy as np

# 1 ====================================================
A = np.array([[1, 1, 0], [1, -2, 1], [2, 1, 2]])
x = np.array([1, 2, -2])
x.shape = (3, 1)
B = np.array([[1, -1, 1], [-1, 0, 1], [3, 2, 1]])
y = np.array([2, -1, 3])
y.shape = (1, 3)
C = np.array([[1, -1j], [-1, 1j], [0, 2j]], dtype=complex)

# =========(A. a)============
print("Ax:\n", A @ x, "\n")
# print(A@x@C)
print("yAB:\n", y @ A @ B, "\n")
print("CC^tx:\n", C @ C.transpose() @ x, "\n\n")
print("yx:\n", y @ x, "\n\n")

# =========(A. b)================================
# ======First Method=============================
print("Sum First Method:", sum(sum(A @ B)), "\n")
# ======Second Method============================
sum2 = 0
result = 0
for i in A @ B:
    sum2 = sum2 + i
for i in sum2:
    result = i + result
print("Sum Second Method:", result, "\n")
