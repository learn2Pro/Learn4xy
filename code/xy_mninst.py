#!/usr/bin/python
# -*- coding: UTF-8 -*-

from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D
from keras.datasets import mnist

# 0-9 数字一共10类
num_classes = 10 # class size
# input vector size image size 28*28
input_unit_size = 28*28

def loadmnist():
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    return (x_train, y_train), (x_test, y_test)


# 使用现成的模型 resnet
def createResnet():
    print("this is resnet")


# 1.创建模型
#  2. 结构
#   dense
#     |
#     V
#  activate
#     |
#     V
#   Dense
#     |
#     V
#   Dense
def createNormalModel():
    model = Sequential()
    model.add(Dense(units=64, input_dim=100))
    model.add(Activation("relu"))
    # model.add(Conv2D())
    model.add(Dense(units=num_classes))
    model.add(Activation("softmax"))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


# 1.创建cnn模型
#  2. 结构
#   conv2d
#     |
#     V
#   maxPool
#     |
#     V
#   activate
#     |
#     V
#   Dense
#     |
#     V
#   softmax
def createConvModel():
    model = Sequential()
    model.add(Conv2D())
    model.add(MaxPooling2D())
    model.add(Dense(units=64, input_dim=100))
    model.add(Activation("softmax"))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model


def trainModel(x_train, y_train, model):
    model.fit(x_train, y_train, epochs=5, batch_size=32)


def evaluate(x_test, y_test, model):
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
    return loss_and_metrics


def predict(x_test, model):
    classes = model.predict(x_test, batch_size=128)
    return classes


if __name__ == '__main__':
    print("this is main")
