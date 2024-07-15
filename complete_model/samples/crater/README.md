# Mars Crater Detection and Segmentation with MaskRCNN

![](https://github.com/mymultiverse/Mask_RCNN/blob/master/samples/crater/gitex.PNG)

#### Dependencies 
Tested On Windows 10 pro PC with GPU
```
conda install tensorflow-gpu
conda install keras
```

Detection of craters on planetary surface is very crucial for the better understanding of planet topography. It is also important for the selection of landing sites of various lander mission, path planning for rover missions. This project is about application of deep learning method for detection and semantic segmentation of craters in an image. Model trained using transfer learning on pretrained MaskRCNN model. Overall project can be devided into four parts as follow:-    

1. [Data Preparation](https://github.com/mymultiverse/Mask_RCNN/edit/master/samples/crater#Data-Collection-and-Training-Validation-data-preparation)

2. [Data Inspection](https://github.com/mymultiverse/Mask_RCNN/blob/master/samples/crater/inspect_crater_data.ipynb)

3. [Training](https://github.com/mymultiverse/Mask_RCNN/blob/master/samples/crater/train.ipynb)

4. [Testing](https://github.com/mymultiverse/Mask_RCNN/blob/master/samples/crater/inspect_crater_model.ipynb)

With splash.py the trained model was tested on video, although it was only trained with Mars data, learned model able to detect craters on the lunar surface as well.

Mars                       |  Moon
:-------------------------:|:-------------------------:
[![](https://img.youtube.com/vi/JdmykAEQing/0.jpg)](https://youtu.be/JdmykAEQing) |                                           [![](https://img.youtube.com/vi/FRbNQiYLvgo/0.jpg)](https://youtu.be/FRbNQiYLvgo)

#### Data Collection and Training-Validation data preparation 

Image data collected from the [sources](Dataset-Sources) and annotated with [VIA](http://www.robots.ox.ac.uk/~vgg/software/via/via.html) tool to get json file. Which looks like:- 

![](https://github.com/mymultiverse/Mask_RCNN/blob/master/samples/crater/viaex.PNG)

The Labeled dataset can be downloaded from [dropbox](https://www.dropbox.com/s/adf8dqbcur54iub/craterData.zip?dl=0).
Dataset directory looks like:-
```bash

├── train
│   ├── img1.jpg
|   ├── :
|   ├── imgn.jpg
│   └── via_region_data.json
└── val
    ├── img.jpg
    ├── :
    ├── imgq.jpg
    └── via_region_data.json
```
train and val folder should be inside datasets directory(which is place at root directory)

Trained model mask_rcnn_crater_new.h5 [dropbox](https://www.dropbox.com/s/49b8qwinjb71doa/mask_rcnn_crater_new.h5?dl=0)

Dataset Sources:

1. [High Resolution Imaging Science Experiment](https://www.uahirise.org/)
2. [Mars Science](https://mars.nasa.gov/multimedia/images/)
3. [ASU](https://jmars.mars.asu.edu/)
4. [USGS](https://webgis2.wr.usgs.gov/Mars_Global_GIS/)

