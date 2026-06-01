# LuvLogic
## ⚙️ Engineering Installation & Local Setup

Deploy the system locally within an isolated virtual environment using the following steps:

1. Clone the Source Repository
```
Bash
git clone [https://github.com/your-username/DuoDevotion.git](https://github.com/your-username/DuoDevotion.git)
cd DuoDevotion
```
2. Install Unified System Dependencies
Ensure the machine learning processing array and the official Google AI packages are fully compiled:
```
Bash
pip install -r requirements.txt
```
3. Establish the Local Secrets Ecosystem
Streamlit relies on strict directory parameters for secret storage. Construct the hidden .streamlit directory and seed your credentials file:
```
Bash
mkdir .streamlit
touch .streamlit/secrets.toml
```
Open .streamlit/secrets.toml in your code editor and populate it with your private developer credentials:
```
Ini, TOML
GEMINI_API_KEY = "AIzaSyYourActualGoogleAIStudioKeyHere"
```
4. Boot the Localhost Server
Execute the runtime wrapper to initialize the platform locally:
```
Bash
streamlit run app.py
```
## ☁️ Cloud Deployment Protocol (Streamlit Community Cloud)

When syncing changes from your local staging terminal to the public cloud via GitHub, adhere strictly to these protection and deployment sequences:

1. Version Control Exposure Prevention
To verify your custom credentials are never exposed on public branches, add the secrets folder to your root .gitignore configuration profile:
```
Plaintext
.streamlit/secrets.toml
```
2. Configure Distributed Cloud Environment Variables
Because .toml configuration properties are banned from GitHub synchronization, you must copy your access infrastructure into the Cloud dashboard manually:

   1. Navigate to your Streamlit Community Cloud Console.

   2. Locate your active application link instance, click the overflow options ellipsis (...), and choose Settings.

   3. Select Secrets within the left-hand configuration panel.

   4. Paste your exact production token dictionary schema inside the console frame:
      ```
      Ini, TOML
      GEMINI_API_KEY = "AIzaSyYourActualGoogleAIStudioKeyHere"
      ```
   5. Click Save. Streamlit Cloud will parse this input automatically, resolve dependencies via requirements.txt, and initialize the live public environment.

## 📜 License

Distributed under the MIT License. See LICENSE for more information.
"""
```
Your production-ready README file has been generated and saved directly to your workspace. 
[file-tag: code-generated-file-0-1780334816264033818]

This comprehensive, data-science-focused file explicitly highlights your metrics, the machine learning architecture (`XGBoost`/`FLAML`), your engineering fail-safe design, and the **Gemini 2.5 JSON payload structure** that solved your previous crashing issues. 

Here is the exact code block you can copy and paste into your project's `README.md`:

```markdown
# 📊 DuoDevotion: AI-Powered Relationship Analytics Platform

DuoDevotion is an advanced, data-driven relationship analytics web application built with **Streamlit**. The platform bridges predictive machine learning modeling and modern generative AI to evaluate relationship health parameters, predict compatibility scores, analyze churn/ghosting risks, and deliver context-aware, tailored expert advisories in real time.

---

## 🚀 Key Architectural Features

* **Deterministic Machine Learning Execution**: Driven by a robust, optimized pipeline model (`final_pipeline.pkl`) engineered via **FLAML** and **XGBoost** to extract predictive insights from relationship dynamics.
* **Production-Grade Fail-Safe Fallbacks**: Features a custom-engineered mathematical engine designed to mimic the machine learning model array outputs seamlessly, providing complete platform resilience during detached binary state conditions.
* **Structured JSON Payload Handshakes**: Integrates with **Google Gemini 2.5 Flash** using strict programmatic JSON formatting constraints. This enforces reliable text parsing, completely mitigating presentation crashes and formatting errors.
* **Context-Driven Actionable Pro-Tips**: Dynamically segments relationship metrics to deliver tailored, hyper-focused behavioral improvements and optimization strategies.
* **Premium UX/UI Styling Layer**: Formatted entirely with embedded CSS styles, featuring glowing KPI cards, warning banners, and translucent glassmorphism text blocks for a premium presentation.

---

## 📊 Core Analytical Metrics

The application accepts and translates user interaction records into predictive parameters using four distinct focal points:

1. **User 1 Engagement & App Usage**: Quantifies baseline platform interactions, communication velocity, and platform retention variables (Scaled on a continuous 1–10 axis).
2. **User 2 Right Swipe Ratio**: Models matching selectivity thresholds, partner preference criteria, and selective profile interaction metrics.
3. **Compatibility Score (%)**: The target metric calculating overall profile structural alignment, interest convergence, and communication chemistry.
4. **Ghosting Risk (%)**: A predictive indicator estimating the probability of immediate engagement drop-off or conversational termination prior to milestones.

---

## 🛠️ Tech Stack & Dependencies

* **User Interface Engine**: [Streamlit](https://streamlit.io/) (Interactive sliders, state managers, custom CSS rendering)
* **Predictive ML Framework**: `scikit-learn`, `xgboost`
* **AutoML Hyperparameter Optimization**: `flaml` (Fast Lightweight AutoML)
* **Generative Intelligence Engine**: Official [Google Generative AI SDK](https://ai.google.dev/) (`gemini-2.5-flash`)
* **Serialization & Model Unpacking**: `joblib`
* **Data Core Processing**: `numpy`, `pandas`

---

## 📦 Project Directory Structure

```text
├── .streamlit/
│   └── secrets.toml          # Encrypted local variables (API keys - .gitignored)
├── app.py                     # Main application source and display architecture
├── final_pipeline.pkl         # Serialized production machine learning model
├── requirements.txt           # Cloud deployment environment package manifesto
└── README.md                  # System operation, technical specifications & guide
```
