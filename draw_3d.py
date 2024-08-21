from math import *


def pos_3d(pos, cam_pos, d, rot):
    x = pos[0] - cam_pos[0]
    y = pos[1] - cam_pos[1]
    z = pos[2] - cam_pos[2]
    y-x = z * cos(rot[1]) + x * sin(rot[1])
    y-z = x * cos(rot[1]) + z * sin(rot[1])
    x-y = y * cos(rot[0]) + y-z * sin(rot[0])
    x-z = y-z * cos(rot[0]) + y * sin(rot[0])
    return y-x * d / x-z, x-y * d / x-z
