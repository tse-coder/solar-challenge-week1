---
# 🌞 Solar Challenge Week 1

## 🧭 Overview
This repository is for **Week 1 of the Solar Challenge**.  
The goal is to set up a clean and reproducible Python development environment with version control and CI/CD best practices using GitHub Actions.

---

## 🧱 Folder Structure
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
│   └── README.md
├── tests/
│   ├── **init**.py
└── scripts/
├── **init**.py
└── README.md

````

---

## Environment Setup

### Clone the Repository
```bash
git clone https://github.com/<your-username>/solar-challenge-week1.git
cd solar-challenge-week1
````

### Create a Virtual Environment

Using **venv**:

```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```

Or using **conda**:

```bash
conda create -n solar-week1 python=3.10 -y
conda activate solar-week1
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Continuous Integration (CI)

GitHub Actions is configured to:

* Check out the repository
* Set up Python 3.10
* Install dependencies from `requirements.txt`
* Confirm Python installation and environment setup

You can find the workflow here:
 `.github/workflows/ci.yml`

The workflow runs automatically on:

* Every push to `main` or `setup-task`
* Every pull request targeting `main`

---

## Development Notes

* Use branches for all new features or fixes (e.g., `feature/data-cleaning`, `fix/ci-errors`).
* Commit often with clear messages, following conventional commit style:

  * `init: add .gitignore`
  * `chore: setup venv`
  * `ci: add GitHub Actions workflow`
* Open Pull Requests for code reviews and merging into `main`.

---
