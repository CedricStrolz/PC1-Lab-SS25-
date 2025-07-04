import numpy as np
from scipy.integrate import simpson

V_kp_A12 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04, 36.96, 35, 33.4, 32.36]) * 1e-6  # m³
p_kp_A12 = np.array([1155, 1195, 1197, 1159, 1105, 1037, 973, 918, 874, 839, 816, 808, 815, 841, 890, 958, 1030, 1064]) * 100  # Pa
Th_1 = 229.5 + 273.15
Tk_1 = 73.7 + 273.15
V_min_1 = V_kp_A12.min()
V_max_1 = V_kp_A12.max()
n_1_max = (V_max_1 * p_kp_A12.max()) / (((Th_1 + Tk_1) / 2) * 8.3145)
n_1_min = (V_min_1 * p_kp_A12.min()) / (((Th_1 + Tk_1) / 2) * 8.3145)
n_1 = (n_1_max + n_1_min) / 2

V_kp_A51 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04, 36.96, 35, 33.4, 32.36]) * 1e-6
p_kp_A51 = np.array([1161, 1205, 1209, 1174, 1119, 1049, 983, 925, 878, 841, 817, 806, 813, 839, 888, 955, 1029, 1097]) * 100
Th_2 = 229.5 + 273.15
Tk_2 = 73.7 + 273.15
V_min_2 = V_kp_A51.min()
V_max_2 = V_kp_A51.max()
n_2_max = (V_max_2 * p_kp_A51.max()) / (((Th_2 + Tk_2) / 2) * 8.3145)
n_2_min = (V_min_2 * p_kp_A51.min()) / (((Th_2 + Tk_2) / 2) * 8.3145)
n_2 = (n_2_max + n_2_min) / 2

V_kp_A125 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04, 36.96, 35, 33.4, 32.36]) * 1e-6
p_kp_A125 = np.array([1143, 1192, 1202, 1171, 1115, 1044, 973, 913, 861, 819, 792, 780, 786, 809, 857, 923, 998, 1069]) * 100
Th_3 = 229.5 + 273.15
Tk_3 = 73.7 + 273.15
V_min_3 = V_kp_A125.min()
V_max_3 = V_kp_A125.max()
n_3_max = (V_max_3 * p_kp_A125.max()) / (((Th_3 + Tk_3) / 2) * 8.3145)
n_3_min = (V_min_3 * p_kp_A125.min()) / (((Th_3 + Tk_3) / 2) * 8.3145)
n_3 = (n_3_max + n_3_min) / 2

def berechne_wirkungsgrad(V, p, V_min, V_max, T_H, T_K, n):
    W_real = simpson(p, V)
    W_ideal = n * 8.3145 * (T_H - T_K) * np.log(V_max / V_min)
    eta_ideal = 1 - (T_K / T_H)
    Q_in_ideal = n * 8.3145 * T_H * np.log(V_max / V_min)
    eta_real = W_real / Q_in_ideal
    return W_real, W_ideal, eta_real, eta_ideal

results = []
for data in [
    (V_kp_A12, p_kp_A12, V_min_1, V_max_1, Th_1, Tk_1, n_1),
    (V_kp_A51, p_kp_A51, V_min_2, V_max_2, Th_2, Tk_2, n_2),
    (V_kp_A125, p_kp_A125, V_min_3, V_max_3, Th_3, Tk_3, n_3),
]:
    results.append(berechne_wirkungsgrad(*data))

print(results)
