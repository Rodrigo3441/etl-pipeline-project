# Data Engineering Learning

A personal learning project focused on building a complete ETL pipeline using the Medallion Architecture.

## Overview

This project demonstrates how raw data can be extracted from multiple CSV files, loaded into SQL Server, transformed with pandas, and organized into Bronze, Silver, and Gold layers following modern data warehouse principles.

The main objective is to learn data engineering by designing and implementing an end-to-end ETL pipeline from scratch while applying software engineering practices such as modularity, code reusability, documentation, and clean project organization.

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
- ✅ Dynamic extraction from Bronze
- ✅ Transformation orchestrator
- ✅ Data type standardization
- ✅ Data cleansing and validation
- ✅ CRM transformations
- ✅ ERP transformations
- ✅ Data loading into SQL Server

### Gold Layer
- ✅ Gold schema creation
- ✅ Gold table creation
- ✅ Dynamic extraction from Silver
- ✅ Customer dimension (dim_customers)
- ✅ Product dimension (dim_products)
- ✅ Sales fact table (fact_sales)
- ✅ Business-ready data loading into SQL Server

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

## Pipeline Architecture

```
CSV Files
    │
    ▼
Bronze Layer
    │
    ▼
Silver Layer
    │
    ▼
Gold Layer
    ├── dim_customers
    ├── dim_products
    └── fact_sales
```

## Roadmap

- [x] Bronze Layer
- [x] Silver Layer
- [x] Gold Layer
- [ ] Exception handling
- [ ] Pipeline logging
- [ ] Execution time monitoring
- [ ] Data quality checks
- [ ] Configuration file
- [ ] Unit tests
- [ ] Power BI dashboard
- [ ] Complete documentation

## Learning Objectives

This project is being developed to practice and understand:

- ETL pipeline development
- Medallion Architecture
- Data warehouse design
- Star schema modeling
- Dimension and Fact tables
- Data transformation with pandas
- SQLAlchemy
- SQL Server integration
- Writing modular and maintainable Python code
- ETL orchestration
- Software engineering best practices

## Future Improvements

- Add structured logging across all pipeline layers.
- Implement centralized exception handling.
- Measure execution time for each layer and the complete pipeline.
- Add data quality validation reports.
- Improve configuration management.
- Create architecture diagrams.
- Build a Power BI dashboard using the Gold layer.
- Containerize the project with Docker.

## Purpose

This repository serves as a hands-on learning project for data engineering. The goal is not only to build a working ETL pipeline, but also to understand how real-world data engineering projects are organized, developed, documented, and maintained.