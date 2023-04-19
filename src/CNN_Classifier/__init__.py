import logging
import os,sys
from CNN_Classifier.utils import make_dirs,read_yaml
from CNN_Classifier.constant import *


content=read_yaml()
print(content)
log_dir_name=content.get("logs_root_dir_name")
make_dirs([log_dir_name])
log_file_path = os.path.join(log_dir_name, "running_logs.log")

format = "[ %(asctime)s    %(levelname)   s%(module)s ]  [ %(message)s ]"
logging.basicConfig(
    level=logging.INFO,
    format=format,
    handlers=[
        logging.FileHandler(log_file_path),
        # logging.StreamHandler(sys.stdout)
    ],
)
logger = logging.getLogger("ClassifierLogger")