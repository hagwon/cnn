import cv2

class Camera():
    def __init__(self, target=0, threshold_value=127, title='untitle'):

        self.title = title
        cv2.namedWindow(self.title)
        cv2.createTrackbar("threshold", self.title, 0, 255, self.onChange)
        cv2.createTrackbar("maxValue", self.title, 0, 255, lambda x : x)
        cv2.setTrackbarPos("threshold", self.title, threshold_value)
        cv2.setTrackbarPos("maxValue", self.title, 255)
    
    def onChange(self, pos):
        pass

    def display(self):
        
    
    def isRet(self):
        ret = self.ret
        self.ret = False
        return ret
    
    def getFrame(self):
        return self.frame

    def isKey(self, key_value):
        if cv2.waitKey(33) == ord(key_value):
            return True
        else:
            return False

    def release(self):
        self.capture.release()
        cv2.destroyAllWindows()
    
    