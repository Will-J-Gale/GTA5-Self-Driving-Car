import numpy as np
import os, cv2, time, mss
from vjoy import vJoy
from SelfDrivingCarModel import SelfDrivingCarModel
from keras.models import load_model
from collections import deque

def changeRange(value, minOld, maxOld, minNew, maxNew):
    oldRange = maxOld - minOld
    newRange = maxNew - minNew
    return (((value - minOld) * newRange) / oldRange) + minNew

def scaleSteering(steering):
    #This function tries to eliminate an apparent dead between values 0.4-0.6 in vJoy
    global MIN_WORKING_RANGE_LEFT, MIN_WORKING_RANGE_RIGHT

    if(steering >= 0.5):
        return changeRange(steering, 0.5, 1, MIN_WORKING_RANGE_RIGHT, 1)
    else:
        return changeRange(steering, 0, 0.5, 0, MIN_WORKING_RANGE_LEFT)
      
def preprocess(data):
    newData = data.copy()
    newData = newData / 255
    newData = np.expand_dims(newData, axis=0)
    return newData

def setJoy(controller, stickPos, throttle):
    leftStick = int(stickPos * 32768)
    rightTrigger = int(throttle * 32768)
    
    joystickPosition = controller.generateJoystickPosition(wAxisX = leftStick,
                                                           wAxisZRot = rightTrigger)
    controller.update(joystickPosition)
    
def resetController(controller):
    joystickPosition = controller.generateJoystickPosition()
    controller.update(joystickPosition)

#Screen capture Variables
width = 1920 - 1
height = 1080 
gameWidth = 1274 
gameHeight = 714

xOffset = 2
yOffset = 17
gameStartX = ((width//2) - (gameWidth//2)) + xOffset
gameStartY = ((height//2) - (gameHeight//2)) + yOffset
monitor = {"top": gameStartY, "left": gameStartX, "width": gameWidth, "height": gameHeight}

#Image variables
NEW_SIZE = (400, 220)

#Model Variables
MODEL_NAME = "Self Driving Car.model"
model = SelfDrivingCarModel(inputShape=(NEW_SIZE[1], NEW_SIZE[0], 3))
model.load_weights(MODEL_NAME)

controller = vJoy()
controller.open()
resetController(controller)

AI_ENABLED = True
MIN_WORKING_RANGE_LEFT = 0.45
MIN_WORKING_RANGE_RIGHT = 0.55

numImages = 2
stackedImages = deque(maxlen=numImages)
previousTime = time.time()

index = 0

print("Running")
with mss.mss() as sct:
    while(True):

        #Check for keyboard interrupt
        try:
            start = time.time()
            
            #Get screen capture
            screen = np.array(sct.grab(monitor))
            screen = cv2.resize(screen, NEW_SIZE)
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2RGB) 
                
            if(AI_ENABLED):
                #Model prediction
                modelImage = preprocess(screen)
                prediction = model.predict(modelImage)
                steering = prediction[0][0]
                throttle = prediction[1][0]

                #Apply steering and throttle commands
                scaledSteering = scaleSteering(steering)
                setJoy(controller, scaledSteering, throttle)

                ##Uncomment to show output values
                print(scaledSteering, throttle)
                
            ##Uncomment this to print frame time   
            #print(time.time() - start)
      
        except KeyboardInterrupt:
            print("Closing")
            break
    
resetController(controller)
cv2.destroyAllWindows()










