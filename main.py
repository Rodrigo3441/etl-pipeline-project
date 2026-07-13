"""
=====================================================
Main ETL Pipeline
=====================================================
Script Purpose:
    This script serves as the entry point of the Data Engineering project.
    It starts the ETL process by executing the Bronze layer pipeline, which
    is responsible for creating the required database objects, extracting
    source data, and loading it into the Bronze layer.

Notes:
    - Acts as the project's main execution script.
    - Invokes the Bronze layer pipeline.
    - Will be extended to execute the Silver and Gold layer pipelines
      as they are implemented.
"""

import scripts.bronze.main_bronze as bronze
import scripts.silver.main_silver as silver

# bronze.execute()
silver.execute()
