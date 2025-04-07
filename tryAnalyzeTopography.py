"""
Topography Analyser with Elevation Detection and Vector Visualization
-----------------------------------------------------------------------

Original Code By: M. Nabil Alhanif
Original Title: Topography Analyzer
Original Purpose: Select points on an image and calculate distance between them

Developed by: Farrel Aryo Wahyudi (UBC Applied Science Student)

Modifications: 
  - Added elevation detection using RGB color mapping
  - Included support for elevation delta computation
  - Visualized vectors between base and target points
  - Organized output into tables for analysis

Tools Used:
  - Pillow (PIL) for image processing
  - Tkinter for GUI

Date: 2025

Purpose:
  This tool allows users to select reference and target points on a topographic map image,
  automatically compute displacement, distance, and elevation difference, and visualize 
  directional vectors from the reference point.

"""


import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def get_elevation_from_color(rgb):
    colorbar_colors = [
        ((90, 58, 34), 22.5),
        ((117, 80, 45), 20),
        ((140, 105, 60), 15),
        ((160, 130, 80), 10),
        ((170, 170, 100), 5),
        ((190, 210, 130), 0),
        ((200, 230, 170), -2.5),
        ((220, 245, 210), -5),
        ((230, 250, 235), -7.5),
        ((240, 255, 255), -10)
    ]
    # Convert RGB to a tuple of floats
    min_dist = float('inf')
    elevation = None
    for color, elev in colorbar_colors:
        dist = sum((a - b) ** 2 for a, b in zip(rgb, color))
        if dist < min_dist:
            min_dist = dist
            elevation = elev
    return elevation

class ImageDistanceCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Distance and Elevation Calculator")

        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        self.img = None
        self.photo_img = None
        self.image_path = ""

        self.point1 = None
        self.point2 = []

        self.canvas.bind("<Button-1>", self.select_point)

        select_button = tk.Button(self.root, text = "Select Image", command = self.open_image)
        select_button.pack()

        calculate_button = tk.Button(self.root, text = "Calculate Distance & Elevation", command = self.calculate_distance)
        calculate_button.pack()

        delete_button = tk.Button(self.root, text = "Clear Dots", command = self.clear)
        delete_button.pack()

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            self.img = Image.open(self.image_path).convert("RGB")
            self.photo_img = ImageTk.PhotoImage(self.img)
            self.canvas.config(width = self.img.width, height = self.img.height)
            self.canvas.create_image(0, 0, anchor = tk.NW, image = self.photo_img)

    def select_point(self, event):
        if self.img:
            if not self.point1:
                current_point = self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="red")
                self.point1 = (current_point, event.x, event.y)
            else:
                current_point = self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill="blue")
                self.point2.append((current_point, event.x, event.y))

    def calculate_distance(self):
        if self.point1 and self.point2:
            arr = []
            width, height = self.img.width, self.img.height

            base_x, base_y = self.point1[1], self.point1[2]
            base_rgb = self.img.getpixel((base_x, base_y))
            base_elev = get_elevation_from_color(base_rgb)

            for p2 in self.point2:
                px, py = p2[1], p2[2]

                act_x = px - base_x
                x_dist = abs(act_x) * 120 / width
                x_dist = round(x_dist)
                if act_x < 0:
                    x_dist *= -1

                act_y = py - base_y
                y_dist = abs(act_y) * 120 / height
                y_dist = round(y_dist)
                if act_y > 0:
                    y_dist *= -1

                rgb = self.img.getpixel((px, py))
                elev = get_elevation_from_color(rgb)
                elev_diff = round(elev - base_elev, 2)

                distance = (x_dist ** 2 + y_dist ** 2) ** 0.5

                arr.append((distance, x_dist, y_dist, elev, elev_diff))
            
            arr.sort()
            for i in arr:
                print(f"Distance: {i[0]:.2f} m | Δx: {i[1]} m | Δy: {i[2]} m | Elevation: {i[3]} m | Elevation Δ: {i[4]} m")
            print(f"Reference Elevation at base point: {base_elev} m")
            print("DONE")
        else:
            print("Please select two points on the image.")

    def clear(self):
        if self.point1:
            self.canvas.delete(self.point1[0])
            self.point1 = None
        for p in self.point2:
            self.canvas.delete(p[0])
        self.point2.clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageDistanceCalculator(root)
    root.mainloop()
