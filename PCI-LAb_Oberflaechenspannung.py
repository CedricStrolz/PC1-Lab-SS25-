import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Dichten in g/cm³
roh_Probe_15 = 0.79642
roh_Probe_25 = 0.78520
roh_Probe_35 = 0.77989
roh_Air = 0.001
roh_Wasser = 0.99587

# Ringradius in cm, g in m/s²
R_ring = 0.954
g = 9.81

# -------------------- Wasser --------------------
m_H2O_rein = np.array([0.863, 0.860, 0.863, 0.864, 0.864, 0.857])
m_H2O_rein_avg = np.mean(m_H2O_rein)
V_H2O = m_H2O_rein_avg / (roh_Wasser - roh_Air)
R3V_H2O = (R_ring**3) / V_H2O
print(f"R³/V für Wasser = {R3V_H2O}")

beta_H2O = 0.932
sigma_H2O = (beta_H2O * m_H2O_rein_avg * g) / (4 * pi * R_ring * 0.01)

# -------------------- Probe --------------------
m_Probe_2mL = np.array([0.645, 0.641, 0.648, 0.652, 0.651, 0.649])
m_Probe_4mL = np.array([0.587, 0.594, 0.596, 0.597, 0.586, 0.590, 0.600, 0.590])
m_Probe_6mL = np.array([0.554, 0.557, 0.554, 0.550, 0.548, 0.551])

m_Probe_2mL_avg = np.mean(m_Probe_2mL)
m_Probe_4mL_avg = np.mean(m_Probe_4mL)
m_Probe_6mL_avg = np.mean(m_Probe_6mL)

beta_Probe_2mL = 0.91
beta_Probe_4mL = 0.9049
beta_Probe_6mL = 0.9

sigma_Probe_2mL = (beta_Probe_2mL * m_Probe_2mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Probe_4mL = (beta_Probe_4mL * m_Probe_4mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Probe_6mL = (beta_Probe_6mL * m_Probe_6mL_avg * g) / (4 * pi * R_ring * 0.01)

sigma_Probe = np.array([
    sigma_Probe_2mL,
    sigma_Probe_4mL,
    sigma_Probe_6mL
])

# -------------------- Ethanol --------------------
m_Ethanol_2mL = np.array([0.605, 0.608, 0.608, 0.603, 0.598, 0.599])
m_Ethanol_4mL = np.array([0.542, 0.545, 0.546, 0.545, 0.543, 0.545])
m_Ethanol_6mL = np.array([0.491, 0.491, 0.492, 0.489, 0.493, 0.493])

m_Ethanol_2mL_avg = np.mean(m_Ethanol_2mL)
m_Ethanol_4mL_avg = np.mean(m_Ethanol_4mL)
m_Ethanol_6mL_avg = np.mean(m_Ethanol_6mL)

beta_Ethanol_2mL = 0.904
beta_Ethanol_4mL = 0.898
beta_Ethanol_6mL = 0.8919

sigma_Ethanol_2mL = (beta_Ethanol_2mL * m_Ethanol_2mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Ethanol_4mL = (beta_Ethanol_4mL * m_Ethanol_4mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Ethanol_6mL = (beta_Ethanol_6mL * m_Ethanol_6mL_avg * g) / (4 * pi * R_ring * 0.01)

sigma_Ethanol = np.array([
    sigma_Ethanol_2mL,
    sigma_Ethanol_4mL,
    sigma_Ethanol_6mL
])

# -------------------- Propanol --------------------
m_Propanol_2mL = np.array([0.520, 0.519, 0.517, 0.516, 0.512, 0.509])
m_Propanol_4mL = np.array([0.416, 0.414, 0.416, 0.417, 0.412, 0.413])
m_Propanol_6mL = np.array([0.371, 0.371, 0.376, 0.371, 0.376, 0.369])

m_Propanol_2mL_avg = np.mean(m_Propanol_2mL)
m_Propanol_4mL_avg = np.mean(m_Propanol_4mL)
m_Propanol_6mL_avg = np.mean(m_Propanol_6mL)

beta_Propanol_2mL = 0.896
beta_Propanol_4mL = 0.88
beta_Propanol_6mL = 0.8718

sigma_Propanol_2mL = (beta_Propanol_2mL * m_Propanol_2mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Propanol_4mL = (beta_Propanol_4mL * m_Propanol_4mL_avg * g) / (4 * pi * R_ring * 0.01)
sigma_Propanol_6mL = (beta_Propanol_6mL * m_Propanol_6mL_avg * g) / (4 * pi * R_ring * 0.01)

sigma_Propanol = np.array([
    sigma_Propanol_2mL,
    sigma_Propanol_4mL,
    sigma_Propanol_6mL
])

from scipy.stats import linregress

V_fit = np.array([2, 4, 6])

sigma_Probe_fit = sigma_Probe
sigma_Ethanol_fit = sigma_Ethanol
sigma_Propanol_fit = sigma_Propanol

slope_probe, intercept_probe, *_ = linregress(V_fit, sigma_Probe_fit)
slope_ethanol, intercept_ethanol, *_ = linregress(V_fit, sigma_Ethanol_fit)
slope_propanol, intercept_propanol, *_ = linregress(V_fit, sigma_Propanol_fit)

V_smooth = np.linspace(2, 6, 100)

fit_probe = slope_probe * V_smooth + intercept_probe
fit_ethanol = slope_ethanol * V_smooth + intercept_ethanol
fit_propanol = slope_propanol * V_smooth + intercept_propanol

fig, ax = plt.subplots(figsize=(8, 6))

ax.scatter([ 2, 4, 6], sigma_Probe, color='green', label='Probe', s=60)
ax.scatter([ 2, 4, 6], sigma_Ethanol, color='blue', label='Ethanol', s=60)
ax.scatter([ 2, 4, 6], sigma_Propanol, color='red', label='Propanol', s=60)
ax.scatter(0, sigma_H2O, color='yellow', label='H2O', s=60)

ax.plot(V_smooth, fit_probe, color='green', linestyle='--')
ax.plot(V_smooth, fit_ethanol, color='blue', linestyle='--')
ax.plot(V_smooth, fit_propanol, color='red', linestyle='--')

ax.set_xlabel(r'Volumen $V$ [mL]', fontsize=12)
ax.set_ylabel(r'Oberflächenspannung $\sigma$ [mN/m]', fontsize=12)
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(fontsize=9, frameon=False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()


#Automatisierte Messung

Temp = np.array([15.6, 15.9, 15.7, 25.1, 25.2, 25.1, 25.1, 25.2, 25.1, 30.0, 30, 30])
sigma_autom = np.array([23.69, 23.80, 21.12, 22.07, 20.44, 20.44, 20.59, 21.05, 21.33, 20.95, 22.21, 21.88 ])

# Bereinigte Daten
Temp_ber = np.array([15.6, 15.9, 25.1, 25.2, 25.1, 30.0, 30, 30])
sigma_autom_ber = np.array([23.69, 23.80, 22.07, 21.05, 21.33, 20.95, 22.21, 21.88 ])

# Regression für Originaldaten
slope_org, intercept_org, r_org, _, _ = linregress(Temp, sigma_autom)
x_org = np.linspace(min(Temp), max(Temp), 100)
y_org = slope_org * x_org + intercept_org

# Regression für bereinigte Daten
slope_ber, intercept_ber, r_ber, _, _ = linregress(Temp_ber, sigma_autom_ber)
x_ber = np.linspace(min(Temp_ber), max(Temp_ber), 100)
y_ber = slope_ber * x_ber + intercept_ber

# Plot
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

# Plot 1: Originaldaten
axs[0].scatter(Temp, sigma_autom, color='#1f77b4', label='Originaldaten')
axs[0].plot(x_org, y_org, color='#1f77b4', linestyle='--', label=f'Regression (R²={r_org**2:.2f})')
axs[0].set_ylabel(r'$\sigma$ [mN/m]')
axs[0].legend()
axs[0].spines['top'].set_visible(False)
axs[0].spines['right'].set_visible(False)

# Plot 2: Bereinigte Daten
axs[1].scatter(Temp_ber, sigma_autom_ber, color='#ff7f0e', label='Bereinigte Daten')
axs[1].plot(x_ber, y_ber, color='#ff7f0e', linestyle='--', label=f'Regression (R²={r_ber**2:.2f})')
axs[1].set_ylabel(r'$\sigma$ [mN/m]')
axs[1].set_xlabel(r'Temperatur [°C]')
axs[1].legend()
axs[1].spines['top'].set_visible(False)
axs[1].spines['right'].set_visible(False)

plt.tight_layout()
plt.show()

ranges = {
    '15 ± 1 °C': (14.0, 16.0),
    '25 ± 1 °C': (24.0, 26.0),
    '30 ± 1 °C': (29.0, 31.0)
}

sigma_by_temp = []
labels = []

for label, (low, high) in ranges.items():
    indices = (Temp >= low) & (Temp <= high)
    values = sigma_autom[indices]
    sigma_by_temp.append(values)
    labels.append(label)

fig, axs = plt.subplots(1, 1, figsize=(7.4, 3.4))

axs.boxplot(sigma_by_temp, patch_artist=True,
            boxprops=dict(facecolor='#1f77b4', color='black', alpha=0.5),
            medianprops=dict(color='black'),
            whiskerprops=dict(color='black'),
            capprops=dict(color='black'),
            flierprops=dict(markerfacecolor='red', marker='o', markersize=5, linestyle='none', markeredgecolor='black'))

axs.set_xticklabels(labels)
axs.set_ylabel(r'$\sigma$ [mN/m]')
axs.spines['top'].set_visible(False)
axs.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()
