# Data Engineering Learning

A personal learning project focused on building a modern data engineering pipeline using the Medallion Architecture.

## Overview

This project demonstrates how raw data can be extracted from CSV files, loaded into SQL Server, transformed using pandas, and organized into the Bronze, Silver, and Gold layers of a data warehouse.

The objective is to learn industry-standard data engineering concepts and best practices by designing and implementing the entire ETL pipeline from scratch, without relying on step-by-step tutorials.

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
- ✅ Silver table creation (in progress)
- ✅ Dynamic extraction of Bronze tables into pandas DataFrames
- ✅ Transformation pipeline architecture
- ✅ Customer (`crm_cust_info`) transformation implemented
- ⏳ Remaining table transformations

## Project Structure

```text
etl-pipeline-project/
│
├── database/
│   └── connection.py          # Database connection
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
│   │   └── main_bronze.py     # Bronze orchestrator
│   │
│   ├── silver/
│   │   ├── transformations/
│   │   │   └── crm_cust_info.py
│   │   │
│   │   ├── define_tables.py
│   │   ├── extract.py
│   │   ├── transform.py       # Transformation orchestrator
│   │   └── main_silver.py     # Silver orchestrator
│   │
│   ├── gold/
│   │
│   ├── create_schema.py       # Shared utility
│   └── create_table.py        # Shared utility
│
├── main.py                    # Project orchestrator
└── README.md
```

## Roadmap

- [x] Bronze Layer
- [ ] Silver Layer
- [ ] Gold Layer
- [ ] Data Quality Checks
- [ ] Logging
- [ ] Unit Tests
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

## Purpose

This repository serves as a hands-on learning project for data engineering, focusing on building a complete ETL pipeline while following software engineering best practices such as modularity, code reusability, and documentation.