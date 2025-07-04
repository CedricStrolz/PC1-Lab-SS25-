import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import linregress

#Daten
T_u = 28.5
p_u = 101600

M_a = 84.2
rho_a = 0.780
dH_a = 31.5
T_sa = 80.2

M_b = 74.1
rho_b = 0.932
dH_b = 32.5
T_sb = 56.5


#Molenbrüche

phiB = np.array([0.0, 0.1000, 0.2024, 0.2857, 0.4000, 0.6000, 0.7017, 0.8000, 0.9000, 1.0])
phiA = 1- phiB

m_A = phiA * rho_a
m_B = phiB * rho_b

n_A = m_A / M_a
n_B = m_B / M_b

x_B = n_B / (n_A + n_B)

print(x_B)
#Kalibrergerade Brix

n_mix = np.array([1.42354 , 1.41465, 1.40701, 1.39994, 1.391292, 1.37842, 1.371681, 1.367590, 1.36301, 1.35881])

coeffs = np.polyfit(x_B, n_mix, deg=2)
poly_func = np.poly1d(coeffs)

n_pred = poly_func(x_B)

ss_res = np.sum((n_mix - n_pred) ** 2)
ss_tot = np.sum((n_mix - np.mean(n_mix)) ** 2)
r_squared = 1 - (ss_res / ss_tot)

x_fit = np.linspace(0, 1, 200)
y_fit = poly_func(x_fit)

plt.figure(figsize=(10, 7))
plt.scatter(x_B, n_mix, color='navy', label='Messwerte')
plt.plot(x_fit, y_fit, color='forestgreen',
         label=r'$n_D = %.4f x^2 + %.4f x + %.4f$' % tuple(coeffs))
plt.xlabel('Molenbruch $x_B$ [–]')
plt.ylabel(r'Brechungsindex $n_D^{25}$ [–]')
plt.title('Kalibrierkurve', fontsize=10)
plt.text(0.02, max(n_mix)-0.01, r'$R^2 = %.5f$' % r_squared,
         fontsize=9, va='top')
plt.legend(frameon=False, loc='lower right')
plt.grid(True, linestyle=':', linewidth=0.5)
plt.tight_layout()
plt.show()

#Siedediagramm
import numpy as np
import matplotlib.pyplot as plt

x_kond = np.array([0, 0.4772, 0.6669, 0.6355, 0.6707, 0.7451, 0.7801, 0.82309, 0.8874, 1])
Tb = np.array([80.2 ,62.7, 58.4, 56.5, 55.7, 54.5, 53.9, 54.3, 54.9, 56.5])

x_rueck = np.array([0, 0.1058, 0.2115, 0.3157, 0.4671, 0.6711, 0.7634, 0.9193, 1])
Tb_R = np.array([80.2 ,62.7, 58.4, 56.5, 55.7, 54.5, 53.9, 54.9, 56.5])

x_kond_clean = x_kond[[0,1,3,4,5,6,8,9]]
Tb_kond_clean = Tb[[0,1,3,4,5,6,8,9]]

x_rueck_clean = x_rueck[[0,1,2,3,4,5,6,8]]
Tb_rueck_clean = Tb_R[[0,1,2,3,4,5,6,8]]

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x_kond_clean, Tb_kond_clean, color='navy', linestyle='-', label='Kondensationskurve')
ax.plot(x_rueck_clean, Tb_rueck_clean, color='red', linestyle='-', label='Siedekurve')
ax.scatter(x_kond_clean, Tb_kond_clean, color='navy', label='Kondensat')
ax.scatter(x_rueck_clean, Tb_rueck_clean, color='red', label='Sumpf')
ax.set_xlabel("$x_B$ []", fontsize=10)
ax.set_ylabel("T [K]", fontsize=10)
ax.tick_params(labelsize=8)
ax.set_xlim(0, 1)
ax.set_ylim(50, 82)
ax.legend(fontsize=8, loc="upper right", frameon=False)
plt.title('Siedediagramm', fontsize=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.text(0.70, 81, r'$p = 101.6\ \mathrm{kPa}$', fontsize=10, color='black')
ax.text(0.60, 70, 'gas', fontsize=10, color='black')
ax.text(0.45, 53, r'liquid', fontsize=10, color='black')
ax.text(0.22, 63, r'gas + liquid', fontsize=10, color='black')
plt.tight_layout()
plt.show()
plt.close()

#aktivitätsdiagramm

a_A_id = np.array([1, 0.5,0])
a_B_id = np.array([0, 0.5 ,1])
x_A_id = np.array([1, 0.5,0])
x_B_id = np.array([0, 0.5,1])
a_A_real = np.array([1,0.9090 , 0.7782, 0.7356, 0.5836, 0.5216, 0.4151, 0.2578, 0])
a_B_real = np.array([0,0.3813, 0.6273, 0.6937, 0.7905, 0.8583, 0.8958, 0.9415, 1])
print(x_B)
x_B_akt = np.array([0, 0.13108421, 0.35193547, 0.47510889, 0.67068468, 0.76155515, 0.84450179, 0.92435486, 1])

coeffs_A = np.polyfit(x_B_akt, a_A_real, 3)
coeffs_B = np.polyfit(x_B_akt, a_B_real, 3)
x_fit = np.linspace(0, 1, 100)
y_A_fit = np.polyval(coeffs_A, x_fit)
y_B_fit = np.polyval(coeffs_B, x_fit)

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x_B_id, a_A_id, color='navy', linestyle='--', alpha=0.5)
ax.plot(x_B_id, a_B_id, color='red', linestyle='--', alpha=0.5)
ax.scatter(x_B_akt, a_A_real,color='navy')
ax.scatter(x_B_akt, a_B_real,color='red')
ax.plot(x_fit, y_A_fit, color='navy')
ax.plot(x_fit, y_B_fit, color='red')
ax.set_xlabel("$x_B$ []", fontsize=10)
ax.set_ylabel("Aktivität []", fontsize=10)
ax.tick_params(labelsize=8)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
plt.title('Aktivitätsdiagramm', fontsize=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.tight_layout()
plt.show()
plt.close()

yA_p = np.array([
    1,
    0.520988045288427,
    0.361320273726045,
    0.25187316656547,
    0.216997558533972,
    0.174452435494903,
    0.111007869215921,
    0
])

yB_p = np.array([
    0,
    0.479011954711573,
    0.668823289159516,
    0.74812683343453,
    0.783002441466028,
    0.825547564505098,
    0.888992130784079,
    1
])

pU_ges = np.array([
    73654.3163565801,
    128565.781691962,
    158634.300803584,
    170659.938142029,
    177043.887825944,
    175256.405179335,
    171051.682109065,
    161512.05454311
])*0.001
x_B_ber = np.array([0, 0.13108421, 0.25625161, 0.67068468, 0.76155515, 0.84450179, 0.92435486, 1])
minivap = np.array([
    73.8,
    116.8,
    142.1,
    151.2,
    159.7,
    162.7,
    160.6,
    154.2
])

fig, ax = plt.subplots(figsize=(10, 10))

ax.scatter(x_B_ber, pU_ges, color='navy', label='Kondensat')
ax.scatter(yB_p, pU_ges, color='red', label='Sumpf')
ax.scatter(x_B_ber, minivap, color='green', linewidth=2, label='Minivap', alpha= 0.5)
ax.plot(x_B_ber, pU_ges, color='navy', linewidth=2, label='Kondensationskurve', alpha=0.5)
ax.plot(x_B_ber, minivap, color='green', linewidth=2, label='Minivap', alpha= 0.5)
ax.plot(yB_p, pU_ges, color='red', linewidth=2, label='Siedekurve', alpha= 0.5)
ax.set_xlabel("$x_B$ []", fontsize=10)
ax.set_ylabel("p [kPa]", fontsize=10)
ax.tick_params(labelsize=8)
ax.legend(fontsize=8, loc="lower right", frameon=False)
plt.title('Dampfdruckdiagramm', fontsize=15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.text(0.85, 82, r'$T_w = 343.15\ \mathrm{K}$', fontsize=10, color='black')
ax.text(0.3, 169, r'liquid', fontsize=10, color='black')
ax.text(0.25, 132, r'gas+liquid', fontsize=10, color='black')
ax.text(0.8, 100, r'gas', fontsize=10, color='black')
plt.tight_layout()
ax.set_xlim(0, 1)

plt.show()
plt.close()

x_kond = np.array([0, 0.4772, 0.6669, 0.6355, 0.6707, 0.7451, 0.7801, 0.82309, 0.8874, 1])
Tb = np.array([80.2 ,62.7, 58.4, 56.5, 55.7, 54.5, 53.9, 54.3, 54.9, 56.5])
x_rueck = np.array([0, 0.1058, 0.2115, 0.3157, 0.4671, 0.6711, 0.7634, 0.9193, 1])
Tb_R = np.array([80.2 ,62.7, 58.4, 56.5, 55.7, 54.5, 53.9, 54.9, 56.5])

x_kond_clean = x_kond[[0,1,3,4,5,6,8,9]]
Tb_kond_clean = Tb[[0,1,3,4,5,6,8,9]]
x_rueck_clean = x_rueck[[0,1,2,3,4,5,6,8]]
Tb_rueck_clean = Tb_R[[0,1,2,3,4,5,6,8]]

yA_p = np.array([
    1,
    0.520988045288427,
    0.361320273726045,
    0.25187316656547,
    0.216997558533972,
    0.174452435494903,
    0.111007869215921,
    0
])
yB_p = np.array([
    0,
    0.479011954711573,
    0.668823289159516,
    0.74812683343453,
    0.783002441466028,
    0.825547564505098,
    0.888992130784079,
    1
])
pU_ges = np.array([
    73654.3163565801,
    128565.781691962,
    158634.300803584,
    170659.938142029,
    177043.887825944,
    175256.405179335,
    171051.682109065,
    161512.05454311
]) * 0.001  # [kPa]
x_B_ber = np.array([0, 0.13108421, 0.25625161, 0.67068468, 0.76155515, 0.84450179, 0.92435486, 1])

minivap = np.array([
    73.8,
    116.8,
    142.1,
    151.2,
    159.7,
    162.7,
    160.6,
    154.2
])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 10), sharex=True)

ax1.plot(x_kond_clean, Tb_kond_clean, color='navy', linestyle='-', label='Kondensationskurve')
ax1.plot(x_rueck_clean, Tb_rueck_clean, color='red', linestyle='-', label='Siedekurve')
ax1.scatter(x_kond_clean, Tb_kond_clean, color='navy')
ax1.scatter(x_rueck_clean, Tb_rueck_clean, color='red')

ax1.set_xlabel("$x_B$ [–]", fontsize=8)
ax1.set_ylabel("T [°C]", fontsize=8)
ax1.set_xlim(0, 1)
ax1.set_ylim(50, 82)
ax1.tick_params(labelsize=8)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
ax1.text(0.70, 77, r'$p = 101.6\ \mathrm{kPa}$', fontsize=8)
ax1.text(0.6, 70, 'gas', fontsize=8)
ax1.text(0.45, 53, 'liquid', fontsize=8)
ax1.text(0.22, 63, 'gas + liquid', fontsize=8)

ax2.plot(x_B_ber, pU_ges, color='navy', linewidth=2, alpha=0.5, label='Kondensationskurve')
ax2.plot(yB_p, pU_ges, color='red', linewidth=2, alpha=0.5, label='Siedekurve')
ax2.scatter(x_B_ber, pU_ges, color='navy')
ax2.scatter(yB_p, pU_ges, color='red')
ax2.scatter(x_B_ber, minivap, color='green', linewidth=2, label='Minivap', alpha= 0.5)
ax2.plot(x_B_ber, minivap, color='green', linewidth=2, label='Minivap', alpha= 0.5)

ax2.set_xlabel("$x_B$ []", fontsize=8)
ax2.set_ylabel("p [kPa]", fontsize=8)
ax2.set_xlim(0, 1)
ax2.set_ylim(70, 180)
ax2.tick_params(labelsize=8)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.text(0.05, 175, r'$T_w = 343.15\ \mathrm{K}$', fontsize=10)
ax2.text(0.3, 169, 'liquid', fontsize=10)
ax2.text(0.25, 132, 'gas + liquid', fontsize=10)
ax2.text(0.8, 100, 'gas', fontsize=10)

plt.tight_layout()
plt.show()
plt.close()
