🙂🙂🙂

# Hospital Healthcare Data Pipeline

## Overview

This project is an automated data pipeline for processing synthetic hospital and patient data.

The pipeline extracts patient healthcare records from a CSV dataset, validates and transforms the data, stores it in PostgreSQL, and produces analytics-ready datasets for hospital operations and reporting.

The project demonstrates practical data engineering skills including **Python, SQL, PostgreSQL, Apache Airflow, and Docker**.

## Project Objective

The goal of this project is to build a reliable workflow for turning raw hospital records into structured data that can be used for healthcare analytics.

The pipeline focuses on operational questions such as:

* How many patients visit the hospital over time?
* What are the most common reported illnesses?
* How many patients receive treatment?
* What is the distribution of patients by age and gender?
* How many patients are admitted?
* What are the trends in hospital visits and admissions?

## Data

The dataset contains synthetic patient records with fields such as:

* Patient ID
* Patient Name
* Age
* Gender
* Sickness
* Visit Date
* Admission Date
* Doctor Report
* Treatment Status

The data is **synthetic and does not represent real patients**.

## Pipeline Architecture

```text
Synthetic CSV Dataset
        ↓
   Python Validation
        ↓
      Airflow
        ↓
 PostgreSQL - Bronze
        ↓
 Data Cleaning & Transformation
        ↓
 PostgreSQL - Silver
        ↓
 Healthcare Aggregations
        ↓
 PostgreSQL - Gold
        ↓
 Analytics / Dashboard
```

## Technologies

* **Python** — data ingestion and validation
* **Apache Airflow** — workflow orchestration and scheduling
* **PostgreSQL** — data storage and transformation
* **SQL** — data cleaning and analytics
* **Docker** — containerized development environment
* **Power BI / Tableau** — visualization and reporting

## Pipeline Stages

### 1. Extract

The pipeline reads patient records from the source CSV dataset.

### 2. Validate

The data is checked for issues such as:

* Missing values
* Duplicate patient records
* Invalid dates
* Invalid patient IDs
* Incorrect data types

### 3. Load — Bronze Layer

The validated raw data is loaded into PostgreSQL as the **Bronze** layer.

This layer preserves the source data for traceability and further processing.

### 4. Transform — Silver Layer

SQL transformations clean and standardize the data.

Examples include:

* Standardizing gender values
* Handling missing admission dates
* Cleaning treatment status
* Converting dates to appropriate database types
* Removing or handling duplicate records

### 5. Analytics — Gold Layer

The pipeline creates aggregated tables for hospital analytics.

Possible metrics include:

* Patient visits by month
* Admissions by month
* Treatment rates
* Most common illnesses
* Patient demographics
* Average patient age
* Visits by gender

## Airflow Workflow

Airflow manages the execution order of the pipeline tasks.

Example workflow:

```text
validate_data
      ↓
load_bronze
      ↓
transform_silver
      ↓
build_gold
```

Tasks can be scheduled to run automatically and monitored through the Airflow UI.

## Project Structure

```text
hospital-healthcare-pipeline/
│
├── dags/
│   └── hospital_pipeline.py
│
├── scripts/
│   ├── validate_data.py
│   └── load_data.py
│
├── sql/
│   ├── create_tables.sql
│   ├── transform_data.sql
│   └── build_gold.sql
│
├── data/
│   └── hospital_data.csv
│
├── reports/
│
├── docker-compose.yml
│
└── README.md
```

## Key Data Engineering Concepts Demonstrated

* ETL/ELT pipeline development
* Workflow orchestration
* Data validation
* Data quality checks
* SQL transformations
* Relational data modeling
* Bronze/Silver/Gold architecture
* PostgreSQL data management
* Containerized development
* Automated pipeline execution

## Disclaimer

This project uses **synthetic healthcare data created for educational and portfolio purposes**. It does not contain real patient information and should not be used for medical decision-making.
