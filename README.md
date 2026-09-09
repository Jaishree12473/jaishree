# 🌾 Seasonal Agriculture Performance Analysis

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-1.24+-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.12+-388E3C?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

An in-depth Exploratory Data Analysis (EDA) and econometric assessment of seasonal agricultural performance across major Indian states. This study analyzes 4,000 agricultural observations across 28 agro-climatic, resource utilization, and financial metrics to evaluate crop profitability, yield efficiency, disease vulnerability, and irrigation efficacy.

---

## 📌 Table of Contents
- [Project Overview](#-project-overview)
- [Dataset Description](#-dataset-description)
- [Key Insights & Findings](#-key-insights--findings)
- [Repository Structure](#-repository-structure)
- [Installation & Getting Started](#-installation--getting-started)
- [How to Run](#-how-to-run)
- [Generated Visualizations](#-generated-visualizations)
- [Limitations & Recommendations](#-limitations--recommendations)

---

## 📖 Project Overview

Agriculture in India is heavily dependent on seasonal cycles, irrigation management, and regional climatic factors. This project provides an evidence-based evaluation of agricultural outcomes by:
1. **Cleaning & Preprocessing**: Handling missing values via median/mode imputation, removing duplicates, and detecting IQR outliers.
2. **Exploratory Data Analysis**: Univariate, bivariate, and multivariate distribution analysis across seasonal cohorts (*Kharif*, *Rabi*, *Zaid*).
3. **Resource Efficiency**: Assessing water usage efficiency across various irrigation methods (*Drip*, *Sprinkler*, *Flood*, *Rainfed*).
4. **Economic & Crop Evaluation**: Ranking crop profitability and analyzing cost-to-revenue ratios.
5. **Correlation Discovery**: Identifying primary drivers of agricultural yield and financial return.

---

## 📊 Dataset Description

The dataset (`seasonal_agriculture_performance_dataset.csv`) contains **4,000 records** and **28 attributes**:

| Category | Features Included |
|---|---|
| **Identifiers & Geography** | `Farm_ID`, `State`, `District` |
| **Agricultural Context** | `Crop`, `Season`, `Farm_Area_Hectares` |
| **Agro-Climatic Factors** | `Rainfall_mm`, `Avg_Temperature_C`, `Humidity_pct`, `Sunlight_Hours_Day` |
| **Soil & Fertilizer Inputs** | `Soil_pH`, `Soil_Moisture_pct`, `Nitrogen_kg_ha`, `Phosphorus_kg_ha`, `Potassium_kg_ha`, `Fertilizer_kg_ha`, `Pesticide_Litre_ha`, `Seed_Quality_Score` |
| **Irrigation & Water Metrics** | `Irrigation_Method`, `Water_Used_m3`, `Water_Efficiency_t_per_1000m3` |
| **Yield & Production** | `Yield_Tonnes_Ha`, `Production_Tonnes` |
| **Economics & Risk** | `Market_Price_INR_Tonne`, `Total_Cost_INR`, `Revenue_INR`, `Profit_INR`, `Disease_Pest_Risk_pct` |

---

## 💡 Key Insights & Findings

1. **Seasonal Superiority**:
   - **Kharif** yielded the highest average profit (**₹1,78,914.65**) and highest average yield (**5.63 t/ha**), though it also observed higher pest/disease risk due to high humidity and monsoon rainfall.
   - **Zaid** reported lower profitability (**-₹24,804.82**) due to intense water requirements and higher irrigation costs during dry summer conditions.

2. **Crop Profitability**:
   - **Sugarcane** and **Chilli** demonstrated the highest net profitability among crops (**₹8,17,187.99** and **₹7,50,878.34** respectively).
   - Staple cereals like **Wheat** and **Rice** showed razor-thin or negative operating margins in the absence of subsidized input structures.

3. **Irrigation Efficiency**:
   - **Drip Irrigation** yielded the highest average profit (**₹2,19,626.00**) and superior water productivity compared to traditional **Flood Irrigation**.
   - **Flood Irrigation** consumed the highest water volumes (**8,026.47 m³**) with the lowest water efficiency (**3.44 t/1000 m³**).

4. **Regional Leaders**:
   - **Punjab** (₹1,36,025.64) and **Maharashtra** (₹1,35,428.86) led average state-level agricultural profitability.

5. **Correlation Drivers**:
   - `Water_Efficiency_t_per_1000m3` exhibited the strongest positive correlation with `Yield_Tonnes_Ha`.
   - `Revenue_INR` served as the primary linear determinant of `Profit_INR`.

---

## 📁 Repository Structure

```text
JAISSHREEPROJECT/
├── JAISSHREEPROJECT.ipynb               # Full interactive Jupyter Notebook
├── JAISSHREEPROJECT.html                # Compiled visual HTML report (browser-ready)
├── run_project.py                       # Standalone runnable Python pipeline
├── seasonal_agriculture_performance_dataset.csv  # Project dataset
├── start_jupyter.bat                    # One-click launcher for Jupyter Notebook
├── requirements.txt                     # Python package dependencies
├── .gitignore                           # Git ignore rules
├── README.md                            # Project documentation
└── output_plots/                        # 27 generated high-resolution visualizations
    ├── figure_01.png ... figure_27.png
```

---

## ⚙️ Installation & Getting Started

### Prerequisites
- Python 3.10+ or Python 3.11
- Git installed on your local machine

### 1. Clone the Repository
```bash
git clone https://github.com/Jaishree12473/seasonal_agriculture_performance.git
cd seasonal_agriculture_performance
```

### 2. Set Up Virtual Environment & Dependencies
```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install requirements
pip install -r requirements.txt
```

---

## 🚀 How to Run

### Option A: Run Standalone Python Script
Executes all calculations, displays summaries, and regenerates all figures in `output_plots/`:
```bash
python run_project.py
```

### Option B: Interactive Jupyter Notebook
```bash
jupyter notebook JAISSHREEPROJECT.ipynb
```
*(On Windows, you can also simply double-click `start_jupyter.bat`)*

### Option C: View Pre-compiled HTML Report
Open [`JAISSHREEPROJECT.html`](JAISSHREEPROJECT.html) in any web browser to view all tables and 27 generated charts without executing code.

---

## 📈 Generated Visualizations

The pipeline generates 27 visualizations saved in `output_plots/`:
- **Outlier Boxplots**: For Yield, Profit, Revenue, Rainfall, Water Usage, and Disease Risk.
- **Univariate Distributions**: Yield, Rainfall, and Profit histograms with KDE curves.
- **Bivariate Comparisons**: Season vs. Yield, Season vs. Profit, Rainfall vs. Yield scatter plots.
- **Cross-Tabulation Heatmaps**: Crop vs. Season Average Yield pivot matrices.
- **Correlation Matrix**: High-resolution heatmap of all numerical features.
- **Resource Analytics**: Water efficiency by irrigation method and regional profit bar charts.

---

## 📝 Limitations & Recommendations

- **Missing Values**: Imputed using median (numeric) and mode (categorical) to preserve central tendencies.
- **Correlation vs. Causation**: Strong correlations highlight associations rather than direct causal drivers.
- **Policy Recommendations**:
  - Incentivize modern micro-irrigation systems (drip/sprinkler) to reduce flood irrigation water waste.
  - Prioritize pest monitoring during high-humidity Kharif cycles.
  - Implement crop rotation with cash crops (Sugarcane, Chilli) to offset low-margin cereal yields.

---
*Created as part of the Major Project for Seasonal Agriculture Performance Analysis.*
