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

def execute():

    current_layer = ''

    try:
        start_time = time.perf_counter()

        logging.basicConfig(filename='pipeline.log', level=logging.INFO)
        logger = logging.getLogger()

        current_layer = 'bronze'
        bronze_time = bronze.execute()
        
        current_layer = 'silver'
        silver_time = silver.execute()

        current_layer = 'gold'
        gold_time = gold.execute()

        end_time = time.perf_counter()

        total_time = end_time - start_time

        print(total_time)

    except Exception as e:
        logger.error('=====================================================')
        logger.error('An error occurred while executing the pipeline:')
        logger.error('=====================================================')
        logger.error(f'layer: {current_layer}')
        logger.error(f'Error: {e}')
        logger.error('Stopping the pipeline')

    finally:
        logger.info('===========================================================')
        logger.info('Pipeline execution information')
        logger.info('===========================================================')
        logger.info(f'{'Total time':.<40} {total_time:.2f} sec')
        logger.info(f'{'Bronze layer':.<40} {bronze_time:.2f} sec')
        logger.info(f'{'Silver time':.<40} {silver_time:.2f} sec')
        logger.info(f'{'Gold time':.<40} {gold_time:.2f} sec')
        logger.info('===========================================================')


if __name__ == '__main__':
    execute()