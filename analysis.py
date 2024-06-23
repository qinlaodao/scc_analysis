import numpy as np
import pandas as pd
from scipy.optimize import curve_fit

# 加载数据
data = pd.read_csv('scc_data.csv')

# 提取变量
water = data['水 (kg)'].values
sp = data['高效减水剂 (kg)'].values
powder = data['石粉 (kg)'].values
sand = data['砂 (kg)'].values
gravel = data['碎石 (kg)'].values
cement = data['水泥 (kg)'].values
fc = data['抗压强度 (MPa)'].values
slump = data['坍落度 (mm)'].values

# 变量矩阵
X = np.vstack([water, sp, powder, sand, gravel, cement]).T

# 定义回归模型 (7) 和 (8)
def fc_model(X, a1, a2, a3, a4, a5, a6, a7):
    return a7 * (X[:, 0] ** a1) * (X[:, 1] ** a2) * (X[:, 2] ** a3) * (X[:, 3] ** a4) * (X[:, 4] ** a5) * (X[:, 5] ** a6)

def slump_model(X, b1, b2, b3, b4, b5, b6, b7):
    return b7 * (X[:, 0] ** b1) * (X[:, 1] ** b2) * (X[:, 2] ** b3) * (X[:, 3] ** b4) * (X[:, 4] ** b5) * (X[:, 5] ** b6)

# 初始猜测值
initial_guess_a = [1, 1, 1, 1, 1, 1, 1]
initial_guess_b = [1, 1, 1, 1, 1, 1, 1]

# 使用非线性回归拟合
popt_a, _ = curve_fit(fc_model, X, fc, p0=initial_guess_a)
popt_b, _ = curve_fit(slump_model, X, slump, p0=initial_guess_b)

# 显示结果
print('抗压强度模型系数:')
print('a1, a2, a3, a4, a5, a6, a7')
print(popt_a)

print('坍落度模型系数:')
print('b1, b2, b3, b4, b5, b6, b7')
print(popt_b)
