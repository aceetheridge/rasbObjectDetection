
import numpy as np
import cv2

def tensorIn(interpreter, image):
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = np.expand_dims((image-255)/255, axis=0)


def tensorOut(interpreter, index):
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor

def applyTensors(interpreter, image, threshold):
  tensorIn(interpreter, image)
  cv2.imshow('Pi Feed', image)
  interpreter.invoke()
  classes = tensorOut(interpreter, 3)
  boxes = tensorOut(interpreter, 1)
  count = tensorOut(interpreter, 2)
  scores: np.ndarray = tensorOut(interpreter, 0)
 
  
  

  results = []
  for i in range(0, count.size):
      if scores[i] >= threshold:
          try:
              bounding_box = boxes[i]
          except:
              bounding_box = [0.0, 0.0, 0.0, 0.0]
          result = {
              "bounding_box": bounding_box,
              "class_id": classes[i],
              "score": scores[i],
          }
          results.append(result)
  return results