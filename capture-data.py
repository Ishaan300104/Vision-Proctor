# If you're using this file for capturing data then 
# Skip the "Preparing data" code section and go to
# "Labelling Images code section" after using this script

import os
import cv2
import time
import uuid

# Defining data directory and classes for prediction
IMAGES_PATH = os.path.join('data', 'images') #/data/images
labels = ['covering mouth (WARNING!)', 'speaking (WARNING!)', 'Laughing (WARNING!)' , 'looking on screen (Normal)', 'thinking (Normal)', ]
number_imgs = 5


# Capturing images for fine-tuning YOLOv5 model
cap = cv2.VideoCapture(0)
# Loop through labels
for label in labels:
    print('Collecting images for {}'.format(label))
    time.sleep(3)
    
    # Loop through image range
    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))
        
        # Webcam feed
        ret, frame = cap.read()
        
        # Naming out image path
        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
        
        # Writes out image to file 
        cv2.imwrite(imgname, frame)
        
        # Render to the screen
        cv2.imshow('Image Collection', frame)
        
        # 2 second delay between captures
        time.sleep(2)
        
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()


# Concatenating image name and path
print(os.path.join(IMAGES_PATH, labels[0]+'.'+str(uuid.uuid1())+'.jpg'))


# Collecting images
for label in labels:
    print('Collecting images for {}'.format(label))
    for img_num in range(number_imgs):
        print('Collecting images for {}, image number {}'.format(label, img_num))
        imgname = os.path.join(IMAGES_PATH, label+'.'+str(uuid.uuid1())+'.jpg')
        print(imgname)   


