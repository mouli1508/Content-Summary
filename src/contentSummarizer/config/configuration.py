from contentSummarizer.constants import *
from contentSummarizer.utils.common import read_yaml, create_directories
from contentSummarizer.entity import DataIngestionConfig

class ConfigurationManager:

    def __init__(
            self, 
            config_filepath = CONFIG_FILE_PATH, 
            params_filepath = PARAMS_FILE_PATH
    ):
        self.congif = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.congif.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.congif.data_ingestion

        create_directories([config.root_directory])

        data_ingestion_config = DataIngestionConfig(
            root_directory=config.root_directory,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_directory=config.unzip_directory
        )

        return data_ingestion_config