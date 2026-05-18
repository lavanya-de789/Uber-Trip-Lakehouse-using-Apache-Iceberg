# Uber Lakehouse using Apache Iceberg

## Overview

This project demonstrates an end-to-end modern Data Lakehouse architecture using Apache Iceberg, PySpark, Airflow, Docker, and S3-compatible object storage. The platform processes Uber trip datasets through Bronze, Silver, and Gold layers while leveraging Iceberg features such as schema evolution, ACID transactions, metadata-driven partition management, and time-travel capabilities.

The goal is to simulate a production-style data engineering workflow that ingests raw trip data, applies transformations, and generates analytics-ready datasets for reporting and business insights.

---

## Architecture

```text
Raw Uber Trip Data
        ↓
Bronze Layer
(Raw Ingestion)

        ↓
Silver Layer
(Cleaned + Transformed)

        ↓
Gold Layer
(Business Analytics)

        ↓
Query Layer
(Spark SQL / Trino)
```

---

## Repository Structure

```text
uber-lakehouse-iceberg/

├── docker-compose.yml
├── requirements.txt
├── README.md

├── data/
│    ├── raw/
│    ├── bronze/
│    ├── silver/
│    └── gold/

├── spark/
│    ├── ingest.py
│    ├── transform.py
│    └── analytics.py

├── airflow/
│   └── dags/
│        └── uber_pipeline.py

├── docs/
│     └── architecture.png
```

---

## Tech Stack

- Python
- PySpark
- Apache Iceberg
- Apache Airflow
- Docker
- MinIO (local S3 storage)
- Spark SQL
- Parquet
- Optional: Trino

---

## Features

- Bronze → Silver → Gold architecture
- Apache Iceberg integration
- Schema evolution
- ACID-compliant transactions
- Time-travel queries
- Metadata-driven partition handling
- Data transformation pipelines
- Workflow orchestration using Airflow
- Scalable lakehouse design

---

## Dataset

Dataset used:

NYC Taxi and Uber trip records

Example columns:

- pickup_datetime
- dropoff_datetime
- passenger_count
- trip_distance
- fare_amount
- pickup_location
- dropoff_location
- payment_type

---

## Bronze Layer

Purpose:

Store raw source data exactly as received.

Tasks:

- Ingest source files
- Preserve original schema
- Maintain immutable source records

Example:

```python
df=spark.read.csv(
"data/raw/uber.csv",
header=True
)

df.writeTo(
"local.bronze.uber"
).createOrReplace()
```

---

## Silver Layer

Purpose:

Apply cleansing and business transformations.

Tasks:

- Remove invalid rows
- Handle null values
- Create derived columns
- Standardize formats

Example:

```python
clean=spark.read.table(
"local.bronze.uber"
)

clean=clean.filter(
col("trip_distance")>0
)

clean.writeTo(
"local.silver.uber"
).createOrReplace()
```

---

## Gold Layer

Purpose:

Generate business metrics and analytics datasets.

Example:

```python
gold=spark.sql("""

select
pickup_location,
avg(fare_amount) avg_fare,
count(*) total_trips

from local.silver.uber

group by pickup_location

""")

gold.writeTo(
"local.gold.trip_metrics"
).createOrReplace()
```

---

## Why Apache Iceberg?

Apache Iceberg provides advanced table capabilities beyond standard Spark and Parquet:

### Schema Evolution

Add, rename, or modify columns without rewriting historical datasets.

### ACID Transactions

Ensures writes are atomic and prevents partial updates.

### Time Travel

Query previous versions of a dataset:

```sql
SELECT *
FROM local.silver.uber
VERSION AS OF 3
```

or:

```sql
SELECT *
FROM local.silver.uber
TIMESTAMP AS OF
'2026-05-15 10:00:00'
```

### Metadata Management

Tracks:

- snapshots
- partition metadata
- schema versions
- manifests

---

## Setup Instructions

### Step 1

Clone repository:

```bash
git clone <repository-url>
```

### Step 2

Install dependencies:

```bash
pip install -r requirements.txt
```

### Step 3

Start services:

```bash
docker-compose up -d
```

### Step 4

Run Bronze ingestion:

```bash
spark-submit spark/ingest.py
```

### Step 5

Run transformations:

```bash
spark-submit spark/transform.py
```

### Step 6

Generate analytics:

```bash
spark-submit spark/analytics.py
```

---

## Airflow DAG Flow

```text
Ingest
   ↓
Transform
   ↓
Analytics
```

---

## Future Enhancements

- CDC integration using Debezium
- AWS S3 deployment
- dbt transformations
- Great Expectations validation
- Kubernetes deployment
- CI/CD with GitHub Actions
- Trino query engine
- Iceberg optimization and compaction
- Kafka streaming ingestion
- Prometheus and Grafana monitoring

---

## Resume Bullet

Built an end-to-end Data Lakehouse platform using Apache Iceberg, PySpark, Airflow, and S3-compatible object storage implementing Bronze/Silver/Gold architecture with support for schema evolution, ACID transactions, and time-travel queries.
