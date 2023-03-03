from cnn import CNN
from graph import Grape
from camera import Camera
import time

if __name__ == '__main__':
    cnn = CNN(learning_rate=0.01, epochs=5, batch_size=64)
    graph = Grape()
    cam = Camera(0, 136, 'mnist')

    data_set = cnn.prepareData()
    model = cnn.buildModel()
    model, history = cnn.trainModel(
        model=model,
        train_images=data_set[cnn.TRAIN_IMAGES],
        train_labels=data_set[cnn.TRAIN_LABELS]
    )
    tra_acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    test_loss, test_acc = model.evaluate(
        data_set[cnn.TEST_IMAGES],
        data_set[cnn.TEST_LABEL]
    )
    print(f'test acc: {test_acc:.3f}')

    graph.showPlot(
        x = range(1, cnn.epochs+1),
        y = [tra_acc, val_acc],
        title='Train & Validation accuracy',
        color=['blue', 'red'],
        label=['Train accuracy', "Validation accuracy"]
    )

    '''data = data_set[cnn.TEST_IMAGES][7485]
    predicet = cnn.predict(model, data.reshape(1, cnn.WIDTH, cnn.HEIGHT, 1))
    graph.showImage(data.reshape((cnn.WIDTH, cnn.HEIGHT,)), title='Prediect: ' + str(predicet))
    data = data_set[cnn.TEST_IMAGES][14]
    predicet = cnn.predict(model, data.reshape(1, cnn.WIDTH, cnn.HEIGHT, 1))
    graph.showImage(data.reshape((cnn.WIDTH, cnn.HEIGHT,)), title='Prediect: ' + str(predicet))
    data = data_set[cnn.TEST_IMAGES][2497]
    predicet = cnn.predict(model, data.reshape(1, cnn.WIDTH, cnn.HEIGHT, 1))
    graph.showImage(data.reshape((cnn.WIDTH, cnn.HEIGHT,)), title='Prediect: ' + str(predicet))'''

    while True:
        cam.display()
        if cam.isRet() == True:
            data = cam.getFrame()
            data = data.reshape(1, cnn.WIDTH, cnn.HEIGHT, 1)
            predict = cnn.predict(model, data)
            print('Prediction: ', predict)
            #graph.showImage(data.reshape((cnn.WIDTH, cnn.HEIGHT,)), title='Prediect: ' + str(predict))
            time.sleep(0.1)
        if cam.isKey('q') == True:
            break

    cam.release()


    
    
