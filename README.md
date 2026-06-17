Workshop Viewing Time Analysis
Role: Data Analyst
Company: NotGPT (professional data skills training)
Domain: A/B testing, educational engagement analytics

Overview
NotGPT recently ran a training workshop with a controlled A/B test. One group received a redesigned slide deck with significantly reduced text (avg. 15 words/slide vs. the original 50 words/slide), while the control group experienced no changes. Both groups' viewing times (in minutes) were recorded.

This project cleans, explores, and reports on that data to determine whether the slide redesign had a meaningful effect on how long employees engaged with the workshop.

Project Structure
viewing-time-analysis/
├── data/                  # Raw viewing time data for both groups
├── cleaner.py             # Reusable data cleaning functions
├── explore.ipynb          # EDA, statistics, visualizations, and written findings
└── README.md
How It Works
The analysis is split across two components:

cleaner.py
Contains reusable functions for loading and cleaning the raw viewing time data. Each function is documented and designed to be imported into the notebook.

explore.ipynb
A Jupyter notebook with three parts:

Clean — Import and apply functions from cleaner.py to prepare both groups' data for analysis.
Explore — Compute descriptive statistics and examine distributions programmatically. Compare control vs. treatment group metrics side by side.
Report — Present findings in plain language, supported by one effective data visualization that communicates whether the treatment had a meaningful impact on viewing time.
Running the Project
Open explore.ipynb in Jupyter or VS Code.
Run all cells from top to bottom.
Findings and the visualization are rendered inline within the notebook.
A/B Test Design
Control Group	Treatment Group
Slide format	Original	Redesigned
Avg. words/slide	50	15
Metric tracked	Viewing time (minutes)	Viewing time (minutes)
Skills Practiced
File I/O — Load raw data files into Python for processing.
Data cleaning — Write modular, reusable functions to handle messy or invalid records.
Descriptive statistics — Summarize and compare both groups quantitatively.
Data visualization — Produce one clear, well-labeled chart that supports the findings.
Reporting — Communicate analytical conclusions in plain language within the notebook.
Notes
The cleaning logic lives entirely in cleaner.py to keep the notebook focused on analysis and reporting.
The visualization is chosen to most clearly illustrate the difference (or lack thereof) between the two groups.
All findings are written up in markdown cells within explore.ipynb — the notebook is the deliverable.
