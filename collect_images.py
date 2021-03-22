import os
import time
import cv2

IMAGE_FOLDER = 'Tensorflow/workspace/images/collected_images'

labels = [
    'one',
    'two',
    'three',
    'four',
    'five',
]

num_imgs = 15

for label in labels:
    path = os.path.join(IMAGE_FOLDER, label)
    # os.mkdir(path)
    cap = cv2.VideoCapture(0)
    print('collecting {}'.format(label))
    time.sleep(2)
    for imnum in range(num_imgs):
        ret, frame = cap.read()
        im_name = os.path.join(path, label + '_{}.jpg'.format(str(imnum)))
        if not cv2.imwrite(im_name, frame):
            raise Exception('Cannot write to path specified')
        cv2.imshow('frame', frame)
        time.sleep(1)
        
        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
    cap.release()
