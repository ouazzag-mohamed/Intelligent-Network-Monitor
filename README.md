<div align="center">

<pre>
   _____   _   _   __  __ 
  |_   _| | \ | | |  \/  |
    | |   |  \| | | \  / |
    | |   | . ` | | |\/| |
   _| |_  | |\  | | |  | |
  |_____| |_| \_| |_|  |_|
</pre>

# 🛡️ Intelligent Network Monitor (AI-IDS)

**AI-Powered Intrusion Detection System with Real-Time Inference API**

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-00a393.svg)](https://fastapi.tiangolo.com/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange.svg)](https://scikit-learn.org/)
[![Accuracy](https://img.shields.io/badge/Model_Accuracy-99.8%25-success.svg)]()

</div>

---

## 📖 About The Project

Traditional firewalls rely on static if-else rules and struggle to detect zero-day or mutated cyber-attacks. The **Intelligent Network Monitor (INM)** is a next-generation approach that leverages Machine Learning (**Random Forest Classifier**) to dynamically understand and classify network behavior.

Trained on the robust **NSL-KDD dataset**, this system acts as the "Brain" of a modern firewall. It features a high-performance **FastAPI Backend** equipped with a real-time **Inference Pipeline**, allowing it to translate human-readable network protocols (like `tcp`, `http`) into machine-readable tensors on the fly.

## ✨ Key Features

- **🧠 Machine Learning Core:** Random Forest model with 100 estimators achieving **99.8% accuracy**.
- **⚡ Real-Time API:** Built with FastAPI for lightning-fast threat detection.
- **🔄 Live Data Translation:** Automated `LabelEncoders` translate raw strings (e.g., `protocol_type: tcp`) instantly before feeding them to the AI.
- **🛡️ Threat Classification:** Differentiates between Normal traffic and various attack types (DoS, Probe, R2L, U2R).

## 🏗️ System Architecture

1. **Packet Capture (External):** Tools like Zeek/Suricata extract 41 features from live network packets.
2. **Inference Pipeline (API):** The FastAPI server receives a JSON payload, translates strings to numeric indices using pre-trained `.pkl` encoders.
3. **AI Brain (Predictor):** The Random Forest model evaluates the 41-feature array in milliseconds.
4. **Action (Output):** Returns a `Safe ✅` or `Danger ❌` response to the firewall logic.

## 📂 Project Structure

```text
Intelligent-Network-Monitor/
│
├── data/
│   └── processed_network_traffic.csv  # Cleaned dataset (Not pushed to Git)
│
├── models/
│   ├── random_forest_brain.pkl        # The trained AI model (Not pushed to Git)
│   └── encoders_dictionary.pkl        # Text-to-Number translators (Not pushed to Git)
│
├── EDA_Network_Traffic_1.ipynb        # Data preparation & Encoder training
├── Model_Training.ipynb               # Model training & Evaluation
├── main.py                            # FastAPI Backend server
├── payload.json                       # Sample test data for cURL
└── README.md                          # Project documentation
```

# 🚀 Quick Start

## 1. Clone & Setup
```bash
git clone https://github.com/ouazzag-mohamed/Intelligent-Network-Monitor.git
cd Intelligent-Network-Monitor
```

## 2. Install Dependencies
```bash
pip install -r requirments.txt
```

## 3. Run the API Server
```bash
uvicorn main:app --reload
```

The server will start at:  
👉 http://127.0.0.1:8000  

You can view the interactive Swagger UI at:  
👉 http://127.0.0.1:8000/docs

---

# 🧪 Testing the API (cURL)

Send a simulated **Normal network packet** using `curl` and the provided `payload.json` file.

*(Make sure your server is running, and you execute this command in the same directory as `payload.json`)*

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
     -H "Content-Type: application/json" \
     -d @payload.json
```

## Expected Response

```json
{
  "status": "safe",
  "prediction": "Normal ✅",
  "threat_level": "Low"
}
```

---

Built with 💻 and 🛡️ by **Mohamed Ouazzag**