from keras.models import Sequential, Model
from keras.layers import Activation, Dropout, UpSampling2D, Input, Dense, Permute, Reshape, Activation, Flatten
from keras.layers import Conv2DTranspose, Conv2D, MaxPooling2D, Concatenate
from keras.layers.normalization import BatchNormalization
from keras.optimizers import Adam
from keras import regularizers
from keras.utils.vis_utils import plot_model as plot

def SelfDrivingCarModel(inputShape=(256, 256, 3)):
    dropoutAmount = 0.5
    poolSize = (2,2)
    
    inputLayer = Input(shape=inputShape)

    conv1 = Conv2D(32, 3, activation='relu', padding='same')(inputLayer)
    conv1 = Conv2D(32, 3, activation='relu', padding='same')(conv1)
    pool1 = MaxPooling2D(pool_size=poolSize)(conv1)

    conv2 = Conv2D(64, 3, activation='relu', padding='same')(pool1)
    conv2 = Conv2D(64, 3, activation='relu', padding='same')(conv2)
    pool2 = MaxPooling2D(pool_size=poolSize)(conv2)

    conv3 = Conv2D(128, 3, activation='relu', padding='same')(pool2)
    conv3 = Conv2D(128, 3, activation='relu', padding='same')(conv3)
    pool3 = MaxPooling2D(pool_size=poolSize)(conv3)

    conv4 = Conv2D(256, 3, activation='relu', padding='same')(pool3)
    conv4 = Conv2D(256, 3, activation='relu', padding='same')(conv4)
    drop4 = Dropout(dropoutAmount)(conv4)
    pool4 = MaxPooling2D(pool_size=poolSize)(conv4)

    flat = Flatten()(pool4)
    
    steeringOutput = regressionHead(flat)
    throttleOutput = regressionHead(flat)
                        
    model = Model(inputs=inputLayer, outputs=[steeringOutput, throttleOutput])

    return model

def regressionHead(layer, dropoutAmount=0.5):
    dense1 = Dense(256, activation = "relu")(layer)
    drop6 = Dropout(dropoutAmount)(dense1)

    dense2 = Dense(128, activation = "relu")(drop6)
    drop7 = Dropout(dropoutAmount)(dense2)

    dense3 = Dense(64, activation = "relu")(drop7)
    drop8 = Dropout(dropoutAmount)(dense3)

    dense4 = Dense(24, activation = "relu")(drop8)
    drop9 = Dropout(dropoutAmount)(dense4)
    
    output = Dense(1, activation = "linear")(drop9)

    return output

    
