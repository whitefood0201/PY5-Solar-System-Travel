import py5

def shape_saver(shape, x, y, w, h):
    def drawShape():
        shape(x, y, w, h)
    def back():
        nonlocal x, y
        x-=1
    return drawShape, back

def setup():
    py5.size(640, 640)
    py5.background(10, 10, 20)

def draw():
    py5.background(10, 10, 20)
    py5.fill(255)
    py5.rect(20, py5.height/2-20, 40, 40)

    py5.fill(255, 100, 100)
    ell1_draw()
    ell1_back()
    ell2_draw()
    ell2_back()
    ell3_draw()
    ell3_back()

ell1_draw, ell1_back = shape_saver(py5.ellipse, 100, 200, 70, 70)
ell2_draw, ell2_back = shape_saver(py5.ellipse, 400, 300, 100, 100)
ell3_draw, ell3_back = shape_saver(py5.ellipse, 600, 100, 50, 50)

py5.run_sketch()