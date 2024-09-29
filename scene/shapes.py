import py5
from scene.move import *
from scene.zoom import *
from shapelib import my_shape_class

shape_define = [
    [my_shape_class(py5.rect, 100, 200, 70, 70), 0xFFFFFFFF],
    [my_shape_class(py5.ellipse, 200, 200, 70, 70), 0xFFFF00FF],
    [my_shape_class(py5.rect, 100, 100, 70, 70), 0xFFFFFF00],
    [my_shape_class(py5.ellipse, 0, 320, 5, 5), 0xFF0000FF, m],
    [my_shape_class(py5.ellipse, 400, 320, 5, 5), 0xFFFF00FF, m1, z1]
]