import numpy as np
import scipy.linalg as la

# 1. 直接输入截图 1000047119 里的黑板例题矩阵
A = np.array([[-1, -4, -2],
              [ 0,  6,  1],
              [ 1,  7, -1]])

B = np.array([[2],
              [0],
              [1]])

n = A.shape[0] # 获取系统阶数，这里 n = 3

# 2. 纯代码手工拼装卡尔曼能控性矩阵 M = [B, AB, A^2B]
# （用 python 的矩阵乘法符号 @）
M = np.hstack([B, A @ B, A @ A @ B])

# 3. 算出 M 矩阵的秩 (Rank)
rank_M = np.linalg.matrix_rank(M)

# 4. 一锤定音的架构师判定
print(f"卡尔曼能控性矩阵 M:\n{M}")
print(f"M 矩阵的秩为: {rank_M}")

if rank_M == n:
    print("【判定结果】：系统完全能控！(与黑板例题答案一致)")
else:
    print("【判定结果】：存在无法控制的死角！")