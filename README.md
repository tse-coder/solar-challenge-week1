


# Solar Challenge Week 1

## Overview
This repository contains Week 1 of the Solar Challenge.  
The goal is to set up a reproducible Python environment, perform data profiling and cleaning for solar datasets, and create exploratory analyses.

---

## Folder Structure

```markdown

├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── requirements.txt
├── README.md
├── src/
├── notebooks/
│   ├── **init**.py
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   └── sierra_leone_eda.ipynb
├── tests/
│   ├── **init**.py

````

- `data/` contains cleaned CSVs for each country and is excluded from version control.

---

## Task 1: Git & Environment Setup

### Clone Repository
```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
````

### Create Virtual Environment

Using venv:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Or using conda:

```bash
conda create -n solar-week1 python=3.10 -y
conda activate solar-week1
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Git and CI/CD

* Feature branches are used for tasks (e.g., `setup-task`, `eda-benin`).
* Commit often with clear messages.
* GitHub Actions workflow (`.github/workflows/ci.yml`) installs dependencies and confirms environment setup on push or pull request.

---

## Task 2: Data Profiling, Cleaning & EDA

### Notebooks

* `benin_eda.ipynb`, `togo_eda.ipynb`, `sierra_leone_eda.ipynb`

### Workflow

1. Load each country’s CSV dataset.
2. Summary statistics & missing value analysis:

   * `df.describe()` for numeric columns
   * Identify columns with >5% missing values
3. Outlier detection & cleaning:

   * Compute Z-scores for `GHI`, `DNI`, `DHI`, `ModA`, `ModB`, `WS`, `WSgust`
   * Flag rows with `|Z| > 3`
   * Impute missing values with median
   * Export cleaned CSVs to `data/<country>_clean.csv`
4. Exploratory Data Analysis:

   * Time series plots (`GHI`, `DNI`, `DHI`, `Tamb`)
   * Cleaning impact analysis (ModA/ModB pre/post cleaning)
   * Correlation & scatter plots
   * Wind and distribution analysis
   * Temperature and relative humidity relationships
   * Bubble charts (`GHI` vs. `Tamb`, size = `RH` or `BP`)
5. Documentation:

   * Markdown cells explaining findings
   * Code cells for loading, cleaning, and visualizations
   * Cleaned CSVs prepared for cross-country analysis

```