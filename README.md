# 📈 PSX Market Intelligence & Portfolio Optimization System

An end-to-end financial data analytics project that transforms historical Pakistan Stock Exchange (PSX) data into actionable business insights using **Python** and **Power BI**.

This project demonstrates the complete data analytics lifecycle, including data collection, ETL, exploratory analysis, technical analysis, quantitative trading strategy evaluation, portfolio optimization, and interactive business intelligence dashboards.

---

## 📌 Project Overview

The Pakistan Stock Exchange (PSX) plays a significant role in Pakistan's financial ecosystem. Investors and analysts rely on historical market data to evaluate company performance, identify trading opportunities, and optimize investment portfolios.

This project simulates the workflow of a **Data Analyst** or **Quantitative Analyst** by integrating Python-based analytics with Power BI visualization to support data-driven investment decisions.

---

## 🎯 Project Objectives

- Collect historical stock market data from authentic financial sources.
- Build an automated ETL pipeline using Python.
- Perform descriptive and technical analysis of PSX-listed companies.
- Evaluate quantitative trading strategies using backtesting techniques.
- Apply Modern Portfolio Theory for portfolio optimization.
- Develop an interactive Power BI dashboard for financial decision support.

---

# 🏢 Companies Included

The project analyzes six major companies listed on the Pakistan Stock Exchange.

| Sector | Companies |
|---------|-----------|
| Banking | HBL, MCB |
| Cement | DGKC, Lucky Cement |
| Oil & Gas | OGDC, PPL |

---

# 📅 Time Period

**Historical Daily Data:** 2020 – 2025

---

# 📊 Data Sources

- Yahoo Finance (via `yfinance`)
- Investing.com (KSE-100 Index)
- Sector Classification Dataset

---

# ⚙️ Technologies Used

### Programming

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

### Business Intelligence

- Power BI
- DAX
- Power Query

### Financial Analysis

- Technical Indicators
- Moving Average Strategy
- RSI Strategy
- Monte Carlo Simulation
- Modern Portfolio Theory

---

# 🔄 Project Workflow

```text
Historical Data Collection
            │
            ▼
Data Cleaning & ETL
            │
            ▼
Feature Engineering
            │
            ▼
Descriptive Analytics
            │
            ▼
Technical Analysis
            │
            ▼
Trading Strategy Evaluation
            │
            ▼
Portfolio Optimization
            │
            ▼
Interactive Power BI Dashboard
```

---

# 🧹 ETL Pipeline

The project includes a fully automated ETL process developed in Python.

Major tasks include:

- Data collection using yfinance
- Date standardization
- Missing value handling
- Duplicate removal
- Data type conversion
- Company & sector merging
- KSE-100 integration
- Return calculations
  - Daily
  - Weekly
  - Monthly
  - Annual

The final cleaned dataset serves as the foundation for all analyses and dashboard visualizations.

---

# 📈 Dashboard Pages

## 1️⃣ Market Overview

Provides a macro-level view of the Pakistan Stock Exchange.

Features:

- KSE-100 Trend
- Market Volume Analysis
- Sector Performance
- Market KPIs

---

## 2️⃣ Company Analysis

Detailed technical analysis for individual companies.

Includes:

- Price Trend
- Candlestick Charts
- Moving Average (MA20 & MA50)
- RSI Indicator
- Volume Analysis

---

## 3️⃣ Trading Strategy Performance

Performance comparison of quantitative trading strategies.

Strategies evaluated:

- Moving Average Crossover
- RSI Mean Reversion
- Buy & Hold Benchmark

Performance Metrics:

- Total Return
- Sharpe Ratio
- Maximum Drawdown

---

## 4️⃣ Portfolio Optimization

Portfolio optimization using Modern Portfolio Theory.

Features:

- Monte Carlo Simulation
- Efficient Frontier
- Maximum Sharpe Portfolio
- Minimum Volatility Portfolio
- Asset Allocation Visualization

---

# 💡 Key Business Insights

- Banking stocks demonstrated relatively stable long-term performance.
- Cement and Oil & Gas sectors exhibited higher volatility.
- Moving Average strategy outperformed RSI strategy across most companies.
- RSI strategy performed better during sideways markets.
- Portfolio diversification significantly reduced investment risk.
- The Maximum Sharpe Portfolio provided the best risk-adjusted return.

---

# 📂 Repository Structure

```
PSX-Market-Intelligence/
│
├── README.md
├── LICENSE
│
├── notebooks/
│   ├── 01_Data_Collection.ipynb
│   ├── 02_ETL.ipynb
│   ├── 03_Descriptive_Analytics.ipynb
│   ├── 04_Technical_Indicators.ipynb
│   ├── 05_Trading_Strategy.ipynb
│   └── 06_Portfolio_Optimization.ipynb
│
├── data/
│   └── master_dataset.csv
│
├── powerbi/
│   └── PSX_Market_Intelligence.pbix
│
├── images/
│   ├── dashboard_1.png
│   ├── dashboard_2.png
│   ├── dashboard_3.png
│   └── dashboard_4.png
│
└── documentation/
    └── PSX_Market_Intelligence_Report.pdf
```

---

# 🚀 How to Use

1. Clone this repository.
2. Open the Jupyter notebooks to explore the data pipeline.
3. Review the processed dataset.
4. Open the Power BI (.pbix) file using Microsoft Power BI Desktop.
5. Interact with the dashboard pages to explore market trends, trading strategies, and portfolio optimization.

---

# 🔮 Future Improvements

- Real-time stock market integration
- Machine Learning-based stock price forecasting
- Additional technical indicators
- Macroeconomic factor integration
- Sector-wide portfolio optimization
- Automated dashboard refresh

---

# ⚠️ Disclaimer

This project was developed for **educational and portfolio purposes** using publicly available historical market data.

The analysis and trading strategies presented here **do not constitute financial or investment advice**.

---

# 👨‍💻 Author

**Kashif Hussain**

MS Data Science Student

Python | Power BI | Data Analytics | Machine Learning

If you found this project interesting, feel free to ⭐ the repository and connect with me on LinkedIn.
