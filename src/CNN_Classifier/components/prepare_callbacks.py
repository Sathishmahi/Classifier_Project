import tensorflow as tf
from CNN_Classifier import logger
from CNN_Classifier.entity import PreapreCallBacksConfig
from CNN_Classifier.config import Configuration
import time,os
import tensorflow as tf
from pathlib import Path

class PrepareCallbacks:
    def __init__(self,config=Configuration()):
        self.prepare_callbacks_config=config.prepare_callbacks_config

    @staticmethod
    def _tensorboard_cb(tensorboard_root_path:Path):
        
        time_stamp=time.strftime(f'%Y_%m_%d_%H_%M_%S')
        tb_logs_dir_path=os.path.join(tensorboard_root_path,time_stamp)
        return tf.keras.callbacks.TensorBoard(log_dir=tb_logs_dir_path)
    @staticmethod
    def _ckpt_cb(ckpt_model_name:Path):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=ckpt_model_name,
            save_best_only=True
        )
    @staticmethod
    def _early_stopping_cb():
        return tf.keras.callbacks.EarlyStopping(
        monitor='val_loss',
        min_delta=0.01,
        patience=3,
        verbose=1   )

    def get_calbacks(self):
        tensorboard_root_path=self.prepare_callbacks_config.tb_logs_dir
        ckpt_model_name=self.prepare_callbacks_config.ckpt_best_model_name
        return [
            self._ckpt_cb(Path(ckpt_model_name)),
            self._early_stopping_cb(),
            self._tensorboard_cb(Path(tensorboard_root_path))
        ]

        

