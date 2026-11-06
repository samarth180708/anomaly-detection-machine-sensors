"""Offline anomaly detection: Rolling Z-score + Isolation Forest.
Usage: python detect.py [data.csv]   (CSV: last column = sensor value)
"""
import sys, numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    x = pd.read_csv(sys.argv[1]).iloc[:, -1].astype(float).to_numpy()
else:
    rng = np.random.default_rng(1)
    x = 70 + 3*np.sin(np.arange(1000)/15) + rng.normal(0, .6, 1000)
    x[[200, 450, 700]] += 9
    x[800:860] += np.linspace(0, 8, 60)

s = pd.Series(x)
z = (s - s.rolling(60).mean().shift(1)) / s.rolling(60).std().shift(1)
flag_z = (z.abs() > 3.5).fillna(False).to_numpy()
iso = IsolationForest(contamination=0.02, random_state=0).fit(x.reshape(-1, 1))
flag_if = iso.predict(x.reshape(-1, 1)) == -1

print(f"Rolling Z-score anomalies : {flag_z.sum()}")
print(f"Isolation Forest anomalies: {flag_if.sum()}")
plt.figure(figsize=(11, 4)); plt.plot(x, lw=1, label="sensor")
plt.scatter(np.where(flag_z)[0], x[flag_z], c="r", s=18, label="Z-score")
plt.scatter(np.where(flag_if)[0], x[flag_if], facecolors="none", edgecolors="k", s=40, label="IsoForest")
plt.legend(); plt.tight_layout(); plt.savefig("result.png", dpi=120)
print("Saved result.png")
