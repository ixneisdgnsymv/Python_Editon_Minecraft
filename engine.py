import tkinter as tk
from draw_3d import *
cam_x = 0
cam_y = 0
cam_z = 0
rot_x = 0
rot_y = 0
def on_key_press():
    if event.keysym == 'w':
        cam_z += 5.0
    elif event.keysym == 's':
        cam_z -= 5.0
    elif event.keysym == 'a':
        cam_x -= 5.0
    elif event.keysym == 'd':
        cam_x += 5.0
    elif event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
        cam_y -= 5.0
    elif event.keysym == 'Space':
        cam_y += 5.0
def main():
    root = tk.Tk()
    root.mainloop()
