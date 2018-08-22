# GTA5-Self-Driving-car

## Long Distance Driving
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/LONG_DISTANCE_1.gif)  
## City Driving
![alt text](https://github.com/Will-J-Gale/GTA5-Self-Driving-Car/blob/master/Images/CITY3.gif)  

## Inspiration
This project was inspired by https://github.com/Sentdex/pygta5  
The aim was to make a slightly more realistic GTA5 self driving car,  
that would obey lane keeping, path following, 
traffic speed, traffic lights and stop signs.  

## What the Model Learned
* __Path Following__
   * As the demos show, the car seems to follow the purple path shown in the bottom left and i you run the model without picking a destination it does run much worse.
* __Lane keeping__ 
   * It has learned to keep in lane to a certain extent, which can be seen best when making turns in the city. However this is far from perfect. When driving on the motorway it tends to keep swapping lanes which might be an artifact of overtaking cars in the training data. For some reason it occasionally drove down the hard-shoulder which was not done in training.
* __Trafic Speed__
   * 

Traffic lights and stop signs are difficult to learn as they require some sort of "memory".   
A Reccurant CNN could be a furute upgrade to combat this problem.

## Prerequisites
1. GTA5 + Mods
   * Script Hook V
   * Native Trainer
   * Enhanced Native Trainer
   * GTA V Fov v1.35
   * Extended Camera Settings
   * Hood Camera
   * LeFix Speedometer 1.3.5 (Important)
2. Python 3.6
3. OpenCV
4. Numpy
5. Tensorflow GPU
6. Keras
7. vJoy

## Usage
Recommended to use dual monitors
1. Run GTA5 in windowed mode 1280x720
2. Find a car and enable Hood Camera
3. Enable mini map
4. Create a destination waypoint on the map
5. Run GTA_Self_Driving_Car.py

## The Model
This model was trained using ~100,000 images with corresponding steering, brake and throttle commands.  
It's architecture was moddled after PilotNet by NVIDIA https://arxiv.org/abs/1604.07316  
However, this network was modified to add three regression heads, one for each command.  
The model was initially only trained using the steering command to learn features in the  
convolution layers. After two more regression heads were added and only the remaining regression  
were trained to create the full model.
