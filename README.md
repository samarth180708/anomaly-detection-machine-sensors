# Anomaly Detection in Machine Sensor Readings (IIoT)

Running prototype: machine sensors (temperature, vibration, pressure) ka live stream simulate hota hai aur real-time me anomalies detect hoti hain.

## Features
- 3 simulated sensors, har 200 ms par reading
- 2 detection methods: **Rolling Z-score** aur **EWMA residual**
- Adjustable threshold (σ) aur window size
- Fault injection: **spike** (sudden fault) aur **drift** (slow wear/degradation)
- CSV replay: apna sensor data upload karo (last column = value); `sample_data.csv` try karo
- Live alert log + anomaly counter
- `python/detect.py`: offline Z-score + Isolation Forest comparison

## GitHub Pages par deploy
1. GitHub par naya repo banao (e.g. `iiot-anomaly-detection`).
2. Is zip ko extract karke saari files repo me upload karo (`index.html` root me hona chahiye).
3. **Settings → Pages → Source: Deploy from a branch → main / (root) → Save**.
4. 1-2 min baad link milega: `https://<username>.github.io/iiot-anomaly-detection/`

## Local run
- `index.html` ko browser me double-click karo, ya `python -m http.server` chalao.
- Offline script: `pip install -r python/requirements.txt` → `python python/detect.py sample_data.csv`

## Kaise kaam karta hai
- **Z-score**: z = (x − mean) / std, pichhli N normal readings par. |z| > threshold → anomaly.
- **EWMA**: smoothed forecast se residual nikalta hai; bada residual → anomaly.
- Anomalous points window me add nahi hote, isliye drift/level-shift flag hota rehta hai.

## Real hardware se connect karna (next step)
Sensors (ESP32/Arduino) se MQTT ya HTTP se data bhejo aur `tick()` me simulated value ki jagah real value `feed(s, value)` me do.
