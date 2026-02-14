# End-to-End Market Data Pipeline

## 🚀 Overview
An automated ETL pipeline that ingests real-time market data into Google BigQuery, utilizing Python for extraction and SQL for analytical modeling.

## 🛠 Tech Stack
- **Language:** Python 3.9+
- **Cloud:** Google BigQuery
- **Libraries:** Pandas, Google Cloud SDK, Requests
- **Environment:** Linux VM / Crontab

## 🏗 Workflow
1. **Extraction:** Python script hits external REST API.
2. **Staging:** Data is loaded into a 'Raw' BigQuery table with schema enforcement.
3. **Transformation:** SQL scripts aggregate raw data into 'Gold' business-ready tables.
4. **Monitoring:** Job history and count validation scripts ensure data parity.

## 📈 Key Accomplishments
- Implemented **schema enforcement** to prevent downstream data corruption.
- Optimized loading by using **parquet-based** ingestion for BigQuery.