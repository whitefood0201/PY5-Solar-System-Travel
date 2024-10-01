import py5
import functional.FLfunctions as fl
import functional.lambdas as la
from scene.shapes import *
from shapelib import *
        
def shapes_processor(shape_defines):
    def shapeGenerator(define:list):
        shape:my_shape_class = define[0]
        setters = [
            la.setter(shape, "color"),
            la.setter(shape, "move_func"),
            la.setter(shape, "zoom_func"),
        ]
        param = define[1:]
        for i in range(0, len(param)):
            setters[i](param[i])
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