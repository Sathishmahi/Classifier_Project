from collections import namedtuple


DataIngestionConfig=namedtuple("DataIngestionConfig", 
[
    "ingestion_dir_path",
    "video_file_path",
    "root_image_dir_name",
    "image_size"
]
)


BaseModelConfig=namedtuple("BaseModelConfig", 
[
  "root_dir",
  "base_model_dir_name",
  "base_model_name",
  "updated_model_dir_name",
  "updated_model_name",
  "image_size",
  "no_of_classes"
]
)


PreapreCallBacksConfig=namedtuple("PreapreCallBacksConfig", 
[
    "root_dir",
    "tb_logs_dir",
    "ckpt_model_dir_name",
    "ckpt_best_model_name"
    
]
)