# Sign Interpreter using Tensorflow and OpenCV

this project was assigned as a task for Doxpro Robotics Co.'s internship interview.

Although the project could not reach a working prototype stage due to tensorflow not working I am submitting whatever I could make in the time allotted

## What was done and steps ahead?
> 1. I collected a set of images to train the AI model needed for five different hand gestures using OpenCV [&#x2611;]
> 2. The collected  images were labelled using labelImg python package. The .xml files with necessary metadata could be found in ``` Tensorflo/workspace/images/collected_images/``` [&#x2611;]
> 3. A pre-trained tensorflow object detection model was to be used to train on our own dataset using Transfer Learning technique. related files could be found in ```Tensorflow/scripts/``` and the pretrained model could be found in ```Tensorflo/workspace/pre-trained-model``` [&#x2612;]
> 4. Then the trained model would have been tested in real time using OpenCV and [&#x2612;]
> 5. The rest of my attempts to get tensorlow to work could be found in ```main.ipynb```

## To Test.
> 1. Create a virtual enviornment using ```Python3 -m venv .venv```
> 2. activate the said enviornment
> 3. run ```pip install -r req.txt ``` to install all necessary packages
