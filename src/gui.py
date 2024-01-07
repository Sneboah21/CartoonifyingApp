import tkinter as tk
from tkinter import *
from tkinter import filedialog
import cv2
import numpy as np
from utils.images_utils import *
from cartoonifying import *
import os

OUT_PATH = os.path.join(os.getcwd(), "output")

class CartoonifyingApp:
    def __init__(self,master):
        self.master = master
        master.title("Cartoonifying App")
        self.select_image_button = tk.Button(master, text="Select Image", command=self.select_image, width=15, height=3)
        self.select_image_button.pack(pady=30)
        self.cartoonify_image_button = tk.Button(master, text="Cartoonify Image", command=self.cartoonify_image, width=15, height=3)
        self.cartoonify_image_button.pack(pady=30)

    def select_image(self):
        file_path = filedialog.askopenfilename(initialdir="images/", title="Select image", filetypes=(("Image files", "*.jpg; *.png"),("all files", "*.*")))
        if file_path:
            self.image_path = file_path
            self.original_image = load_image(file_path)
            display_image(self.original_image, "Original Image")

    def cartoonify_image(self):
        if hasattr(self, 'image_path'):
            cartooned_image = cartoonify_image(self.image_path)
            display_image(cartooned_image, "Cartoonified Image")
            save_image(cartooned_image, os.path.join(OUT_PATH, "out1.jpg"))
        else:
            print("Please select an image first.")