from CNN_Classifier.utils import read_yaml,make_dirs
from CNN_Classifier.entity import DataIngestionConfig,BaseModelConfig
from CNN_Classifier.constant import *
import os
import numpy as np


class Configuration:
    def __init__(self):
        self.config_content=read_yaml()
        self.params_content=read_yaml(PARAMS_YAML_FILE_PATH)
        self.artifact_root_dir=self.config_content.get("artifact_root_dir_name")


        #### all config
        self.data_ingestion_config=self.get_data_ingestion_config()
        self.base_model_config=self.get_base_model_config()

    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            data_ingestion_attr=self.config_content.get("data_ingestion")
            data_ingestion_dir_name=data_ingestion_attr.get("data_ingestion_dir_name")
            video_dir_name=data_ingestion_attr.get("video_dir_name")
            root_image_dir_name=data_ingestion_attr.get("root_image_dir_name")
            ingestion_dir_path=os.path.join(self.artifact_root_dir,data_ingestion_dir_name)
            videos_file_path=os.path.join(ingestion_dir_path,video_dir_name)
            root_image_dir_path=os.path.join(ingestion_dir_path,root_image_dir_name)

            make_dirs([self.artifact_root_dir,ingestion_dir_path,videos_file_path])
            data_ingestion_config=DataIngestionConfig(ingestion_dir_path=ingestion_dir_path,
            video_file_path=videos_file_path,
            root_image_dir_name=root_image_dir_path,
            image_size=self.params_content.get("image_size"))

            return data_ingestion_config

        except Exception as e:
            raise e

    def get_base_model_config(self)->BaseModelConfig:
        try:
            base_model_config_attr=self.config_content.get("prepare_base_model")
            root_dir=os.path.join(self.artifact_root_dir,base_model_config_attr.get("root_dir"))


            base_model_dir_name=os.path.join(root_dir,base_model_config_attr.get("base_model_dir_name"))
            base_model_name=os.path.join(base_model_dir_name,base_model_config_attr.get("base_model_name"))
            updated_model_dir_name=os.path.join(root_dir,base_model_config_attr.get("updated_model_dir_name"))
            updated_model_name=os.path.join(updated_model_dir_name,base_model_config_attr.get("updated_model_name"))
            make_dirs([root_dir,base_model_dir_name,updated_model_dir_name])
            image_size=self.params_content.get("image_size")
            no_of_classes=len(os.listdir(self.data_ingestion_config.root_image_dir_name))

            basic_model_config=BaseModelConfig(root_dir=root_dir, base_model_dir_name=base_model_dir_name, 
            base_model_name=base_model_name, updated_model_dir_name=updated_model_dir_name, 
            updated_model_name=updated_model_name,
            image_size=image_size,no_of_classes=no_of_classes)

            return basic_model_config
        except Exception as e:
            raise e
