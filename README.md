# ETL Python Pipeline Project
## Overview

This project implements a complete **ETL (Extract, Transform, Load) pipeline** in Python, following the **Medallion Architecture** (Bronze, Silver, and Gold layers). It demonstrates how raw data from multiple CRM and ERP CSV sources can be extracted, transformed, and loaded into a Microsoft SQL Server data warehouse through a modular and scalable pipeline.

The pipeline is designed with a layered architecture, where each stage has a specific responsibility. The Bronze layer ingests raw source data into the database, the Silver layer performs data cleansing and transformations to improve data quality, and the Gold layer creates business-ready dimensional models for analytical reporting.

To promote maintainability and code organization, the project is divided into independent modules responsible for schema creation, table creation, data extraction, transformation, and loading. Layer orchestration is handled by dedicated pipeline controllers, while centralized logging and exception handling provide execution monitoring and simplify troubleshooting.

This project serves as a practical implementation of Data Engineering concepts using Python, pandas, SQLAlchemy, and Microsoft SQL Server, demonstrating software engineering best practices such as modular design, reusable components, structured logging, execution time monitoring, and comprehensive documentation.


## Features

- Modular ETL architecture<br>
- Bronze, Silver and Gold layers<br>
- SQL Server integration<br>
- pandas transformations<br>
- SQLAlchemy<br>
- Centralized logging<br>
- Execution time monitoring<br>
- Exception handling<br>
- Modular project structure<br>

## Project Requirements


## Technologies

| Category                     | Technologies                    |
| ---------------------------- | ------------------------------- |
| **Programming Language**     | Python                          |
| **Data Processing and Tranformations**     | `pandas`          |
| **Database Connectivity**    | `SQLAlchemy`                    |
| **Database Driver**          | pyodbc
| **Logging**                  | Python `logging`                |
| **Database**                 | Microsoft SQL Server            |
| **Development Tools**        | Visual Studio Code              |
| **Documentation & Diagrams** | Draw.io                         |
| **Version Control**          | Git, GitHub                     |

## Repository Structure
``` bash
etl-pipeline-project/
├── database/
│   └── connection.py
│
├── datasets/
│   ├── source_crm/
│   └── source_erp/
│
├── docs/
│ 
├── scripts/
│   ├── bronze/
│   │   ├── define_tables.py
│   │   ├── extract.py
│   │   └── main_bronze.py
│   │
│   ├── gold/
│   │   ├── transformations/
│   │   │   ├── dim_customers.py
│   │   │   ├── dim_products.py
│   │   │   └── fact_sales.py
│   │   │
│   │   ├── define_tables.py
│   │   ├── main_gold.py
│   │   └── transform.py
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
│   │   ├── main_silver.py
│   │   └── transform.py
│   │
│   ├── create_schema.py
│   ├── create_table.py
│   └── load.py
│
├── .gitignore
├── main.py
├── pipeline.log
└── README.md
```

## Project Architecture


## ETL Flow


## Medallion Architecture


## Logging


## Documentation


## How to Run


## Example Output


## Future Improvements


---

## License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and share this project with proper attribution.

---
## 👨‍💻 About Me

Hi! i'm Rodrigo, a data engineer student that is learning new things every day.