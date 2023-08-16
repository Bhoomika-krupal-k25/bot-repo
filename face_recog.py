#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import dlib
from PIL import Image
import os
import numpy as np
import face_recognition

face_detector = dlib.get_frontal_face_detector()
image_dir = "C:\\Users\\bhoom\\OneDrive\\Desktop\\image direc"
known_image_path = "C:\\Users\\bhoom\\OneDrive\\Desktop\\image direc\\bhoom.jpg"


known_image = face_recognition.load_image_file(known_image_path)
known_face_encoding = face_recognition.face_encodings(known_image)[0]

for filename in os.listdir(image_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(image_dir, filename)
        
       
        image = Image.open(image_path)

        
        gray_image = image.convert("L")

       
        image_array = np.array(gray_image)

        
        faces = face_detector(image_array)

        
        for face in faces:
           
            image.show()


# In[ ]:


C:\\Users\\bhoom\\OneDrive\\Desktop\\image direc\\bhoom.jpg

