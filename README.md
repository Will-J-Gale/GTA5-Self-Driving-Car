# GTA5-Self-Driving-car

## Driving Unfamiliar Roads
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Driving_Unfamiliar_roads.gif)  
## Driving Familiar Roads
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Driving_Familiar_roads.gif)  

Images are at 2x speed to show more driving in a shorter time span.

## Inspiration
This project was inspired by https://github.com/Sentdex/pygta5  
The aim was to make a slightly more realistic GTA5 self-driving car.  
By utilizing imitation learning the model has learned to stay in lane 
and keep it's speed up. 

## The Model
<img src="https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/SelfDrivingModel.png" alt="drawing" width="200"/>

This model was trained using ~80,000 images with corresponding steering and throttle commands.  
The architecture was loosely  modelled after PilotNet by NVIDIA https://arxiv.org/abs/1604.07316  
However, this network was modified to add two regression heads, one for each command.  
The model was initially only trained using the steering command to learn features in the  
convolution layers. After this, a second regression head was added and only the remaining regression  
layers were trained to create the full model.

## Datasets
Two separate datasets were used for steering and throttle.
This was because the distribution of the steering and throttle heavily favoured certain positions, 
so the data was pruned to create a flatter distribution so the model will not overfit.
When the steering data had a good distribution the throttle distribution was bad, and vice versa,
hence training them separately.

Steering Dataset Before    |  Steering Dataset After
:-------------------------:|:-------------------------:
![](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Steering_100k.png)  |  ![](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Steering_52k.png)

Throttle Dataset Before    |  Throttle Dataset After
:-------------------------:|:-------------------------:
![](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Throttle_100k.png)  |  ![](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/Throttle_35k.png)

## Prerequisites
1. GTA5 + Mods
   * Script Hook V
   * Native Trainer
   * Enhanced Native Trainer
   * GTA V Fov v1.35
   * Extended Camera Settings
   * Hood Camera
   * Singleplayer Reveal Map
   * LeFix Speedometer 1.3.5 (Important)
2. Python 3.6
3. OpenCV
4. Numpy
5. Tensorflow GPU
6. Keras
7. x360ce (https://www.x360ce.com/)
8. vJoy (http://vjoystick.sourceforge.net/site/)

## Usage
Recommended to use dual monitors
1. Download model weights from https://drive.google.com/open?id=1NgaGZ-oFjvl-GxJvOtqXdIedrumV64-o and place them in the same directory as GTA_SelfDrivingCar.py 
2. Run GTA5 in windowed mode 1280x720
3. Find a car and enable Hood Camera (press 8)
4. Run GTA_Self_Driving_Car.py
5. Find a long road like a motorway or country road

## Training 
To train the model, simply collect images of size 400x220 along with steering and throttle commands and train the model like any other convolutional neural network in keras.

The images are the inputs to the network.  
The steering and throttle commands are the outputs.

For more information on how to train neural networks generally visit:  
https://www.youtube.com/watch?time_continue=1&v=wQ8BIBpya2k&feature=emb_logo

For information on training networks with multiple outputs visit:  
https://keras.io/getting-started/functional-api-guide/#multi-input-and-multi-output-models

## Thoughts
The model seemed to learn quite a lot from a relatively small dataset.   
However, there is still a long way to go as other things need to be added such as
   * Scene segmentation to give a sense of what is surrounding the car
   * Depth perception to give a sense of distance to surroundings
   * Optical flow to give a sense of how things in the scene are moving
   * Add time into the model using something like an LSTM 
   
Moreover, more data will help improve the model in the future.
