import cv2
import numpy as np 
from utils.images_utils import *


def cartoonify_image(image_path):
    image = load_image(image_path)
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur for noise reduction
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Convert pixel values to float
    gray = gray.astype(float)

    # Apply contrast adjustment using cv2.multiply
    contrasted_image = cv2.multiply(gray, np.array([1.5]))

    # Clip values to the valid range [0, 255]
    contrasted_image = np.clip(contrasted_image, 0, 255)

    # Convert back to uint8
    contrasted_image = contrasted_image.astype(np.uint8)

    # Apply Canny edge detector
    edges = cv2.Canny(contrasted_image, threshold1=30, threshold2=100)
    
    # Apply bilateral filter for smoothing
    smoothed = cv2.bilateralFilter(contrasted_image, d=9, sigmaColor=300, sigmaSpace=300)

    # Combine the edges and smoothed image
    cartoon = cv2.bitwise_and(smoothed, smoothed, mask=edges)
    return cartoon



    

