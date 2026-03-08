# -*- coding: utf-8 | 编码声明，确保支持中文注释 -*-

# 1. 导入库 (Import)
import numpy as np  # 导入 NumPy 库，并简写为 np，这是工业界标准用法

def verify_matrix_multiplication():
    """
    函数功能：验证矩阵乘法的交换律并检查浮点数精度
    遵循 T3 代码规范：使用清晰的函数名和文档字符串
    """
    
    # 2. 创建矩阵 (Array Creation)
    # np.array() 将列表转换为 NumPy 数组（矩阵）
    # 这里定义两个 2x2 的方阵
    A = np.array([[1, 2], 
                  [3, 4]])
    
    B = np.array([[5, 6], 
                  [7, 8]])

    # 3. 矩阵乘法运算 (Matrix Multiplication)
    # 在 Python 3.5+ 中，@ 符号是专门用于矩阵乘法的运算符
    # 它不同于 A * B（那是对应位置元素相乘）
    C1 = A @ B  # 计算 A 乘以 B
    C2 = B @ A  # 计算 B 乘以 A

    # 4. 验证交换律 (Commutative Law Check)
    # 线性代数中，矩阵乘法通常不满足交换律 (A@B != B@A)
    is_equal = np.array_equal(C1, C2) # 比较两个数组是否完全相同
    
    print("--- 矩阵乘法验证 ---")
    print(f"矩阵 A:\n{A}")
    print(f"矩阵 B:\n{B}")
    print(f"A @ B 结果:\n{C1}")
    print(f"B @ A 结果:\n{C2}")
    print(f"两者是否相等? {is_equal}")

    # 5. 浮点数精度极限验证 (Precision Check)
    # 这是你之前跑出的那个误差 $5.55 \times 10^{-17}$ 的逻辑来源
    # 我们通过极其微小的数来测试系统精度
    val1 = 0.1 + 0.2
    val2 = 0.3
    diff = abs(val1 - val2)  # 计算两者的绝对差值
    
    print("\n--- 浮点数精度验证 ---")
    print(f"0.1 + 0.2 的结果: {val1}")
    print(f"误差值 (Difference): {diff:.2e}") # 使用科学计数法打印误差

# 执行函数
if __name__ == "__main__":
    verify_matrix_multiplication()