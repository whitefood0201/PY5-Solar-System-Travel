import py5
import shapelib.shapes as sp

def shapeDraw(shape:sp.AbsShape):
    shape.draw()
def shapeUpdate(shape:sp.AbsShape):
    shape.update()

def resetAll():
    py5.rect_mode(py5.CORNER)
    py5.text_align(py5.BASELINE)
    py5.fill(0)
    py5.text_size(16)

def drawText(text, x, y, size="32", color=0, align=py5.BASELINE):
    py5.fill(color)
    py5.text_size(size)
    py5.text_align(align)
    py5.text(text, x, y)
