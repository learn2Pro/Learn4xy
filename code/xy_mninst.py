#!/usr/bin/python
# -*- coding: UTF-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Activation, Conv2D, MaxPooling2D, Flatten
from keras.datasets import mnist
from keras.utils import np_utils
import os
from keras.utils import plot_model
from keras.callbacks import EarlyStopping

# 0-9 数字一共10类
num_classes = 10  # class size
# input vector size image size 28*28
input_unit_size = 28 * 28
epoch_num = 20
batch_num = 128


def loadMnist():
    currentPath = os.path.abspath('.')
    (x_train, y_train), (x_test, y_test) = mnist.load_data(currentPath + "/../" + 'data/mnist.npz')
    return (x_train, y_train), (x_test, y_test)


# 使用现成的模型 resnet
def createResnet():
    print("this is resnet")


# 加工cnn mnist数据
def handleCNNData():
    (x_train, y_train), (x_test, y_test) = loadMnist()

    ##归一化数据
    x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
    x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255

    # one-hot representation
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)
    return (x_train, y_train), (x_test, y_test)


def handleNormalData():
    (x_train, y_train), (x_test, y_test) = loadMnist()
    ##归一化数据
    x_train = x_train.reshape(x_train.shape[0], input_unit_size)
    x_test = x_test.reshape(x_test.shape[0], input_unit_size)
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    # one-hot representation
    y_train = np_utils.to_categorical(y_train, num_classes)
    y_test = np_utils.to_categorical(y_test, num_classes)
    return (x_train, y_train), (x_test, y_test)


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
    denseModel = Sequential()
    denseModel.add(Dense(output_dim=128, input_dim=input_unit_size))
    denseModel.add(Activation("relu"))
    # model.add(Conv2D())
    denseModel.add(Dense(output_dim=num_classes))
    denseModel.add(Activation("softmax"))
    denseModel.compile(loss='categorical_crossentropy',
                       optimizer='adam',
                       metrics=['accuracy'])
    denseModel.summary()
    return denseModel


#### cnn model
# 28*28*1->28*28*64->14*14*64->7*7*256--->512-->dropOut->10
# conv2D
#   |
#   V
#  pool
#   |
#   V
#  relu
#   |
#   V
#  Dense
#   |
#   V
#  softMax
def createConvModel():
    cnnModel = Sequential()
    cnnModel.add(Conv2D(64, (2, 2), input_shape=(28, 28, 1)))
    cnnModel.add(Activation("relu"))
    cnnModel.add(MaxPooling2D(pool_size=(2, 2)))

    # BatchNormalization(axis=-1)
    cnnModel.add(Conv2D(128, (2, 2)))
    cnnModel.add(Activation('relu'))
    # BatchNormalization(axis=-1)
    cnnModel.add(Conv2D(256, (2, 2)))
    cnnModel.add(Activation('relu'))
    cnnModel.add(MaxPooling2D(pool_size=(2, 2)))

    # fully layer
    cnnModel.add(Flatten())

    cnnModel.add(Dense(512))
    # cnnModel.add(Dropout(0.1))
    cnnModel.add(Activation('relu'))
    # BatchNormalization()
    cnnModel.add(Dense(num_classes))
    cnnModel.add(Activation("softmax"))
    cnnModel.compile(loss='categorical_crossentropy',
                     optimizer='adam',
                     metrics=['accuracy'])

    # 打印模型结构
    cnnModel.summary()
    return cnnModel


def plotDenseResult(denseModel, denseResult):
    plot_model(denseModel, "data/denseModel.png")
    ### dense model graph
    x = range(denseResult.history.s)
    plt.plot(x, denseResult.history['acc'], label='train')
    plt.plot(x, denseResult.history['val_acc'], label='validation')
    plt.title('Accuracy')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

    plt.plot(x, denseResult.history['loss'], label='train')
    plt.plot(x, denseResult.history['val_loss'], label='validation')
    plt.title('Loss')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def plotCNNResult(cnnModel, cnnResult):
    plot_model(cnnModel, "data/cnnModel.png")

    ### cnn model graph

    x = range(cnnResult.length)
    plt.plot(x, cnnResult.history['acc'], label='train')
    plt.plot(x, cnnResult.history['val_acc'], label='validation')
    plt.title('Accuracy')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
    plt.show()

    plt.plot(x, cnnResult.history['loss'], label='train')
    plt.plot(x, cnnResult.history['val_loss'], label='validation')
    plt.title('Loss')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))


def trainModel(x_train, y_train, model):
    return model.fit(x_train, y_train, epochs=epoch_num, batch_size=batch_num,
                     verbose=2, validation_split=0.15,
                     callbacks=[EarlyStopping(monitor='val_loss',
                                              patience=1, verbose=2,
                                              mode='auto')])


def evaluate(x_test, y_test, model):
    loss_and_metrics = model.evaluate(x_test, y_test, batch_size=batch_num)
    return loss_and_metrics


def predict(x_test, model):
    classes = model.predict(x_test, batch_size=128)
    return classes


if __name__ == '__main__':
    print("this is main")
    (x_train, y_train), (x_test, y_test) = handleNormalData()
    model = createNormalModel()
    result = trainModel(x_train, y_train, model)
    print("this is main"+result.epoch.size)
    # plotDenseResult(model, result)
