# 🎧 Chinook Hive Warehouse

A full ETL pipeline project designed for practicing data engineering skills. The project extracts music store data from the Chinook SQL Server database, transforms it using Python, stages it as CSV, and loads it into Hive for analysis.

---

## 🔁 ETL Pipeline Overview

```
SQL Server (Chinook)
    │
    └──► Python ETL
            │
            ├─ Extract raw data via pyodbc / SQLAlchemy
            ├─ Transform with business logic (fact & dimension tables)
            └─ Save as CSV Stage files
                │
                └──► Load into Hive (data warehouse)
                          │
                          └──► Analyze with Python + ML (scikit-learn, matplotlib)
```

---

## 🧱 1. Data Source

- **Chinook Database** (SQL Server)  
- Tables used:
  - `Customer`, `Invoice`, `InvoiceLine`  
  - `Artist`, `Album`, `Track`, `Genre`  
- Goal:
  - Analyze customer behavior, revenue trends, top artists/genres.

---

## 🔧 2. Data Processing & Staging

- **Tools:** Python, Pandas, pyodbc / SQLAlchemy  
- **Steps:**
  - Define business processes: purchase behavior, music sales  
  - Build star schema:
    - Dimension tables: `dim_customer`, `dim_artist`, `dim_album`, `dim_track`, `dim_genre`  
    - Fact table: `fact_sales`
  - Stage data as `.csv` files for manual inspection and Hive loading

---

## 🐝 3. Hive Data Warehouse

- **Tools:** Apache Hive, PyHive (or Beeline)  
- **Steps:**
  - Create Hive schema (star schema format)  
  - Define tables for each dimension and fact  
  - Load CSV stage files into Hive:
    - Using `LOAD DATA INPATH` or Python + PyHive `INSERT INTO`

---

## 📊 4. Data Analysis

- **Tools:** scikit-learn, matplotlib, seaborn  
- **Possible Analysis:**
  - 📌 Customer segmentation (clustering by revenue, location, frequency)  
  - 📈 Revenue forecasting (monthly/quarterly using Linear Regression / ARIMA)  
  - 📊 Top artists and genres  
  - 📅 Time-based sales analysis

---

## ⚙️ Technologies Used

- SQL Server (Chinook DB)  
- Python (Pandas, SQLAlchemy, PyHive)  
- Hive + HiveServer2 + Metastore (MariaDB)  
- Docker Compose  
- Scikit-learn, Matplotlib, Seaborn

---

## 📂 Project Structure

```
├── chinook_etl/
│   ├── extract/         # SQL Server connectors and queries
│   ├── transform/       # Business logic and data modeling
│   └── stage/           # CSV outputs (dim/fact tables)
├── hive/
│   ├── conf/            # hive-site.xml and table schemas
│   ├── hiveserver2/     # Custom Dockerfile with telnet, ping, etc.
│   └── docker-compose.yaml
├── analysis/            # Python notebooks or scripts for ML
├── README.md
└── .env
```

---

## 🚀 Getting Started

1. **Start the Hive + Metastore environment:**

```bash
cd hive
docker-compose up -d
```

2. **Run ETL pipeline using Python:**

```bash
cd chinook_etl
python main.py
```

3. **Analyze data in Hive using Beeline or PyHive**

---

## 📌 Author

Made with ❤️ by **[hungfnguyen]** as a portfolio project for Data Engineer internships.
