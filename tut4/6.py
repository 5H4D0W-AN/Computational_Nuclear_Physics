import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root 

MeV, fm, c = 1, 1, 1
ℏ = 197.3269631 * MeV * fm / c

gv = np.sqrt(195.9)
gs = np.sqrt(267.1)
mv = ms = M = 939 * MeV / c ** 2
kf = np.linspace(0.1, 3.1, 100) * ℏ * c

def rooter(γ, mv, ms, ml, el, pl):
    for kF in kf:
        def m(M_):
            EF = np.sqrt(kF ** 2 + M_ ** 2)
            return M - (gs / (ms * 2 * np.pi)) ** 2 * γ * M_ * (kF * EF - M_ ** 2 * np.log((kF + EF) / M_)) - M_
        M_ = root(m, ml[-1] * M).x
        EF = np.sqrt(kF ** 2 + M_ ** 2)
    
        ρB = γ / (6 * np.pi ** 2) * kF ** 3
    
        E = 0.5 * (gv / mv * ρB) ** 2 + 0.5 * (ms / gs * (M - M_)) ** 2 \
            + γ / (4 * np.pi) ** 2 * (kF * EF * (kF **2 + EF ** 2) - M_ ** 4 * np.log((kF + EF) / M_))
    
        P = 0.5 * (gv / mv * ρB) ** 2 - 0.5 * (ms / gs * (M - M_)) ** 2 \
            + γ / (3 * (4 * np.pi) ** 2) * (kF * EF * (2 * kF **2 - 3 * M_ ** 2) + 3 * M_ ** 4 * np.log((kF + EF) / M_))
    
        ml.append(M_ / M)
        el.append(E / ρB - M)
        pl.append(P / (ℏ * c) ** 3)
    return ml, el, pl

ml1, el1, pl1 = rooter(2, 939, 939, [1], [], [])
ml2, el2, pl2 = rooter(4, 939, 939, [1], [], [])

ml1 = ml1[1:]
ml2 = ml2[1:]

fig = plt.figure(figsize=(20, 4))

fig.add_subplot(1, 3, 1)
plt.plot(kf / (ℏ * c), ml1, label="neutron")
plt.plot(kf / (ℏ * c), ml2, label="nuclear")
plt.legend()

fig.add_subplot(1, 3, 2)
plt.plot(kf / (ℏ * c), el1, label="neutron")
plt.plot(kf / (ℏ * c), el2, label="nuclear")
plt.xlim(0.5, 2)
plt.ylim(-20, 25)
plt.legend()

fig.add_subplot(1, 3, 3)
plt.plot(kf / (ℏ * c), pl1, label="neutron")
plt.plot(kf / (ℏ * c), pl2, label="nuclear")
plt.xlim(0, 2.2)
plt.ylim(-8, 100)
plt.legend()

plt.show()

# ms = 500 * MeV / c ** 2
# mv = 782 * MeV / c ** 2

ml1, el1, pl1 = rooter(2, 500, 782, [1], [], [])
ml2, el2, pl2 = rooter(4, 500, 782, [1], [], [])

ml1 = ml1[1:]
ml2 = ml2[1:]

fig = plt.figure(figsize=(20, 4))

fig.add_subplot(1, 3, 1)
plt.plot(kf / (ℏ * c), ml1, label="neutron")
plt.plot(kf / (ℏ * c), ml2, label="nuclear")
plt.legend()

fig.add_subplot(1, 3, 2)
plt.plot(kf / (ℏ * c), el1, label="neutron")
plt.plot(kf / (ℏ * c), el2, label="nuclear")
plt.xlim(0, 1.5)
plt.ylim(-5, 100)
plt.legend()

fig.add_subplot(1, 3, 3)
plt.plot(kf / (ℏ * c), pl1, label="neutron")
plt.plot(kf / (ℏ * c), pl2, label="nuclear")
plt.xlim(0, 2.2)
plt.ylim(-5, 100)
plt.legend()

plt.show()