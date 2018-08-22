from NVIDIA_Model_Multi import NVIDIAModelMulti
import numpy as np
import cv2, os, time, mss, math
from vjoy import vJoy
import math

def sigmoid(x, k = 1):
    newValue = 1/(1+math.exp(-k * (x-0.5)))
    return newValue

def preprocess(data):
    newData = data.copy()
    newData = newData / 255
    return newData

def resetController(controller):
    joystickPosition = controller.generateJoystickPosition()
    controller.update(joystickPosition)

def showFrameTime():
    global previousTime, averageFPS
    frameTime = time.time() - previousTime
    averageFPS.append(frameTime)
    print(1/np.average(averageFPS))
    previousTime = time.time()
    
    if(len(averageFPS) > 50):
        averageFPS.pop(0)
    
def setJoy(controller, stickPos, brake, throttle):
    leftStick = int(stickPos * 32768)
    leftTrigger = int(brake * 32768)
    rightTrigger = int(throttle * 32768)
    
    joystickPosition = controller.generateJoystickPosition(wAxisX = leftStick,
                                                           wAxisZ = leftTrigger,
                                                           wAxisZRot = rightTrigger)
    controller.update(joystickPosition)
    
MODEL_NAME = "SDCNN_NVIDIA_Multi.model"    
model = NVIDIAModelMulti(inputShape=(315, 560, 3))
model.load_weights(MODEL_NAME)
#model.summary()

width = 1920 - 1
height = 1080 
gameWidth = 1274 
gameHeight = 714

xOffset = 2 #Gets rid of x boarder on window
yOffset = 17 #Gets rid of y boarder on window
gameStartX = ((width//2) - (gameWidth//2)) + xOffset
gameStartY = ((height//2) - (gameHeight//2)) + yOffset
monitor = {"top": gameStartY, "left": gameStartX, "width": gameWidth, "height": gameHeight}

#SCREEN_REGION = (gameStartX, gameStartY, gameEndX, gameEndY)
SCREEN_NAME = "Self Driving Car"

NEW_SIZE = (560, 315)
AI_ENABLED = True

controller = vJoy()
controller.open()
resetController(controller)

previousTime = time.time()

averageFPS = []

with mss.mss() as sct:
    print("Running")
    while(True):
        try:
            #Get screen and process it
            screen = np.array(sct.grab(monitor))
            screen = cv2.resize(screen, NEW_SIZE)
            screen = screen[:, :, :3]

            #Self driving code
            if(AI_ENABLED):
                modelInput = preprocess(screen)
                modelInput = np.expand_dims(modelInput, axis=0)
                prediction = model.predict(modelInput)
                steering = prediction[0][0]
                brake = prediction[1][0]
                throttle = prediction[2][0]
                steeringBefore = steering
                steering = sigmoid(steering, 5) #Tries to compensate for low sensitivity of GTA gamepad
                #print(steering, throttle) # Shows predictions from model
                #showFrameTime() #Shows average FPS
                setJoy(controller, steering, brake, throttle)

            #cv2.imshow(SCREEN_NAME, screen)
            key = cv2.waitKey(2)

            if(key == 13):
                AI_ENABLED = not AI_ENABLED
                print("AI Enabled: ", AI_ENABLED)
                if(not AI_ENABLED):
                    resetController(controller)
        except KeyboardInterrupt:
            print("Closing")
            break

resetController(controller)   
cv2.destroyAllWindows() 




