# 📊 Credit Risk Prediction System – Home Credit Project

<div align="center">

![Credit Risk](https://img.shields.io/badge/Credit%20Risk-Analytics-2563eb?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![Statistics](https://img.shields.io/badge/Statistical%20ML-Explainable-16a34a?style=for-the-badge)
![Finance](https://img.shields.io/badge/Finance-Regulator%20Friendly-7c3aed?style=for-the-badge)

*A statistically validated and interpretable credit risk prediction framework*

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Results](#-results--analysis) • [Contributing](#-contributing)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Installation](#-installation)
- [Usage](#-usage)
- [Results & Analysis](#-results--analysis)
- [Statistical Validation](#-statistical-validation)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Overview

This project presents a **hybrid and interpretable credit risk prediction system** built using the **Home Credit Default Risk dataset**. The goal is to accurately predict borrower default risk while maintaining **statistical rigor, transparency, and auditability**, which are essential in regulated financial environments.

Unlike black-box machine learning approaches, this system integrates **classical statistical techniques** with machine learning to provide **explainable and reliable credit risk scores**.

---

## ✨ Features

### 📉 Dimensionality Reduction
- Principal Component Analysis (PCA) to handle high-dimensional financial data
- Reduces 100+ correlated features to 23 orthogonal components
- Retains approximately 90% of total variance

### 🧩 Borrower Segmentation
- Hierarchical (Agglomerative) Clustering on PCA-transformed data
- Identifies meaningful borrower groups with shared risk characteristics
- Dendrogram-based cluster selection

### 📊 Statistical Validation
- One-way ANOVA to validate cluster separability
- Cronbach’s Alpha to assess feature reliability
- Ensures statistical significance and internal consistency

### 📐 Interpretable Risk Models
- Linear Discriminant Analysis (LDA)
- Quadratic Discriminant Analysis (QDA)
- Logistic Regression as a baseline comparison

### 📈 Bayesian Risk Estimation
- Gaussian Naïve Bayes for probabilistic default prediction
- Outputs posterior probability of default
- Enables threshold-based risk decisions

---

## 🛠 Technology Stack

### Core Technologies
- **Python** – Primary programming language
- **NumPy & Pandas** – Data manipulation and analysis
- **Scikit-Learn** – PCA, clustering, and classification models
- **SciPy** – Statistical testing (ANOVA)
- **Matplotlib / Seaborn** – Data visualization

### Development Environment
- Jupyter Notebook / Google Colab
- Conda / pip for dependency management

---

## 📁 Project Structure

```text
.
├── Team_4_Code.ipynb          # Main project notebook
├── Dataset/                  # Dataset directory (excluded from Git)
│   ├── application_data.csv
│   └── previous_application.csv
├── requirements.txt          # pip dependencies
├── environment.yml           # conda environment (optional)
├── README.md                 # Project documentation
├── LICENSE                   # License file
└── .gitignore                # Dataset and environment exclusions
```
---

## 🗂 Dataset

- **Source:** Home Credit Default Risk Dataset
- **Records:** ~300,000 loan applicants
- **Features:** 100+ demographic, financial, and credit-history attributes
- **Target Variable:** Loan Default (0 = Non-default, 1 = Default)

### Data Handling
- The dataset is excluded from the repository due to size constraints
- Place the dataset files inside the `Dataset/` folder:
  - application_data.csv
  - previous_application.csv

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Jupyter Notebook or Anaconda

### Setup using pip

```bash
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
```

---

## ✅ Usage

1. Open `Team_4_Code.ipynb` in Jupyter or Colab.
2. Place the required CSVs inside `Dataset/`.
3. Run each notebook cell in order; key sections:
   - Data preprocessing and feature engineering
   - PCA and clustering
   - Model training and validation
   - Results visualization and statistical tests

---

## 🧾 Results & Analysis

Summarize key performance metrics, e.g.:
- AUC-ROC, Precision/Recall, and Calibration curves
- ANOVA p-values for cluster separability
- Cronbach’s Alpha values for reliability

Include representative plots and a short narrative about model performance and fairness checks.

---

## 📊 Statistical Validation

Include a step-by-step description of the statistical tests applied, thresholds for significance, and why those tests are appropriate for regulatory scrutiny.

---

## 🔭 Future Scope

- Add cross-validation and time-aware validation for temporal stability
- Explore ensemble methods with interpretability constraints
- Implement model monitoring and drift detection

---

## 🤝 Contributing

Thanks for your interest in contributing! Please follow these steps:

1. Fork the repository and create a feature branch from `main`.
2. Make small, focused commits and include tests for changes.
3. Run the test suite and ensure linting passes (if configured).
4. Open a pull request describing the change and linking any relevant issues.

---

## 📄 License

This project is released under the MIT License - see `LICENSE`.
