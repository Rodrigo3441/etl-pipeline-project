# Data Engineering Learning

A personal learning project focused on building a modern data engineering pipeline using the Medallion Architecture.

## Overview

This project demonstrates how raw data can be extracted from CSV files, loaded into SQL Server, transformed using pandas, and organized into the Bronze, Silver, and Gold layers of a data warehouse.

The objective is to learn industry-standard data engineering concepts and best practices by designing and implementing the entire ETL pipeline from scratch, emphasizing modularity, code reusability, and maintainable software architecture.

## Technologies

- Python
- Pandas
- SQLAlchemy
- Microsoft SQL Server
- SQL Server Management Studio (SSMS)

## Current Progress

### Bronze Layer
- ✅ Database connection
- ✅ Bronze schema creation
- ✅ Bronze table creation
- ✅ Data extraction from CSV files
- ✅ Data loading into SQL Server

### Silver Layer
- ✅ Silver schema creation
- ✅ Silver table creation
- ✅ Dynamic extraction of Bronze tables into pandas DataFrames
- ✅ Transformation orchestration
- ✅ CRM customer transformations
- ✅ CRM product transformations
- ✅ CRM sales transformations
- ✅ ERP customer transformations
- ✅ ERP location transformations
- ✅ ERP product category transformations
- ✅ Data loading into SQL Server

### Gold Layer
- 🚧 Planning and implementation

## Project Structure

```text
etl-pipeline-project/
│
├── database/
│   └── connection.py
│
├── datasets/
│   ├── source_crm/
│   └── source_erp/
│
├── scripts/
│   ├── bronze/
│   │   ├── define_tables.py
│   │   ├── extract.py
│   │   ├── load.py
│   │   └── main_bronze.py
│   │
│   ├── silver/
│   │   ├── transformations/
│   │   │   ├── crm_cust_info.py
│   │   │   ├── crm_prd_info.py
│   │   │   ├── crm_sales_details.py
│   │   │   ├── erp_cust_az12.py
│   │   │   ├── erp_loc_a101.py
│   │   │   └── erp_px_cat_g1v2.py
│   │   │
│   │   ├── define_tables.py
│   │   ├── extract.py
│   │   ├── transform.py
│   │   ├── load.py
│   │   └── main_silver.py
│   │
│   ├── gold/
│   │
│   ├── create_schema.py
│   └── create_table.py
│
├── main.py
└── README.md
```

## Roadmap

- [x] Bronze Layer
- [x] Silver Layer
- [ ] Gold Layer
- [ ] Pipeline Logging
- [ ] Data Quality Checks
- [ ] Unit Tests
- [ ] Configuration File
- [ ] Complete Documentation

## Learning Objectives

This project is being developed to practice and understand:

- ETL pipeline development
- Medallion Architecture
- Data warehouse concepts
- Data transformation with pandas
- SQLAlchemy
- SQL Server integration
- Writing modular and maintainable Python code
- ETL orchestration
- Data quality and validation techniques

## Future Improvements

- Implement the Gold layer with business-ready tables.
- Add structured logging throughout the pipeline.
- Add data quality validation reports.
- Improve configuration management.
- Document the pipeline architecture with diagrams.
- Build a Power BI dashboard using the Gold layer.

## Purpose

This repository serves as a hands-on learning project for data engineering, focusing on building a complete ETL pipeline while applying software engineering best practices such as modularity, code reusability, documentation, and layered architecture.