import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
from tensorflow import keras
from keras import layers
from keras.datasets import mnist

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        # Only enable memory growth on available GPUs
        for device in physical_devices:
            tf.config.experimental.set_memory_growth(device, True)
        print("GPU memory growth enabled")
    except RuntimeError as e:
        print(f"GPU setup error: {e}")
else:
    print("No GPU devices found. Running on CPU.")

(x_train,y_train), (x_test, y_test)=mnist.load_data()
X_train = x_train.reshape(-1,28*28).astype("float32")/255.0
X_test = x_test.reshape(-1,28*28).astype("float32")/255.0

print(X_train.shape)
print(y_train.shape)

# Sequential API of Keras (convenient but not flexible)

## Building model with an including function
# model = keras.Sequential(
#     [
#         keras.Input(shape=(28*28,)),  # Add comma to make it a proper tuple
#         layers.Dense(512, activation='relu'),
#         layers.Dense(256, activation='relu'),
#         layers.Dense(10, activation='softmax')  # Add softmax for classification
#     ]
# )

## Building the model with a segmented function, so a print-function can be injected inbetween for better debugging
# model = keras.Sequential()
# model.add(keras.Input(shape=(28*28,)))
# model.add(layers.Dense(512, activation='relu'))
# print(model.summary())
# model.add(layers.Dense(256, activation='relu'))
# model.add(layers.Dense(10, activation='softmax'))
# 
# import sys
# sys.exit()

# Functional API (only use if neccessary!)

inputs = keras.Input(shape=(28*28,))
x = layers.Dense(512, activation='relu')(inputs)
x = layers.Dense(256, activation='relu')(x)
outputs = layers.Dense(10, activation='softmax')(x)
model = keras.Model(inputs=inputs, outputs=outputs)

model.compile(
    loss=keras.losses.SparseCategoricalCrossentropy(from_logits=False),
    optimizer=keras.optimizers.Adam(learning_rate=0.001),
    metrics=['accuracy']
)
model.fit(
    X_train,
    y_train,
    batch_size = 32,
    epochs = 5,
    verbose = 2
)
model.evaluate(
    X_test,
    y_test,
    batch_size = 32,
    verbose = 2
)
