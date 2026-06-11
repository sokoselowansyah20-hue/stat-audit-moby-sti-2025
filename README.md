# Statistical Audit of Pandas Open-Source Repository

## Overview

This project presents a statistical audit of the Pandas open-source repository hosted on GitHub. The audit applies statistical inference and computational probability techniques to examine repository activity, contributor behavior, and overall project health.

Using data collected from the GitHub API, the analysis focuses on commits, pull requests, issues, and contributor participation. The project demonstrates how statistical methods can be used to evaluate the sustainability and development patterns of a large-scale open-source software project.

## Repository Audited

**Project:** Pandas

**GitHub Repository:** https://github.com/pandas-dev/pandas

## Objectives

The main objectives of this audit are:

* Explore repository activity through Exploratory Data Analysis (EDA).
* Estimate important repository metrics using statistical estimation methods.
* Construct confidence intervals for selected project indicators.
* Perform hypothesis testing on contribution and development patterns.
* Apply computational probability methods such as Monte Carlo Simulation, Bloom Filter, and Markov Chain Monte Carlo (MCMC).
* Assess the statistical health and maintenance activity of the Pandas project.

## Methods Used

### Exploratory Data Analysis (EDA)

* Commit trend analysis
* Pull request activity analysis
* Issue distribution analysis
* Contributor activity analysis

### Parameter Estimation

* Maximum Likelihood Estimation (MLE)
* Bayesian Estimation using Beta Posterior

### Confidence Intervals

* 90% Confidence Interval
* 95% Confidence Interval
* 99% Confidence Interval

### Hypothesis Testing

* One-Sample t-Test
* Proportion Test

### Computational Probability

* Monte Carlo Simulation
* Bloom Filter
* Markov Chain Monte Carlo (MCMC)

## Project Structure

```text
stat-audit-pandas-sti-2025/

├── data/
│   ├── raw/
│   └── clean/
│
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_parameter_estimation.ipynb
│   ├── 04_confidence_interval.ipynb
│   ├── 05_hypothesis_testing.ipynb
│   └── 06_simulation.ipynb
│
├── src/
│   ├── github_api.py
│   ├── preprocessing.py
│   ├── estimation.py
│   ├── ci.py
│   ├── hypothesis.py
│   └── simulation.py
│
├── presentation/
│   ├── Presentation_Slides.pptx
│   └── video_link.txt
│
├── report/
│   └── Statistical_Health_Report.pdf
│
├── README.md
├── AI_USAGE_LOG.md
├── requirements.txt
├── .gitignore
└── LICENSE
```


### Folder Description

| Folder/File      | Description                                               |
| ---------------- | --------------------------------------------------------- |
| data/raw         | Raw data collected from GitHub API                        |
| data/clean       | Cleaned datasets ready for analysis                       |
| notebooks        | Jupyter notebooks containing statistical analyses         |
| src              | Python source code and utility modules                    |
| presentation     | Presentation slides and video materials                   |
| report           | Statistical Health Report and final written documentation |
| README.md        | Project documentation                                     |
| AI_USAGE_LOG.md  | Documentation of AI-assisted development                  |
| requirements.txt | Required Python dependencies                              |
| .gitignore       | Git ignore configuration                                  |
| LICENSE          | Repository license                                        |

## Data Source

All data used in this project were collected from the GitHub REST API and include:

* Commits
* Pull Requests
* Issues
* Contributors

## Team Members

| No | Name           | NIM | Role                                         |
| -- | -------------- | --- | -------------------------------------------- |
| 1  | Soko Selowansyah | 1519625063 | Team Leader & Data Collection                |
| 2  | Anggota 2 | NIM | Exploratory Data Analysis (EDA)              |
| 3  | Anggota 3 | NIM | Parameter Estimation & Confidence Interval   |
| 4  | Anggota 4 | NIM | Hypothesis Testing                           |
| 5  | Anggota 5 | NIM | Simulation (Monte Carlo, Bloom Filter, MCMC) |

## AI Usage

Artificial Intelligence tools were used solely for coding assistance, debugging, and documentation support. All statistical interpretations, hypotheses, discussions, and conclusions were developed and validated by the project team.

For detailed information regarding AI usage, please refer to **AI_USAGE_LOG.md**.

## Academic Purpose

This repository was created exclusively for academic purposes as part of the Statistical Audit Final Project.
