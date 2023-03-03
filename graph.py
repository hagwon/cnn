import matplotlib.pyplot as plt

class Grape():
    def showPlot(slef, x, y, title, color, label):
        plt.title(title)
        for i in range(len(y)):
            plt.plot(x, y[i], color=color[i], label=label[i])
        plt.grid(True)
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()
        plt.show()

    def showImage(self, image, title):
        plt.title(title)
        plt.imshow(image, cmap=plt.cm.gray_r)
        plt.show()
    
