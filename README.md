


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
│   ├── **init**.py
│   ├── benin_eda.ipynb
│   ├── togo_eda.ipynb
│   ├── sierra_leone_eda.ipynb
│   └── compare_countries.ipynb
├── tests/
│   ├── **init**.py
├── app/
|   ├── **init**.py
|   ├── main.py
|   └── utils.py
└──screenshots/
    ├── 1.png
    ├── 2.png
    ├── 3.png
    └── 4.png
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
7. A streamlit dashboard to visualize data interactively

---
## streamlit dashboard

# Overview

A fully interactive dashboard was implemented to visualize solar data across Benin, Sierra Leone, and Togo.

- Select countries via multiselect widget.
- Choose metrics (GHI, DNI, DHI, Tamb) for visualization.
- View boxplots, correlation heatmaps, bubble charts, and summary statistics.
- Clean and professional layout suitable for screenshots and presentations.

Run Locally
```bash
streamlit run app/main.py
```

Open in Browser at [http://localhost:8501](http://localhost:8501)

## Notes

* All raw and cleaned CSVs are excluded from git via `.gitignore`.
* Notebooks include markdown cells describing findings and observations.
* All analyses and visualizations are reproducible from the virtual environment.

## screenshots

![Dashboard Screenshot 1](https://raw.githubusercontent.com/tse-coder/solar-challenge-week1/main/screenshots/1.png)
![Dashboard Screenshot 2](https://raw.githubusercontent.com/tse-coder/solar-challenge-week1/main/screenshots/2.png)
![Dashboard Screenshot 3](https://raw.githubusercontent.com/tse-coder/solar-challenge-week1/main/screenshots/3.png)
![Dashboard Screenshot 4](https://raw.githubusercontent.com/tse-coder/solar-challenge-week1/main/screenshots/4.png)

