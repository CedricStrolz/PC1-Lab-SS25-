import numpy as np
import matplotlib.pyplot as plt
import math as m

ln_phi_pyk = np.array([m.log(2.2383), m.log(2.3436), m.log(2.4612)])
ln_phi_dma = np.array([m.log(2.2099), m.log(2.3109), m.log(2.4436)])
T_inv = np.array([1/(20+273.15), 1/(25+273.15), 1/(30+273.15)])

fit_pyk = np.polyfit(T_inv, ln_phi_pyk, 1)
fit_dma = np.polyfit(T_inv, ln_phi_dma, 1)
poly_pyk = np.poly1d(fit_pyk)
poly_dma = np.poly1d(fit_dma)

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred)**2)
    ss_tot = np.sum((y_true - np.mean(y_true))**2)
    return 1 - ss_res / ss_tot

r2_pyk = r_squared(ln_phi_pyk, poly_pyk(T_inv))
r2_dma = r_squared(ln_phi_dma, poly_dma(T_inv))

T_inv_fit = np.linspace(min(T_inv), max(T_inv), 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7), sharey=True)

ax1.scatter(T_inv, ln_phi_pyk, color='navy', s=50, label='Daten')
ax1.plot(T_inv_fit, poly_pyk(T_inv_fit), '--', color='navy', label='Regression')
ax1.set_title("Pyknometer", fontsize=12)
ax1.set_xlabel(r"$1/T$ [1/°C]", fontsize=11)
ax1.set_ylabel(r"$\ln(\phi)$", fontsize=11)
ax1.legend(fontsize=10, frameon=False)
ax1.tick_params(labelsize=9)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)

eq1 = r"$\ln(\phi) = {:.4f} \cdot \frac{{1}}{{T}} + {:.4f}$".format(fit_pyk[0], fit_pyk[1])
r2_text1 = r"$R^2 = {:.4f}$".format(r2_pyk)
ax1.text(0.0033, 0.81, eq1 + "\n" + r2_text1, fontsize=10)

ax2.scatter(T_inv, ln_phi_dma, color='darkred', s=50, label='Daten')
ax2.plot(T_inv_fit, poly_dma(T_inv_fit), '--', color='darkred', label='Regression')
ax2.set_title("DMA38", fontsize=12)
ax2.set_xlabel(r"$1/T$ [1/°C]", fontsize=11)
ax2.legend(fontsize=10, frameon=False)
ax2.tick_params(labelsize=9)
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)

eq2 = r"$\ln(\phi) = {:.4f} \cdot \frac{{1}}{{T}} + {:.4f}$".format(fit_dma[0], fit_dma[1])
r2_text2 = r"$R^2 = {:.4f}$".format(r2_dma)
ax2.text(0.0033, 0.81, eq2 + "\n" + r2_text2, fontsize=10)

plt.suptitle("Arrhenius-Diagramm: Pyknometer vs. DMA38", fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

t = np.array([21.13, 14.53, 11.28, 9.46, 8.36, 7.7, 7.54, 6.94, 6.04, 11.47])
alpha = np.array([20, 30, 40, 50, 60, 70, 75, 80, 85, 90])
sina = np.array([m.sin(m.radians(a)) for a in alpha])
tsina = t * sina

mask = alpha <= 70
alpha_fit = alpha[mask]
tsina_fit = tsina[mask]

coeffs = np.polyfit(alpha_fit, tsina_fit, 1)
fit_func = np.poly1d(coeffs)

alpha_line = np.linspace(min(alpha_fit), max(alpha_fit), 200)
tsina_line = fit_func(alpha_line)

import numpy as np
import matplotlib.pyplot as plt
import math as m

t = np.array([21.13, 14.53, 11.28, 9.46, 8.36, 7.7, 7.54, 6.94, 6.04, 11.47])
alpha = np.array([20, 30, 40, 50, 60, 70, 75, 80, 85, 90])
sina = np.array([m.sin(m.radians(a)) for a in alpha])
tsina = t * sina

mask = alpha <= 70
alpha_fit = alpha[mask]
tsina_fit = tsina[mask]

coeffs = np.polyfit(alpha_fit, tsina_fit, 1)
fit_func = np.poly1d(coeffs)
alpha_line = np.linspace(min(alpha_fit), max(alpha_fit), 200)
tsina_line = fit_func(alpha_line)

fig, ax = plt.subplots(figsize=(8, 6))
ax.scatter(alpha, tsina, color='green', s=60, label='Datenpunkte')
ax.plot(alpha_line, tsina_line, '--', color='black', label=r'Regression bis $70^\circ$')
ax.set_xlabel(r'$\alpha$ [°]', fontsize=12)
ax.set_ylabel(r'$t \cdot \sin(\alpha)$', fontsize=12)
ax.set_title(r'$t \cdot \sin(\alpha)$ vs. $\alpha$', fontsize=14)
ax.tick_params(labelsize=10)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(fontsize=10, frameon=False)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
plt.show()
