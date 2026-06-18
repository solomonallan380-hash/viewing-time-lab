# 📊 Workshop Viewing Time — A/B Testing Analysis

**Domain:** A/B Testing · Educational Engagement Analytics  
**Tools:** Python · Pandas · Matplotlib · Jupyter Notebook  
**GitHub:** [solomonallan380-hash/viewing-time-lab](https://github.com/solomonallan380-hash/viewing-time-lab)

---

## Overview

This project analyzes whether a redesigned slide format — with significantly reduced text — had a measurable effect on how long employees engaged with a training workshop.

**NotGPT**, a professional data skills training company, ran a controlled A/B test:

| | Control Group | Treatment Group |
|---|---|---|
| Slide format | Original | Redesigned |
| Avg. words per slide | 50 | 15 |
| Sample size | 500 employees | 500 employees |
| Metric tracked | Viewing time (minutes) | Viewing time (minutes) |

---

## Key Findings

- **The treatment group watched longer.** Mean viewing time was **16.80 minutes** for the treatment group vs. **12.45 minutes** for the control group — a difference of ~4.3 minutes per session.
- **The treatment group was more consistent.** Standard deviation was **2.09 minutes** (treatment) vs. **3.26 minutes** (control), indicating the redesigned slides produced more uniform engagement.
- **Conclusion:** Reducing slide word count from 50 to 15 words per slide appears to increase and stabilize viewer engagement.

---

## Project Structure

```
viewing-time-lab/
├── data/
│   ├── control.txt        # 500 viewing time recordings — original slides
│   └── treatment.txt      # 500 viewing time recordings — redesigned slides
├── cleaner.py             # Reusable data cleaning module
├── explore.ipynb          # Full analysis: cleaning, stats, visualization, findings
└── README.md
```

---

## How It Works

### `cleaner.py`
A reusable module containing the `clean_data()` function. It reads raw text data, strips headers, typecasts string values to floats, and returns a cleaned list along with a count of removed records. Designed to be imported directly into the notebook.

### `explore.ipynb`
A Jupyter notebook organized into three parts:

1. **Clean** — Loads both data files using file I/O and applies `clean_data()` to prepare each group for analysis.
2. **Explore** — Computes descriptive statistics (mean, standard deviation, outlier detection using ±2 SD) and compares both groups side by side.
3. **Report** — Presents findings in plain language, supported by an overlapping histogram that visualizes the distribution and mean difference between groups.

---

## Running the Project

```bash
# Clone the repo
git clone https://github.com/solomonallan380-hash/viewing-time-lab.git
cd viewing-time-lab

# Open the notebook
jupyter notebook explore.ipynb
# or in VS Code:
code explore.ipynb
```

Run all cells top to bottom. All findings and visualizations render inline.

---

## Skills Demonstrated

| Skill | Application |
|---|---|
| File I/O | Load raw `.txt` data files into Python |
| Data Cleaning | Modular `clean_data()` function handles headers, type errors, and invalid records |
| Descriptive Statistics | Mean, standard deviation, and outlier detection via the `statistics` module |
| Data Visualization | Overlapping histogram (Matplotlib) comparing both group distributions |
| A/B Test Analysis | Interpret treatment vs. control outcomes and draw data-backed conclusions |
| Technical Reporting | Written findings in markdown, backed by discrete numbers |
