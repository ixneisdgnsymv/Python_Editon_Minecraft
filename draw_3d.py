from math import *
import pygame


def pos_3d(pos, cam_pos, d, rot):
    x = pos[0] - cam_pos[0]
    y = pos[1] - cam_pos[1]
    z = pos[2] - cam_pos[2]
    y_x = z * cos(rot[1]) + x * sin(rot[1])
    y_z = x * cos(rot[1]) + z * sin(rot[1])
    x_y = y * cos(rot[0]) + y_z * sin(rot[0])
    x_z = y_z * cos(rot[0]) + y * sin(rot[0])
    return y_x * d / x_z, x_y * d / x_z


def draw_3d_line(surface, start_pos, end_pos, cam_pos, d, rot):
    start = pos_3d(start_pos, cam_pos, d, rot)
    end = pos_3d(end_pos, cam_pos, d, rot)
    pygame.draw.line(surface, (255, 255, 255), start, end)
