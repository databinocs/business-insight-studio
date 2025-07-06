# 📊 Business Insight Studio

**Business Insight Studio** is a modular web app for quick data exploration and analysis powered by Streamlit.

This app allows users to:
- Upload and preview CSV files
- Segment data using KMeans clustering
- Forecast trends using Prophet
- Visualize KPIs by category or time
- Export processed data

---

## 🚀 Features

| Module        | Description                         |
|---------------|-------------------------------------|
| Upload        | Upload CSV files and preview them   |
| Segmentation  | Perform KMeans clustering           |
| Forecasting   | Forecast numeric values over time   |
| KPIs          | Visualize category & time-based metrics |
| Export        | Download processed dataset          |

---

## 🧱 Project Structure

business-insight-studio/
├── app.py
├── requirements.txt
├── .gitignore
├── LICENSE
├── README.md
└── modules/
├── upload.py
├── segmentation.py
├── forecasting.py
├── kpi.py
├── export.py


---

## ⚙️ Installation

```bash
git clone https://github.com/databinocs/business-insight-studio.git
cd business-insight-studio
python -m venv venv
.\venv\Scripts\activate  # On Windows
pip install -r requirements.txt
streamlit run app.py

> ⚠️ **Model note:** TAPAS performs best with tables under 50 rows and a limited number of columns. Larger inputs may reduce accuracy or fail.

This project is licensed under the MIT License.