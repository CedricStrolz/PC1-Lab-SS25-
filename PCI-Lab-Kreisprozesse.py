import numpy as np
from matplotlib import pyplot as plt
from numpy.ma.extras import average

V_kp_A12 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04, 36.96, 35, 33.4, 32.36, 32])
p_kp_A12 = np.array([1155, 1195, 1197, 1159, 1105, 1037, 973, 918, 874, 839, 816, 808, 815, 841, 890, 958, 1030, 1064, 1155])
Th_kp_A12 = 229.5 + 273.15
Tk_kp_A12 = 73.7 + 273.15

n_1_max = (V_kp_A12.max() * p_kp_A12.max()*0.0001) / (((Th_kp_A12 + Tk_kp_A12) / 2) * 8.3145)
n_1_min = (V_kp_A12.min() * p_kp_A12.min()*0.0001) / (((Th_kp_A12 + Tk_kp_A12) / 2) * 8.3145)
n_1 = (n_1_max + n_1_min) / 2

V_min_1 = V_kp_A12.min() * 1e-6
V_max_1 = V_kp_A12.max() * 1e-6
V_exp_1 = np.linspace(V_min_1, V_max_1, 100)
V_comp_1 = np.linspace(V_max_1, V_min_1, 100)
p_exp_1 = (n_1 * 8.3145 * Th_kp_A12) / V_exp_1
T_isochore_cool_1 = np.linspace(Th_kp_A12, Tk_kp_A12, 50)
p_isochore_cool_1 = n_1 * 8.3145 * T_isochore_cool_1 / V_max_1
p_comp_1 = (n_1 * 8.3145 * Tk_kp_A12) / V_comp_1
T_isochore_heat_1 = np.linspace(Tk_kp_A12, Th_kp_A12, 50)
p_isochore_heat_1 = n_1 * 8.3145 * T_isochore_heat_1 / V_min_1
V_exp_1_plot = V_exp_1 * 1e6
V_comp_1_plot = V_comp_1 * 1e6
p_exp_1_plot = p_exp_1 / 100
p_comp_1_plot = p_comp_1 / 100
p_isochore_cool_1_plot = p_isochore_cool_1 / 100
p_isochore_heat_1_plot = p_isochore_heat_1 / 100
V_max_1_plot = V_max_1 * 1e6
V_min_1_plot = V_min_1 * 1e6

V_kp_A51 =np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36, 32])
p_kp_A51 =np.array([1161, 1205, 1209, 1174, 1119, 1049, 983, 925, 878, 841, 817, 806, 813, 839, 888, 955, 1029, 1097, 1161])
Th_kp_A51 = 229.5 + 273.15
Tk_kp_A51 = 73.7 + 273.15

n_2_max = (V_kp_A51.max() * p_kp_A51.max()*0.0001) / (((Th_kp_A51 + Tk_kp_A51) / 2) * 8.3145)
n_2_min = (V_kp_A51.min() * p_kp_A51.min()*0.0001) / (((Th_kp_A51 + Tk_kp_A51) / 2) * 8.3145)
n_2 = (n_2_max + n_2_min) / 2

V_min_2 = V_kp_A51.min() * 1e-6
V_max_2 = V_kp_A51.max() * 1e-6
V_exp_2 = np.linspace(V_min_2, V_max_2, 100)
V_comp_2 = np.linspace(V_max_2, V_min_2, 100)
p_exp_2 = (n_2 * 8.3145 * Th_kp_A51) / V_exp_2
T_isochore_cool_2 = np.linspace(Th_kp_A51, Tk_kp_A51, 50)
p_isochore_cool_2 = n_2 * 8.3145 * T_isochore_cool_2 / V_max_2
p_comp_2 = (n_2 * 8.3145 * Tk_kp_A51) / V_comp_2
T_isochore_heat_2 = np.linspace(Tk_kp_A51, Th_kp_A51, 50)
p_isochore_heat_2 = n_2 * 8.3145 * T_isochore_heat_2 / V_min_2
V_exp_2_plot = V_exp_2 * 1e6
V_comp_2_plot = V_comp_2 * 1e6
p_exp_2_plot = p_exp_2 / 100
p_comp_2_plot = p_comp_2 / 100
p_isochore_cool_2_plot = p_isochore_cool_2 / 100
p_isochore_heat_2_plot = p_isochore_heat_2 / 100
V_max_2_plot = V_max_2 * 1e6
V_min_2_plot = V_min_2 * 1e6

V_kp_A125 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36,32])
p_kp_A125 =np.array([1143, 1192,1202, 1171, 1115, 1044, 973, 913, 861, 819, 792, 780, 786, 809, 857, 923, 998, 1069, 1143])
Th_kp_A125 = 229.5 + 273.15
Tk_kp_A125 = 73.7 + 273.15

n_3_max = (V_kp_A125.max() * p_kp_A125.max()*0.0001) / (((Th_kp_A125 + Tk_kp_A125) / 2) * 8.3145)
n_3_min = (V_kp_A125.min() * p_kp_A125.min()*0.0001) / (((Th_kp_A125 + Tk_kp_A125) / 2) * 8.3145)
n_3 = (n_3_max + n_3_min) / 2

V_min_3 = V_kp_A125.min() * 1e-6
V_max_3 = V_kp_A125.max() * 1e-6
V_exp_3 = np.linspace(V_min_3, V_max_3, 100)
V_comp_3 = np.linspace(V_max_3, V_min_3, 100)
p_exp_3 = (n_3 * 8.3145 * Th_kp_A125) / V_exp_3
T_isochore_cool_3 = np.linspace(Th_kp_A125, Tk_kp_A125, 50)
p_isochore_cool_3 = n_3 * 8.3145 * T_isochore_cool_3 / V_max_3
p_comp_3 = (n_3 * 8.3145 * Tk_kp_A125) / V_comp_3
T_isochore_heat_3 = np.linspace(Tk_kp_A51, Th_kp_A51, 50)
p_isochore_heat_3 = n_3 * 8.3145 * T_isochore_heat_3 / V_min_3
V_exp_3_plot = V_exp_3 * 1e6
V_comp_3_plot = V_comp_3 * 1e6
p_exp_3_plot = p_exp_3 / 100
p_comp_3_plot = p_comp_3 / 100
p_isochore_cool_3_plot = p_isochore_cool_3 / 100
p_isochore_heat_3_plot = p_isochore_heat_3 / 100
V_max_3_plot = V_max_3 * 1e6
V_min_3_plot = V_min_3 * 1e6

fig, axs = plt.subplots(3, 1, figsize=(7.4, 9.4), sharex=True)

axs[0].plot(V_kp_A12, p_kp_A12, color = '#1f77b4')
axs[0].plot(V_exp_1_plot, p_exp_1_plot, color = '#1f77b4' ,label='Isotherme Expansion', linestyle='--')
axs[0].plot([V_max_1_plot]*len(p_isochore_cool_1_plot), p_isochore_cool_1_plot,color = '#1f77b4', label='Isochore Kühlung', linestyle='--')
axs[0].plot(V_comp_1_plot, p_comp_1_plot, label='Isotherme Kompression', linestyle='--')
axs[0].plot([V_min_1_plot]*len(p_isochore_heat_1_plot), p_isochore_heat_1_plot, color = '#1f77b4', linestyle='--', label='Isochore Erwärmung (Vmin)')
axs[0].set_ylabel(r'$p$ [hPA]')
axs[0].set_title("Versuch 1 - $R= 13.76 \Omega$ ")
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)


axs[1].plot(V_kp_A51, p_kp_A51, color = '#ff7f0e')
axs[1].plot(V_exp_2_plot, p_exp_2_plot, color = '#ff7f0e' ,label='Isotherme Expansion', linestyle='--')
axs[1].plot([V_max_2_plot]*len(p_isochore_cool_2_plot), p_isochore_cool_2_plot,color = '#ff7f0e', label='Isochore Kühlung', linestyle='--')
axs[1].plot(V_comp_2_plot, p_comp_2_plot,'#ff7f0e', label='Isotherme Kompression', linestyle='--')
axs[1].plot([V_min_2_plot]*len(p_isochore_heat_2_plot), p_isochore_heat_2_plot, color = '#ff7f0e', linestyle='--', label='Isochore Erwärmung (Vmin)')
axs[1].set_ylabel(r'$p$ [hPA]')
axs[1].set_title("Versuch 2 - $R= 100.78 \Omega$")
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)

axs[2].plot(V_kp_A125, p_kp_A125, color = '#2ca02c')
axs[2].plot(V_exp_3_plot, p_exp_3_plot, color = '#2ca02c' ,label='Isotherme Expansion', linestyle='--')
axs[2].plot([V_max_3_plot]*len(p_isochore_cool_3_plot), p_isochore_cool_3_plot,color = '#2ca02c', label='Isochore Kühlung', linestyle='--')
axs[2].plot(V_comp_3_plot, p_comp_3_plot,'#2ca02c', label='Isotherme Kompression', linestyle='--')
axs[2].plot([V_min_3_plot]*len(p_isochore_heat_3_plot), p_isochore_heat_3_plot, color = '#2ca02c', linestyle='--', label='Isochore Erwärmung (Vmin)')
axs[2].set_ylabel(r'$p$ [hPA]')
axs[2].set_title("Versuch 3 - $R= 598.33 \Omega$")
axs[2].spines['top'].set_visible(False)
axs[2].spines['right'].set_visible(False)
axs[2].set_xlabel(r'$V$ [mL]')

#boyle mariotte versuch

T_bm1 = 34.4
p_bm1 = np.array([1138,1126,1085, 1025, 968, 914, 874, 848, 834, 831, 838, 856, 885, 926, 980, 1038, 1088, 1123])
V_bm1 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36])

T_bm2 = 32.6
p_bm2 = np.array([1140, 1129, 1088, 1029, 971, 917, 877, 851, 835, 832, 838, 856, 885, 926, 979, 1036, 1088, 1123])
V_bm2 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36])

T_bm3 = 32.6
p_bm3 = np.array([1145, 1131, 1091,1033,974,920,879,853,838,834,841,859,889,930,984,1042,1093,1129])
V_bm3 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04, 36.96, 35 ,33.4 ,32.36])

V_fit = np.linspace(min(V_bm3), max(V_bm3), 100)

logV_1 = np.log(V_bm1)
logp_1 = np.log(p_bm1)
b_pow_1, loga_pow_1 = np.polyfit(logV_1, logp_1, 1)
a_pow_1 = np.exp(loga_pow_1)
p_fit_bm1 = a_pow_1 * V_fit**b_pow_1

logV_2 = np.log(V_bm2)
logp_2 = np.log(p_bm2)
b_pow_2, loga_pow_2 = np.polyfit(logV_2, logp_2, 1)
a_pow_2 = np.exp(loga_pow_2)
p_fit_bm2 = a_pow_2 * V_fit**b_pow_2

logV_3 = np.log(V_bm3)
logp_3 = np.log(p_bm3)
b_pow_3, loga_pow_3 = np.polyfit(logV_3, logp_3, 1)
a_pow_3 = np.exp(loga_pow_3)
p_fit_bm3 = a_pow_3 * V_fit**b_pow_3

fig, axs = plt.subplots(3, 1, figsize=(7.4, 9.4), sharex=True)

axs[0].scatter(V_bm1, p_bm1, marker='o', color = "#1f77b4", label="Messdaten")
axs[0].plot(V_fit, p_fit_bm1, color = "#8fbddc", linewidth=1, alpha=0.75 ,label= 'Regression')
axs[0].set_ylabel(r'$p$ [hPA]')
axs[0].set_title("Versuch 1")
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].tick_params(direction='out', length=4, width=1)
axs[0].text(42, 1100, 'T=34.4°C')
axs[0].text(42, 1050, fr'$p = {11133.189} \cdot V^{{-1.222}}$', fontsize=9)
axs[0].legend()

axs[1].scatter(V_bm2, p_bm2, marker='s', color = "#ff7f0e", label="Messdaten")
axs[1].plot(V_fit, p_fit_bm2, color = "#ffbf88", linewidth=1, alpha=0.75, label =r'Regression')
axs[1].set_ylabel(r'$p$ [hPa]')
axs[1].set_title("Versuch 2")
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].tick_params(direction='out', length=4, width=1)
axs[1].text(42, 1100, 'T=32.6°C')
axs[1].text(42, 1050, fr'$p = {11498.927} \cdot V^{{-1.258}}$', fontsize=9)
axs[1].legend()

axs[2].scatter(V_bm3, p_bm3, marker='^', color = "#2ca02c", label="Messdaten")
axs[2].plot(V_fit, p_fit_bm3, color = "#97d297", linewidth=1, alpha=0.75, label='Regression')
axs[2].set_xlabel(r'$V$ [mL]')
axs[2].set_ylabel(r'$p$ [hPA]')
axs[2].set_title("Versuch 3")
axs[2].spines['top'].set_visible(False)
axs[2].spines['right'].set_visible(False)
axs[2].tick_params(direction='out', length=4, width=1)
axs[2].text(42, 1100, 'T=32.6°C')
axs[2].text(42, 1050, fr'$p = {11548.024} \cdot V^{{-1.273}}$', fontsize=9)
axs[2].legend()

plt.tight_layout()
plt.show()
plt.close()

#wärmepunpe

p_d4 = np.array([1146, 1134, 1091, 1032, 973, 919, 878, 852, 838, 835, 843, 861, 891, 932, 987, 1044, 1095, 1130])
V_d4 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36])

p_d6 = np.array([1146, 1134, 1091, 1031, 973, 919, 878, 853, 838, 836, 843, 862, 892, 934, 989, 1046, 1097, 1131])
V_d6 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36])

p_d91 = np.array([1148, 1133, 1091, 1031, 972, 919, 879, 853, 839, 837, 846, 865, 895, 937, 992, 1049, 1099, 1134])
V_d91 = np.array([32, 32.36, 33.40, 35, 36.96, 39.04, 41, 42.6, 43.64, 44, 43.46, 42.6, 41.00, 39.04,36.96, 35,33.4,32.36])

fig, axs = plt.subplots(3, 1, figsize=(7.4, 9.4), sharex=True)

axs[0].scatter(V_d4, p_d4, marker='o', color = "#1f77b4", label="Messdaten")
axs[0].set_ylabel(r'$p$ [hPA]')
axs[0].set_title("Versuch 1 - $\Delta T = 4^\\circ$C")
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)
axs[0].tick_params(direction='out', length=4, width=1)

axs[1].scatter(V_d6, p_d6, marker='s', color = "#ff7f0e", label="Messdaten")
axs[1].set_ylabel(r'$p$ [hPa]')
axs[1].set_title("Versuch 2 - $\Delta T = 6^\\circ$C")
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)
axs[1].tick_params(direction='out', length=4, width=1)

axs[2].scatter(V_d91, p_d91, marker='^', color = "#2ca02c", label="Messdaten")
axs[2].set_xlabel(r'$V$ [mL]')
axs[2].set_ylabel(r'$p$ [hPA]')
axs[2].set_title("Versuch 3 - $\Delta T = 9.1^\\circ$C")
axs[2].spines['top'].set_visible(False)
axs[2].spines['right'].set_visible(False)
axs[2].tick_params(direction='out', length=4, width=1)

plt.tight_layout()
plt.show()
plt.close()

rpm = np.array([809, 679, 437])
pel = np.array([0.086, 0.262, 0.201])
pvol = np.array([3.223, 2.863, 2.027])

color_pel = "#1f77b4"  # Blau
color_pvol = "#ff7f0e"  # Orange

fig, ax = plt.subplots(figsize=(7.4, 4.5))

ax.plot(rpm, pel, 'o-', label=r'$P_{el}$', color=color_pel)
ax.plot(rpm, pvol, 'o-', label=r'$P_{vol}$', color=color_pvol)
ax.set_xlabel(r'Drehzahl [RPM]')
ax.set_ylabel(r'$P$ [W]')
ax.set_title(r'$P_{el}$ und $P_{vol}$ in Abhängigkeit von der Drehzahl')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(direction='out', length=4, width=1)
ax.legend()
plt.tight_layout()
plt.show()

rpm = np.array([809, 679, 437])
pel = np.array([0.086, 0.262, 0.201])
pvol = np.array([3.223, 2.863, 2.027])

color_pel = "#1f77b4"
color_pvol = "#ff7f0e"

fig, ax = plt.subplots(figsize=(7.4, 4.5))

ax.plot(rpm, pel, 'o-', label=r'$P_{el}$', color=color_pel)
ax.plot(rpm, pvol, 'o-', label=r'$P_{vol}$', color=color_pvol)
ax.set_xlabel(r'Drehzahl [RPM]')
ax.set_ylabel(r'$P$ [W]')
ax.set_title(r'$P_{el}$ und $P_{vol}$ in Abhängigkeit von der Drehzahl')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(direction='out', length=4, width=1)
ax.legend()
plt.tight_layout()
plt.show()

rpm_wp = np.array([587, 586, 587])
pel_wp = np.array([3.470, 3.470, 3.440])
pvol_wp = np.array([0.049, 0.459, 0.117])

color_pel = "#1f77b4"
color_pvol = "#ff7f0e"

fig, ax = plt.subplots(figsize=(7.4, 4.5))

ax.plot(rpm_wp, pel_wp, 'o-', label=r'$P_{el}$', color=color_pel)
ax.plot(rpm_wp, pvol_wp, 'o-', label=r'$P_{vol}$', color=color_pvol)
ax.set_xlabel(r'Drehzahl [RPM]')
ax.set_ylabel(r'$P$ [W]')
ax.set_title(r'$P_{el}$ und $P_{vol}$ in Abhängigkeit von der Drehzahl')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.tick_params(direction='out', length=4, width=1)
ax.legend()
plt.tight_layout()
plt.show()