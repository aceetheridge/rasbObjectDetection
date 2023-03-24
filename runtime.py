import re
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
from createLabels import *
from tensorHelpers import *

inX = 640
inY = 480
labelPath = "./partslist2-1.csv"


def main():
    labels = createLabels(labelPath)
    interpreter = Interpreter('detect.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']

    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, frame = cap.read()
        img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (320,320))
        res = applyTensors(interpreter, img, 0.7)
        print(res)

        for result in res:
            ymin, xmin, ymax, xmax = result['bounding_box']
            xmin = int(max(1,xmin * inX))
            xmax = int(min(inX, xmax * inX))
            ymin = int(max(1, ymin * inY))
            ymax = int(min(inY, ymax * inY))
            
            cv2.rectangle(frame,(xmin, ymin),(xmax, ymax),(0,255,0),3)
            cv2.putText(frame,labels[int(result['class_id'])],(xmin, min(ymax, inY-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA) 

        cv2.imshow('Pi Feed', frame)

        if cv2.waitKey(10) & 0xFF ==ord('q'):
            cap.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    main()