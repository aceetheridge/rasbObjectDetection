
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
  boxes = tensorOut(interpreter, 0)
  classes = tensorOut(interpreter, 1)
  scores = tensorOut(interpreter, 2)
  count = np.array(tensorOut(interpreter, 3)).size
  

  results = []
  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results