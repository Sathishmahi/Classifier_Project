from CNN_Classifier.config import Configuration
import tensorflow as tf
from pathlib import Path


class PrepareBaseModel:
    def __init__(self,config=Configuration()):
        self.base_model_config=config.base_model_config

    @staticmethod
    def save_model(model:tf.keras.Model,path:Path):
        model.save(path)
    @staticmethod
    def load_model(path:Path)->tf.keras.Model:
        return tf.keras.models.load_model(path)

    def _prepare_base_model(self):
        # model=tf.keras.applications.resnet50.ResNet50(
        #     include_top=False,
        #     weights='imagenet',
        #     input_shape=self.base_model_config.image_size,
        #     classes=self.base_model_config.no_of_classes
        # )



        model=tf.keras.applications.vgg16.VGG16(
            include_top=False,
            weights='imagenet',
            input_shape=self.base_model_config.image_size,
            classes=self.base_model_config.no_of_classes
        )

        base_model_path=self.base_model_config.base_model_name
        self.save_model(model,base_model_path)
        return model

    def _preapare_full_model(self,base_model,freeze_all:bool=False,freeze_till:int=2):


        
        
        full_model_path=self.base_model_config.updated_model_name

        no_of_classes=self.base_model_config.no_of_classes
        if freeze_all:
            base_model.trainable=False
        if not freeze_all and freeze_till>1:
            for layer in base_model.layers[:-freeze_till]:
                layer.trainable = False

        flatten_in=tf.keras.layers.Flatten()(base_model.output)
        dense_1=tf.keras.layers.Dense(units=64,activation='relu')(flatten_in)
        dense_2=tf.keras.layers.Dense(units=64,activation='relu')(dense_1)
        prediction=tf.keras.layers.Dense(units=no_of_classes,activation='softmax')(flatten_in)

        full_model=tf.keras.models.Model(
            inputs=base_model.input,
            outputs=prediction
        )

        full_model.compile(
            loss=tf.keras.losses.SparseCategoricalCrossentropy(),
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
            metrics=['accuracy']
        )

        full_model.summary()
        self.save_model(model=full_model,path=Path(full_model_path))


    def combine_all(self):
        model=self._prepare_base_model()
        self._preapare_full_model(base_model=model)

