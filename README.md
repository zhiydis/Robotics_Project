# Robotics Project: Matrix & Precision Check

这是我的机器人工程实践起始仓库，用于验证核心算法逻辑。

## 🛠️ 技术栈
- **Language**: Python 3.10
- **Library**: NumPy (矩阵运算核心)
- **Environment**: PyCharm + Git

## 🧪 验证任务
- [x] **T1: 矩阵非交换性验证**：验证 $A \times B \neq B \times A$。
- [x] **T2: 浮点数精度校验**：记录 IEEE 754 误差（$5.55 \times 10^{-17}$）。
- [x] **T4: GitHub SSH 自动化联调**。
- ---

## 📐 Math_Rules: 多变量求导准则 (C9-T1)

为了支撑 **Paper 1 (SAE 降维)** 的梯度推导，在此记录核心数学逻辑：

### 1. 偏导数准则 (Partial Rule)
求对单个变量的变化率时，冻结其他所有变量：
$$\frac{\partial f}{\partial x} = \lim_{\Delta x \to 0} \frac{f(x+\Delta x, y) - f(x, y)}{\Delta x}$$

### 2. 链式法则 (Chain Rule)
处理误差 $E$ 通过中间变量 $u$ 传导至底层参数 $\theta$ 的逻辑：
$$\frac{dE}{d\theta} = \frac{\partial E}{\partial u} \cdot \frac{du}{d\theta}$$

### 3. 全微分 (Total Differential)
系统整体变化量是各维度偏导贡献的线性累加：
$$df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$$
## 📚 现代控制理论专题
* [点击阅读：现代控制理论核心架构与工程落地全手册](./modern_control_theory.md)