import keras
import numpy
from keras import layers
from keras.datasets import mnist

class CNN():
    def __init__(self, learning_rate, epochs, batch_size):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.batch_size = batch_size
        self.TRAIN_IMAGES = 0
        self.TRAIN_LABELS = 1
        self.TEST_IMAGES = 2
        self.TEST_LABEL= 3
        self.WIDTH = 28
        self.HEIGHT = 28

    def prepareData(self):
        (train_images, train_labels), (test_images, test_labels) = mnist.load_data()
        train_images = train_images.reshape((60000, self.WIDTH, self.HEIGHT, 1))
        train_images = train_images.astype('float32') / 255
        test_images = test_images.reshape((10000, self.WIDTH, self.HEIGHT, 1))
        test_images = test_images.astype('float32') / 255

        data_set = [train_images, train_labels, test_images, test_labels]

        return data_set
    
    def buildModel(self):

        return model

    def trainModel(self, model, train_images, train_labels):
        x_val = train_images[:10000]
        partial_x_train = train_images[10000:]
        y_val = train_labels[:10000]
        partial_y_train = train_labels[10000:]

        return model, history

    def evaluateModel(self, model, test_images, test_labels):
        test_loss, test_acc = model.evaluate(test_images, test_labels)
        return test_loss, test_acc
    
    def predict(self, model, data):
        return numpy.argmax(model.predict(data))