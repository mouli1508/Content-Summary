from contentSummarizer.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from contentSummarizer.logging import logger

STAGE_NAME = 'Data ingesiton stage'

try:
    logger.info(f'~~~~~~~~~~~~ Starting {STAGE_NAME} ~~~~~~~~~~~~')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'~~~~~~~~~~~~ Finished {STAGE_NAME} ~~~~~~~~~~~~')

except Exception as e:
    logger.exception(e)
    raise e