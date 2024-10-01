import py5
from scene.move import *
from scene.zoom import *
from shapelib import my_shape_class

# TODO: 子对象关系
shape_define = [
    #[my_shape_class(py5.rect, 100, 200, 70, 70), 0xFFFFFFFF],
    #[my_shape_class(py5.ellipse, 200, 200, 70, 70), 0xFFFF00FF],
    [my_shape_class(py5.rect, 100, 100, 70, 70), 0xFFFFFF00],
    [my_shape_class(py5.ellipse, 0, 320, 10, 10), 0xFF0000FF, cos_move(1, 100)],
    [my_shape_class(py5.ellipse, 400, 320, 5, 5), 0xFFFF00FF, sin_move(1, 100), line_zoom(1, 1)],
    [my_shape_class(py5.ellipse, 400, 320, 5, 5), 0xFFFF00FF, tan_move(1, 100)],
    [my_shape_class(py5.ellipse, 400, 320, 10, 10), 0xFFFF00FF, circle_move(50)],
    [my_shape_class(py5.ellipse, 400, 320, 10, 10), 0xFFFF00FF, ellipse_move(50, 25)],
    [my_shape_class(py5.ellipse, 400, 320, 10, 10), 0xFFFF00FF, ellipse_move(50, 0)],
    [my_shape_class(py5.ellipse, 400, 320, 10, 10), 0xFFFF00FF, line_move(0, 0, -1, 0)],
    [my_shape_class(py5.ellipse, 400, 320, 10, 10), 0xFF0000FF, no_move, abs_sin_zoom(100)],
    [my_shape_class(py5.ellipse, 320, 320, 30, 20), 0xFFFFFFFF, ellipse_move(20, 30, 0, 0)],
    [my_shape_class(py5.ellipse, 320, 320, 30, 20), 0xFFFFFFFF, ellipse_move(450, 380, 0, 100)],
]