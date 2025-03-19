import unittest
from unittest.mock import patch, MagicMock
from unittest.mock import patch, MagicMock, call
import cv2
import numpy as np

def process_image(model):
    model.setInputSize(320, 320)
    model.setInputScale(1.0 / 127.5)
    model.setInputMean((127.5, 127.5, 127.5))
    model.setInputSwapRB(True)
    
class TestObjectDetection(unittest.TestCase):

    @patch('cv2.imread')
    @patch('cv2.dnn_DetectionModel')
    def test_image_reading_and_model_setup(self, mock_dnn_model, mock_imread):
        # Mock image reading
        mock_imread.return_value = np.zeros((640, 640, 3), dtype=np.uint8)  # Mock an image

        # Mock the model and its methods
        mock_model_instance = MagicMock()
        mock_dnn_model.return_value = mock_model_instance
        process_image(mock_model_instance)
        # Execute the image processing code
        image = cv2.imread("config_files/images.jpg")
        image = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)
        
        # Assert that image was read and resized
        self.assertIsNotNone(image)
        self.assertEqual(image.shape, (1280, 1280, 3))

        # Assert model methods were called correctly
        mock_model_instance.setInputSize.assert_called_with(320, 320)
        mock_model_instance.setInputScale.assert_called_with(1.0 / 127.5)
        mock_model_instance.setInputMean.assert_called_with((127.5, 127.5, 127.5))
        mock_model_instance.setInputSwapRB.assert_called_with(True)
        
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data='person\ncar\nbike\n')
    def test_class_names_loading(self, mock_file):
        classFile = 'config_files/coco.names'
        
        # Load class names
        with open(classFile, 'rt') as f:
            classNames = f.read().rstrip('\n').split('\n')
        
        # Assert class names are loaded correctly
        self.assertEqual(classNames, ['person', 'car', 'bike'])

    @patch('cv2.imshow')
    @patch('cv2.waitKey')
    @patch('cv2.rectangle')
    @patch('cv2.putText')
    @patch('cv2.dnn_DetectionModel')
    def test_detection_and_drawing(self, mock_dnn_model, mock_putText, mock_rectangle, mock_waitKey, mock_imshow):
        # Mock image and detection
        image = np.zeros((640, 640, 3), dtype=np.uint8)
        mock_model_instance = MagicMock()
        mock_model_instance.detect.return_value = (np.array([[1]]), np.array([0.6724]), np.array([[60, 40, 373, 461]]))
        mock_dnn_model.return_value = mock_model_instance

        classNames = ['person']

        # Perform detection
        classIds, confs, bbox = mock_model_instance.detect(image, confThreshold=0.5)

        # Simulate drawing on the image
        for classId, confidence, box in zip(classIds.flatten(), confs.flatten(), bbox):
            box_tuple = tuple(box)  # Convert to tuple
            mock_rectangle(image, box_tuple, color=(255, 255, 0), thickness=2)
            mock_putText(image, classNames[classId - 1], (box[0] + 10, box[1] + 30),
                         cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
           # Debugging print statements
        print("Preparing to show image with mock_imshow.")
        print(f"Image shape: {image.shape}")
        print("Image array:", image)

    # Call imshow here to ensure it's being called in the actual logic
    # (You might want to do this in your main code instead)
        mock_imshow("output",np.zeros((640, 640, 3), dtype=np.uint8)) # Simulate showing the image
        mock_waitKey(0)
        print("After calling imshow:")
        print("All calls to mock_imshow:", mock_imshow.call_args_list)

        # Assert rectangle and text drawing functions were called
        expected_box = (60, 40, 373, 461)
        mock_rectangle.assert_any_call(image,expected_box, color=(255, 255, 0), thickness=2)
        mock_putText.assert_called_with(image, 'person', (70, 70), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
        mock_imshow.assert_called()
        last_call_args = mock_imshow.call_args[0]  # Get the last call arguments
        assert np.array_equal(last_call_args[1], image), "The image passed to imshow does not match."

        # Test showing image (just ensure it runs)
        mock_imshow("Output",np.zeros((640, 640, 3), dtype=np.uint8))
        mock_waitKey(0)

if __name__ == '__main__':
    unittest.main()
