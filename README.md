# 🏠 House Price Prediction using Machine Learning & DVC

## 📌 Project Overview

This project implements an end-to-end **Machine Learning pipeline** to predict house prices based on various property features such as size, number of rooms, and other attributes.

The project follows best practices including:

* Data Version Control (DVC)
* Reproducible ML pipelines
* Experiment tracking
* Model comparison

---

## 📂 Project Structure

```
Assignment-1/
│
├── src/                 # Source code
│   ├── prepare.py       # Data cleaning & splitting
│   ├── transform.py     # Feature engineering & scaling
│   ├── train.py         # Model training
│   └── evaluate.py      # Model evaluation & plots
│
├── data/                # Dataset (tracked using DVC)
│   ├── raw.csv
│   ├── processed/
│   └── features/
│
├── models/              # Trained models (DVC tracked)
│   └── model.pkl
│
├── reports/             # Metrics & visualizations
│   ├── metrics.json
│   └── plot.png
│
├── dvc.yaml             # DVC pipeline definition
├── dvc.lock             # Pipeline lock file
├── params.yaml          # Parameters configuration
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## 📊 Dataset

* Source: https://www.kaggle.com/datasets/harlfoxem/housesalesprediction
* The dataset contains housing features such as:

  * Square footage
  * Number of bedrooms & bathrooms
  * Location-based attributes
  * Price (target variable)

---

## ⚙️ Pipeline Stages (DVC)

The pipeline is defined in `dvc.yaml` with the following stages:

### 1. Prepare

* Loads raw dataset
* Cleans data
* Splits into **90% train / 10% test**

### 2. Transform

* Removes non-numeric features
* Applies feature scaling
* Outputs processed feature datasets

### 3. Train

* Trains regression model (Linear Regression / XGBoost)
* Saves trained model

### 4. Evaluate

* Evaluates model performance using MSE
* Generates:

  * `metrics.json`
  * `plot.png` (Actual vs Predicted)

---

## 🚀 How to Run the Project

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd Assignment-1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run DVC Pipeline

```bash
dvc repro
```

---

## 📈 Metrics & Results

View metrics:

```bash
dvc metrics show
```

Compare experiments:

```bash
dvc metrics diff
```

View plots:

```bash
dvc plots show
```

---

## 🤖 Models Used

### Baseline Model

* Linear Regression

### Advanced Model

* XGBoost Regressor

The models are compared based on Mean Squared Error (MSE).

---

## 🔁 Reproducibility

This project ensures full reproducibility:

* Dataset tracked using DVC
* Pipeline reproducible using:

```bash
dvc repro
```

* Parameter changes trigger selective pipeline execution

---

## 🧠 Key Learnings

* Building modular ML pipelines
* Using DVC for experiment tracking
* Handling real-world datasets
* Feature engineering & preprocessing
* Model comparison and evaluation

---

## 📌 Submission Requirements Covered

✅ DVC pipeline implementation
✅ Dataset versioning
✅ Multiple model experimentation
✅ Metrics tracking
✅ Visualization (plots)
✅ Git version control

---

## 🎥 Additional Deliverables

* 📄 Experiment Report (PDF)
* 🎬 Screencast Video explaining the workflow

---

## ⚠️ Note

All AI-assisted code includes:

```
# Assisted by ChatGPT
```

---

## 👤 Author

**Rahail Mohammed**
AI-ML Assignment Submission
