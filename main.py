"""
=====================================================
Main ETL Pipeline
=====================================================
Script Purpose:
    This script serves as the entry point of the Data Engineering
    project. It orchestrates the complete ETL workflow by executing
    the Bronze, Silver, and Gold layer pipelines in sequence.

    In addition to orchestrating the pipeline, it configures the
    logging system, measures execution times for each layer and the
    overall pipeline, and handles pipeline-level exceptions.

Notes:
    - Acts as the project's main execution script.
    - Configures the application's logging.
    - Executes the Bronze, Silver, and Gold layer orchestrators.
    - Measures and logs the execution time of each layer.
    - Measures and logs the total pipeline execution time.
    - Handles pipeline-level exceptions and reports the layer
      where the failure occurred.
"""

import scripts.bronze.main_bronze as bronze
import scripts.silver.main_silver as silver
import scripts.gold.main_gold as gold
import logging
import time

# logging configuration
logging.basicConfig(
                    filename='pipeline.log', 
                    level=logging.INFO,
                    format='%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                    )

logger = logging.getLogger()

def execute():
    logger.info('=====================================================')
    logger.info('Starting the ETL Pipeline')
    logger.info('=====================================================')

    # variable to store the current layer that's being executed
    current_layer = ''

    # variables to track time
    bronze_time = 0
    silver_time = 0
    gold_time = 0
    total_time = 0

    try:
        start_time = time.perf_counter()

        current_layer = 'bronze'
        logger.info('Executing Bronze Layer')
        bronze_time = bronze.execute()
        
        current_layer = 'silver'
        logger.info('Executing Silver Layer')
        silver_time = silver.execute()

        current_layer = 'gold'
        logger.info('Executing Gold Layer')
        gold_time = gold.execute()

        end_time = time.perf_counter()

        total_time = end_time - start_time

    except Exception as e:
        logger.exception('=====================================================')
        logger.exception('An error occurred while executing the pipeline:')
        logger.exception('=====================================================')
        logger.exception(f'layer: {current_layer}')
        logger.exception(f'Error: {e}')
        logger.exception('Stopping the pipeline')

    finally:
        logger.info('===========================================================')
        logger.info('Pipeline execution information')
        logger.info('===========================================================')
        logger.info(f'{'Total time':.<40} {total_time:.2f} sec')
        logger.info(f'{'Bronze layer':.<40} {bronze_time:.2f} sec')
        logger.info(f'{'Silver layer':.<40} {silver_time:.2f} sec')
        logger.info(f'{'Gold layer':.<40} {gold_time:.2f} sec')
        logger.info('===========================================================')
        logger.info('Pipeline completed successfully.')


if __name__ == '__main__':
    execute()