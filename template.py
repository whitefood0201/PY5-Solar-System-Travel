import py5
import functional.FLfunctions as fl
import shapelib.shapeFactory as sf
import shapelib.shapes as sp
from shapelib.shapes import *
        
def shapeDraw(shape:sp.absShape):
    shape.draw()
def shapeUpdate(shape:sp.absShape):
    shape.update()

def initShapes():
    shapes = sf.shapes_processor("shape.xml")
    def updateShapes():
        nonlocal shapes
        shapes = fl.filter(lambda shp: not shp.removed(), shapes)
        fl.map(shapeUpdate, shapes)
    def getShapes():
        return shapes
    return updateShapes, getShapes
updateShapes, getShapes = initShapes()

def setup():
    py5.size(640, 640)

def draw():
    sps = getShapes()
    py5.background(10, 10, 20)
    fl.map(shapeDraw, sps)
    updateShapes()

py5.run_sketch()