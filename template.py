import py5
import functional.FLfunctions as fl
from scene.shapes import *
from shapelib import *
        
def shapes_processor(shape_defines):
    def shapeGenerator(define:list):
        shape:my_shape_class = define[0]
        for i in range(1, len(define)):
            if i == 1:
                shape.color = define[1]
            if i == 2:
                shape.move_func = define[2]
            if i == 3:
                shape.zoom_func = define[3]
        return shape
    savers = fl.map(shapeGenerator, shape_defines)
    return savers

shapes = shapes_processor(shape_define)

def shapeDraw(shape:my_shape_class):
    shape.draw()
def shapeUpdate(shape:my_shape_class):
    shape.update()

def setup():
    py5.size(640, 640)

def draw():
    py5.background(10, 10, 20)
    fl.map(shapeDraw, shapes)
    fl.map(shapeUpdate, shapes)
    
py5.run_sketch()