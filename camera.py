import cv2

class Camera():
    def __init__(self, target=0, threshold_value=127, title='untitle'):
        self.capture = cv2.VideoCapture(target)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 640)
        self.title = title
        cv2.namedWindow(self.title)
        cv2.createTrackbar("threshold", self.title, 0, 255, self.onChange)
        cv2.createTrackbar("maxValue", self.title, 0, 255, lambda x : x)
        cv2.setTrackbarPos("threshold", self.title, threshold_value)
        cv2.setTrackbarPos("maxValue", self.title, 255)
    
    def onChange(self, pos):
        pass

    def display(self):
        ret, frame = self.capture.read()
        if ret == True:
            self.ret = ret
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            thresh = cv2.getTrackbarPos("threshold",self.title)
            maxval = cv2.getTrackbarPos("maxValue", self.title)
            _, dst = cv2.threshold(gray, thresh, maxval, cv2.THRESH_BINARY)
            cv2.imshow(self.title, dst)
            self.frame = cv2.resize(255 - dst, dsize=(28, 28), interpolation=cv2.INTER_NEAREST)
    
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
    
    