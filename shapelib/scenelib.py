import py5

def shapeDraw(shape):
    shape.draw()

def shapeUpdate(tick):
    def update(shape):
        shape.update(tick)
    return update

def resetAll():
    py5.rect_mode(py5.CORNER)
    py5.text_align(py5.BASELINE)
    py5.fill(0)
    py5.text_size(16)
    py5.no_stroke()
    py5.stroke_weight(0)
    py5.text_align(py5.BASELINE)
    py5.text_size(1)

def drawText(text, x, y, size="32", color=0, align=py5.BASELINE):
    py5.fill(color)
    py5.text_size(size)
    py5.text_align(align)
    py5.text(text, x, y)

def getRotation(ori_x:float, ori_y:float, angle:float):
    """
        angle: angle of rotation specified in radians
    """
    def rotate():
        py5.push_matrix()
        py5.translate(ori_x, ori_y)
        py5.rotate(angle)
        py5.translate(-ori_x, -ori_y)

    def endRotate():
        py5.pop_matrix()
    
    return rotate, endRotate