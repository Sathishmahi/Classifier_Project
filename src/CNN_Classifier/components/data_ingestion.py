from CNN_Classifier import logger
from CNN_Classifier.config import Configuration
from CNN_Classifier.utils import make_dirs
from pathlib import Path
from PIL import Image
import uuid
import os
import cv2
import streamlit as st

class DataIngestion:
    def __init__(self,config=Configuration()):
        self.data_ingestion_config=config.data_ingestion_config

    def to_get_videos(self):
        all_files=st.file_uploader('Select Files Note[File name and Class name Must Be Same]',
        accept_multiple_files=True)
        click_btn=st.button('Start Training')
        if (all_files is None and click_btn) or( len(all_files)==1 and click_btn) :
            st.exception('minimum to select 2 files')
        # if not all_files:
        for file_detail in all_files:
            root_dir=os.path.join(self.data_ingestion_config.video_file_path)
            file_path=os.path.join(root_dir,file_detail.name)
            with open(file_path,'wb') as file:
                print('file write start')
                file.write(file_detail.read())
                print(f'done {file_path}')

    def convert_video_to_frame(self):

        root_image_dir_name=self.data_ingestion_config.root_image_dir_name
        all_vedios_list=os.listdir(self.data_ingestion_config.video_file_path)
        print(self.data_ingestion_config.video_file_path)
        all_class_name=[ os.path.splitext(file)[0].replace(' ', '_') for file in all_vedios_list ]
        all_class_dir_path=[os.path.join(root_image_dir_name,class_name) for class_name in all_class_name ]
        make_dirs(all_class_dir_path)
        image_size=tuple(self.data_ingestion_config.image_size[:-1])

        for video,class_name in zip(all_vedios_list,all_class_dir_path):
            video_file_path=os.path.join(self.data_ingestion_config.video_file_path,video)
            vf=cv2.VideoCapture(video_file_path)
            sucess=1
            while True:
                sucess,img_arr=vf.read()
                if sucess:
                    img_file_path=os.path.join(class_name,f'{str(uuid.uuid1())}.jpg')
                    img_srr=cv2.resize(image_size)
                    cv2.imwrite(img_file_path, img_arr)
                else:
                    break
                    




    