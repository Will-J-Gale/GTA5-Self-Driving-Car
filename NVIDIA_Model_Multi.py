from keras.models import Model
from keras.layers import Input, Activation, Dropout, Flatten, Dense
from keras.layers import Conv2D, MaxPooling2D
from keras.layers.normalization import BatchNormalization
from keras import regularizers

def NVIDIAModelMulti(inputShape = (270, 480, 3)):
    
    inputs = Input(shape = inputShape)
    
    x = BatchNormalization()(inputs)
    
    x = Conv2D(24, (5,5), padding='valid', strides=(2,2), activation='relu', name='Conv1')(x)
    x = BatchNormalization()(x)

    x = Conv2D(36, (5,5), padding='valid', strides=(2,2), activation='relu', name='Conv2')(x)
    x = BatchNormalization()(x)

    x = Conv2D(48, (5,5), padding='valid', strides=(2,2), activation='relu', name='Conv3')(x)
    x = BatchNormalization()(x)

    x = Conv2D(64, (3,3), padding='valid', strides=(2,2), activation='relu', name='Conv4')(x)
    x = BatchNormalization()(x)

    x = Conv2D(64, (5,5), padding='valid', strides=(2,2), activation='relu', name='Conv5')(x)
    x = BatchNormalization()(x)
    
    flatLayer = Flatten(name="Flatten")(x)
    steeringOutput = regressionHead(flatLayer, "Steering_Output", trainable = False)
    brakeOutput = regressionHead(flatLayer, "Brake_Output", trainable = False)
    throttleOutput = regressionHead(flatLayer, "Throttle_Output", trainable = False)
    
    model = Model(inputs=inputs, outputs=[steeringOutput, brakeOutput, throttleOutput], name="Self_Driving_Car")
    
    model.compile(loss='mean_squared_error', optimizer='adam')
    
    return model

def regressionHead(inputs, outputName="CREATE_NAME", trainable=True):
    
    x = Dense(1164, activation='relu', trainable=trainable)(inputs)
    x = Dense(100, activation='relu', trainable=trainable)(x)
    x = Dense(50, activation='relu', trainable=trainable)(x)
    x = Dense(10, activation='relu', trainable=trainable)(x)    
    x = Dense(1, activation='linear', name = outputName, trainable=trainable)(x)

    return x


    
    
