


# Solar Challenge Week 1

## Overview
This repository contains Week 1 of the Solar Challenge.  
The goal is to set up a reproducible Python environment, perform data profiling and cleaning for solar datasets, and create visual analyses, including an interactive Streamlit dashboard.

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
---

If you want, I can also **add a short “how to reproduce each task” section** with exact commands for Task 1, Task 2, Task 3, and the dashboard — this makes your README completely step-by-step for reviewers.  

Do you want me to do that?
```
│   ├── **init**.py
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── tests/
│   ├── **init**.py
└── app/
├── **init**.py
├── main.py
└── utils.py

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

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Git and CI/CD

## Git and CI/CD

* Use feature branches for tasks (e.g., `setup-task`, `eda-countries`,`compare-countries`).
* Commit often with descriptive messages.
* GitHub Actions workflow (`.github/workflows/ci.yml`) installs dependencies and verifies Python environment on every push and pull request.

---

## Data Profiling, Cleaning, and EDA

### Notebooks

* `benin_eda.ipynb`, `togo_eda.ipynb`, `sierra_leone_eda.ipynb`
* `compare_countries.ipynb` for cross-country analysis

### Workflow

1. Load cleaned CSV for each country.
2. Perform summary statistics and missing value analysis.
3. Detect outliers using Z-scores and impute missing values.
4. Visualize time series, correlations, cleaning impact, distributions, temperature effects, and bubble charts.
5. Export cleaned CSVs to `data/<country>_clean.csv` (ignored by git).
6. Cross-country comparison includes boxplots, summary tables, statistical tests, and visual rankings.

---

## Notes

* All raw and cleaned CSVs are excluded from git via `.gitignore`.
* Notebooks include markdown cells describing findings and observations.
* All analyses and visualizations are reproducible from the virtual environment.

