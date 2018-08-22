# GTA5-Self-Driving-car

## Long Distance Driving
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/LONG_DISTANCE_1.gif)  
## City Driving
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/CITY3.gif)  

## Inspiration
This project was inspired by https://github.com/Sentdex/pygta5  
The aim was to make a slightly more realistic GTA5 self-driving car. 
It should obey lane keeping, path following, 
traffic speed, traffic lights and stop signs. 

## The Model
This model was trained using ~100,000 images with corresponding steering, brake and throttle commands.  
The architecture was modelled after PilotNet by NVIDIA https://arxiv.org/abs/1604.07316  
However, this network was modified to add three regression heads, one for each command.  
The model was initially only trained using the steering command to learn features in the  
convolution layers. After this, two more regression heads were added and only the remaining regression  
layers were trained to create the full model.

## What the Model Learned
* __Path Following__
   * As the demos show, the car seems to follow the purple path shown in the bottom left and i you run the model without picking a destination it does run much worse. 
* __Lane keeping__ 
   * It has learned to keep in lane to a certain extent, which can be seen best when making turns in the city. However, this is far from perfect. When driving on the motorway it tends to keep swapping lanes which might be an artefact of overtaking cars in the training data. For some reason it occasionally drove down the hard-shoulder which was not done in training. Moreover,it manages to get back in the correct lane if it accidently goes in the other lane
* __Traffic Speed__
   * On the long distance demo, the model seems to maintain roughly 60mph, however this could be just mimicking the training data and not following any laws of the road. In the city, however, it does reach speeds faster than the training data went, which could be because there is more long distance data than city data.

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
1. Download model weights from https://drive.google.com/open?id=1nyTTkGVF7DM1gmA-_RlkQaf-IZb8MDlP and place them in the same directory as GTA_Self_Driving_Car.py 
2. Run GTA5 in windowed mode 1280x720
3. Find a car and enable Hood Camera
4. Enable mini map
5. Create a destination waypoint on the map
6. Run GTA_Self_Driving_Car.py

## Thoughts
The model seemed to learn quite a lot from a relativly small dataset.   
However, there is still a long way to go as other things need to be added such as
   * Dedicated lane finding
   * Object detection (Cars, people, signs etc)
   * Logical rules such as what to do at traffic lights/stop signs
   * OR use a Reccurent CNN for these tasks.  
  
Moreover, more data will help improve the model in the future.
