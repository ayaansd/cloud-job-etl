# Cloud Job ETL — GCP BigQuery + Airflow  

🚀 **Goal**: Build an end-to-end **ETL pipeline** that ingests 200K+ job postings into **BigQuery**, applies 40+ optimized SQL transformations, and powers **Power BI dashboards** for real-time analytics.

## 🛠️ Tools & Tech
- **Airflow**: DAG orchestration
- **Google Cloud**: GCS + BigQuery
- **SQL**: dbt-style transformations
- **DuckDB (local demo)**
- **Power BI**: dashboards

## 📂 Architecture
1. **Extract** → Python operator downloads CSV → GCS.
2. **Load** → BigQueryLoadJobOperator → raw table.
3. **Transform** → SQL scripts (40+ transformations).
4. **Serve** → BI dashboards (DirectQuery to BigQuery).

## 🚀 Quickstart (local demo)
```bash
pip install -r requirements.txt
python dags/dev_local_runner.py


📊 Deliverables

dags/job_etl.py — Airflow DAG skeleton.

sql/transformations/*.sql — transformation scripts.

data/sample_jobs.csv — synthetic dataset.

Power BI dashboards (connect to BQ).


---

### **Batch ETL Pipeline — PySpark & Hive**
```markdown
# Batch ETL Pipeline — PySpark + Hive

⚡ **Goal**: Process 5M+ log records, clean & deduplicate, and aggregate metrics into **Hive tables** for BI.

## 🛠️ Tools & Tech
- **PySpark**: batch ETL
- **Hive**: warehouse tables
- **Parquet/ORC**: optimized storage

## 🚀 Quickstart
```bash
pip install -r requirements.txt
python etl_spark.py

xpected output:

✅ Tables created in etl.duckdb

✅ Aggregated top companies (agg_top_companies)

📊 Example Queries
-- top hiring companies
select * from agg_top_companies limit 10;

-- avg salary by role bucket
select role_bucket, round(avg(salary_mid)) avg_salary
from fact_jobs
group by role_bucket;

📈 Deliverables

Airflow DAG (dags/job_etl.py) — GCP-ready skeleton

SQL scripts (sql/transformations/) — 10 included, expandable to 40+

Synthetic dataset (data/sample_jobs.csv) — 1,000 job postings

DuckDB local runner (dags/dev_local_runner.py) — run pipeline locally

Power BI dashboard (not included — connect to BigQuery fact tables)

🔜 Roadmap

 Add GCS & BigQuery operators to DAG for production

 Expand SQL scripts → 40+ transformations (salary bands, geo rollups)

 Deploy Airflow DAG to Cloud Composer

 Connect Power BI dashboards to BigQuery (DirectQuery or refresh)

📜 License

MIT — free to use and adapt.
