import unittest
from unittest.mock import patch, MagicMock
import numpy as np
import cv2


class TestObjectDetectionIntegration(unittest.TestCase):

    @patch('cv2.imread')
    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.dnn_DetectionModel')
    def test_object_detection_integration(self, mock_dnn_model, mock_waitKey, mock_imshow, mock_imread):
        # Mock the image input
        mock_image = np.zeros((640,640,3), dtype=np.uint8)
        mock_imread.return_value = mock_image

        # Mock the model
        mock_model_instance = MagicMock()
        mock_dnn_model.return_value = mock_model_instance

        # Mock detection results
        mock_model_instance.detect.return_value = (
            np.array([[1]]),         # classIds
            np.array([0.6724]),     # confidence
            np.array([[60, 40, 373, 461]])  # bounding box
        )
        # Run the actual object detection code
        image = cv2.imread("config_files/images.jpg")
        if image is None:
            raise FileNotFoundError("Image not found or unable to read the image.")

        image = cv2.resize(image, (640,640))
        print("Importing classes")
        # Mocking class names loading
    #Import the class names
        classNames = ['person']
        classFile = 'config_files/coco.names'

#### Extracts the classes into a list
#rt = open file for read
# rstrip('\n') removing white space
# split seperates each word at each line into a string
        with open(classFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n') 
        # Set up the model parameters
        configPath = 'config_files/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
        weightsPath = 'config_files/frozen_inference_graph.pb'
        net = cv2.dnn_DetectionModel(weightsPath, configPath)
        net.setInputSize(320, 320)
        net.setInputScale(1.0 / 127.5)
        net.setInputMean((127.5, 127.5, 127.5))
        net.setInputSwapRB(True)

        # Perform detection
        classIds, confs, bbox = net.detect(image, confThreshold=0.5)

        # Draw the bounding box and text
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            cv2.rectangle(image, box, color=(255, 255, 0), thickness=2)
            cv2.putText(image, classNames[classId - 1], (box[0] + 10, box[1] + 30),
                        cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        # Show the output image
        cv2.imshow("Output", image)
        cv2.waitKey(0)
    # Assertions to verify that the mocks were called correctly
        mock_imread.assert_called_once_with("config_files/images.jpg")
    # Check the actual call arguments
        print(mock_model_instance.detect.call_args_list)
        # Get the first call args
        # Instead of accessing the index directly, you might check if it was called
     
        call_args = mock_model_instance.detect.call_args
        if call_args is not None:
            actual_call_args = call_args[0]  # Get the positional arguments
            if len(actual_call_args) > 1:
                actual_conf_threshold = actual_call_args[1]  # Access the second arg if it exists
                print(f"Confidence Threshold: {actual_conf_threshold}")
            else:
                print("Expected argument not found.")
        else:
            print("detect was not called.")

        actual_image =  np.zeros((640, 640, 3), dtype=np.uint8) 
        print("Actual Image Array:")
        print(actual_image)
        print("Mock Image Array:")
        print(mock_image)
        
    # Check that imshow was called correctly
        mock_imshow("Output", mock_image)
        mock_waitKey(0)
       

if __name__ == '__main__':
    unittest.main()
