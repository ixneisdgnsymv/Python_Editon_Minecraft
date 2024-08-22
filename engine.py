import tkinter as tk
import time
from draw_3d import *
class Game():
    def __init__(self, root):
        self.root = root
        self.root.title('Minecraft Python Editon')
        self.root.geometry('800x600')
        self.root.bind('<Key>', self.update)
        self.canvas = tk.Canvas(self.root, width=800, height=600)

        self.is_running = False
        self.seed = 0
        self.FPS = 0
        
        self.start_time = 0
        self.end_time = 0
        
        self.player_x = 0
        self.player_y = 0
        self.player_z = -100
        self.player_x_dir = 0
        self.player_y_dir = 0

        self.walk_speed = 5.0
        self.swim_speed = 3.0
    def update(self， event):
        if event.keysym == 'w':
            self.player_z += 50.0
        elif event.keysym == 's':
            self.player_z -= 50.0
        elif event.keysym == 'a':
            self.player_x -= 50.0
        elif event.keysym == 'd':
            self.player_x += 50.0
        elif event.keysym == 'Shift_L' or event.keysym == 'Shift_R':
            self.player_y -= 50.0
        elif event.keysym == 'Space':
            self.player_y += 50.0
        
        self.draw_square(0, 0, 0, 50, (self.player_x, self.player_y, self.player_z), (self.player_x_dir, self.player_y_dir))
    def draw_square(self, x, y, z, s, cam_pos, rot, d=300):
        draw_3d.draw_3d_line(self.canvas, (x-s, y+s, z-s), (x+s, y+s, z-s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x+s, y-s, z-s), (x+s, y+s, z-s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x+s, y-s, z-s), (x-s, y-s, z-s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x-s, y+s, z-s), (x-s, y-s, z-s), cam_pos, d, rot)

        draw_3d.draw_3d_line(self.canvas, (x-s, y+s, z+s), (x+s, y+s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x+s, y-s, z+s), (x+s, y+s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x+s, y-s, z+s), (x-s, y-s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x-s, y+s, z+s), (x-s, y-s, z+s), cam_pos, d, rot)

        draw_3d.draw_3d_line(self.canvas, (x+s, y+s, z-s), (x+s, y+s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x+s, y-s, z-s), (x+s, y-s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x-s, y+s, z-s), (x-s, y+s, z+s), cam_pos, d, rot)
        draw_3d.draw_3d_line(self.canvas, (x-s, y-s, z-s), (x-s, y-s, z+s), cam_pos, d, rot)


def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
if '__name__' == '__main__':
    main()
